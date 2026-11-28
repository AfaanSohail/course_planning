"""Provision a task-local Ollama runtime and record a separate real experiment.

Writes progress/errors, never fabricates completions or edits an earlier trial.
The official release asset digest is checked before executing the full runtime.
"""
import hashlib,json,os,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
import requests

ROOT=Path(__file__).resolve().parents[1]
JOB=ROOT/'evaluation/results/local_execution'
RUN='qwen3_trial2_local'
RUNTIME=Path('/tmp/course_planning_ollama_runtime')
PACKAGE=Path('/tmp/course_planning_ollama_linux.tar.zst')
EXPECTED_SIZE=1648243083
EXPECTED_HASH='b82649006cb5b54ed1237fa2d1a26a7f939a4fd03150033759acbff7ff315adf'
URL='https://github.com/ollama/ollama/releases/download/v0.40.18/ollama-linux-amd64.tar.zst'


def status(stage,**extra):
    JOB.mkdir(parents=True,exist_ok=True)
    value={'stage':stage,'updated_utc':datetime.now(timezone.utc).isoformat(),'run_id':RUN,'pid':os.getpid(),**extra}
    temporary=JOB/'status.tmp';temporary.write_text(json.dumps(value,indent=2)+'\n');temporary.replace(JOB/'status.json')
    print(json.dumps(value),flush=True)


def execute(command,**kwargs):
    print('EXEC',command,flush=True)
    subprocess.run(command,cwd=ROOT,check=True,**kwargs)


def main():
    server=None
    try:
        status('downloading_runtime',expected_bytes=EXPECTED_SIZE,package=str(PACKAGE))
        for attempt in range(4):
            if PACKAGE.exists() and PACKAGE.stat().st_size==EXPECTED_SIZE:break
            code=subprocess.run(['curl','--silent','--show-error','--location','--fail','--max-time','7200',
                                 '--continue-at','-',URL,'--output',str(PACKAGE)]).returncode
            if code==0:break
            print('Download attempt returned',code,flush=True)
        if not PACKAGE.exists() or PACKAGE.stat().st_size!=EXPECTED_SIZE:raise RuntimeError('Runtime download incomplete')
        checksum=hashlib.sha256()
        with PACKAGE.open('rb') as stream:
            for chunk in iter(lambda:stream.read(8*1024*1024),b''):checksum.update(chunk)
        if checksum.hexdigest()!=EXPECTED_HASH:raise RuntimeError('Official runtime digest verification failed')
        status('extracting_cpu_runtime')
        RUNTIME.mkdir(parents=True,exist_ok=True)
        execute(['tar','--zstd','-xf',str(PACKAGE),'-C',str(RUNTIME),
                 '--exclude=lib/ollama/cuda*','--exclude=lib/ollama/vulkan*','--exclude=lib/ollama/rocm*'])
        env=dict(os.environ,OLLAMA_HOST='127.0.0.1:11435',OLLAMA_MODELS='/tmp/course_planning_ollama_models',
                 OLLAMA_NO_CLOUD='1',OLLAMA_NUM_PARALLEL='1',OLLAMA_MAX_LOADED_MODELS='1',
                 OLLAMA_FLASH_ATTENTION='1',OLLAMA_KV_CACHE_TYPE='q8_0')
        binary=str(RUNTIME/'bin/ollama')
        log=(JOB/'server.log').open('a')
        server=subprocess.Popen([binary,'serve'],env=env,stdout=log,stderr=subprocess.STDOUT)
        for _ in range(30):
            if server.poll() is not None:raise RuntimeError('Local server failed; inspect server.log')
            try:
                if requests.get('http://127.0.0.1:11435/api/version',timeout=2).ok:break
            except requests.RequestException:pass
            time.sleep(1)
        else:raise RuntimeError('Local server did not become ready')
        status('downloading_model',model='qwen3:4b-instruct')
        execute([binary,'pull','qwen3:4b-instruct'],env=env,timeout=10800)
        execute([binary,'create','course-planning-qwen3-v2','-f','config/Modelfile.rerun'],env=env)
        config=json.loads((ROOT/'config/rerun.example.json').read_text())
        config['base_url']='http://127.0.0.1:11435/v1'
        # CPU calls can take many minutes; failures still remain explicit.
        config['timeout_seconds']=7200
        config_path=JOB/'execution_config.json';config_path.write_text(json.dumps(config,indent=2)+'\n')
        (JOB/'runtime_environment.json').write_text(json.dumps({
            'ollama_version':'0.40.18','cpu_only':True,'parallel_calls':1,
            'flash_attention_requested':True,'kv_cache_type_requested':'q8_0',
            'runtime_package_sha256':EXPECTED_HASH,'model_storage':env['OLLAMA_MODELS']},indent=2)+'\n')
        status('running_experiment',response_directory=str(ROOT/'evaluation/results'/RUN))
        execute([sys.executable,'-m','evaluation.prepare'])
        execute([sys.executable,'-u','-m','evaluation.run','--config',str(config_path),'--run-id',RUN,'--conditions','AB'])
        execute([sys.executable,'-m','evaluation.score','--run-id',RUN,'--init'])
        execute([sys.executable,'-m','scripts.audit_received_run','--run-id',RUN])
        status('responses_complete_grading_pending',response_directory=str(ROOT/'evaluation/results'/RUN))
    except KeyboardInterrupt:
        status('paused',reason='Execution interrupted by user; completed response artifacts are preserved.')
        raise SystemExit(130)
    except BaseException as error:
        status('failed',error=f'{type(error).__name__}: {error}',log=str(JOB/'job.log'))
        raise
    finally:
        if server is not None:
            server.terminate()
            try:server.wait(timeout=30)
            except subprocess.TimeoutExpired:server.kill()


if __name__=='__main__':main()
