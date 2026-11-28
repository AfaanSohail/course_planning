"""Audit supplied model artifacts without changing responses or assigning grades."""
import argparse,csv,hashlib,json
from reasoning import KG
from reasoning.kg import ROOT,save_json
from app.service import citation_ids


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(rows):
    cleaned=[]
    for row in rows:
        row=dict(row)
        for key in ('stillRequired','mentions','blockingConditions','couldCountToward','allocatedTo','courses'):
            value=row.get(key)
            if isinstance(value,str):
                sep=' | ' if ' | ' in value else ', '
                row[key]=sep.join(sorted(value.split(sep)))
        cleaned.append(json.dumps(row,sort_keys=True))
    return sorted(cleaned)


def audit(run_id):
    folder=ROOT/'evaluation/results'/run_id
    manifest=json.loads((folder/'manifest.json').read_text())
    cases=json.loads((folder/'cqs.snapshot.json').read_text());kg=KG();findings=[];checks=[];edges={}
    if digest(folder/'cqs.snapshot.json')!=manifest['cqs_sha256']:findings.append('Expected snapshot hash mismatch')
    if kg.sha256!=manifest['graph_sha256']:findings.append('Graph hash mismatch')
    grades={(g['cq'],g['condition']):g for g in csv.DictReader((folder/'grades.csv').open())}
    for case in cases:
        for mode in 'AB':
            path=folder/f"{case['id']}_{mode}.json";d=json.loads(path.read_text());completion=d['completion']
            request=completion['request'];raw=completion['raw'];messages=request.get('messages',[]);issues=[]
            available={e['id'] for e in d.get('context',{}).get('evidence',[])}|{r['id'] for r in d.get('context',{}).get('rows',[])}
            if d['question']!=case['question']:issues.append('question_mismatch')
            if d.get('config')!=manifest['config']:issues.append('config_mismatch')
            if digest(path)!=grades[(case['id'],mode)]['raw_sha256']:issues.append('grade_hash_mismatch')
            for key in ('model','temperature','max_tokens'):
                if request.get(key)!=manifest['config'][key]:issues.append('request_'+key+'_mismatch')
            prompt='baseline.txt' if mode=='A' else 'grounded.txt'
            if not messages or hashlib.sha256(messages[0]['content'].encode()).hexdigest()!=manifest['prompt_hashes'][prompt]:issues.append('prompt_hash_mismatch')
            if raw.get('choices',[{}])[0].get('message',{}).get('content')!=d['answer']:issues.append('answer_differs_from_raw')
            if mode=='A' and (d.get('evidence') or len(messages)!=2 or messages[-1]['content']!=case['question']):issues.append('baseline_not_isolated')
            if mode=='B':
                if canonical(d['retrieval']['rows'])!=canonical(case['expected']):issues.append('retrieved_rows_differ_from_expected')
                for e in d['evidence']:edges[(e['s'],e['p'],e['o'],e['status'])]=e
            checks.append({'cq':case['id'],'condition':mode,'llm_called':d.get('llm_called',False),
                           'finish_reason':completion.get('finish_reason'),'truncated':completion.get('truncated',False),
                           'unknown_citation_ids':sorted(set(citation_ids(d['answer']))-available) if mode=='B' else [],
                           'issues':issues,'raw_sha256':digest(path),
                           'review_complete':all(grades[(case['id'],mode)].get(k,'').strip() for k in
                           ('correct','evidence_available','unsupported_claims','reviewer','notes'))})
    invalid=[e for e in edges.values() if not kg.valid_edge(e)]
    summary={'run_id':run_id,'manifest':manifest,'case_count':len(cases),'response_records':len(checks),
             'llm_calls_recorded':sum(bool(x['llm_called']) for x in checks),'checks':checks,'integrity_findings':findings,
             'distinct_evidence_edges_checked':len(edges),'invalid_evidence_edges':len(invalid),
             'complete_human_reviews':sum(bool(x['review_complete']) for x in checks),
             'truncated_responses':[x['cq']+'_'+x['condition'] for x in checks if x['truncated']],
             'records_with_unknown_citations':[x['cq']+'_'+x['condition'] for x in checks if x['unknown_citation_ids']],
             'note':'Internal consistency of supplied records does not independently prove provider execution or semantic correctness.'}
    save_json(folder/'artifact_audit.json',summary)
    print(json.dumps({k:v for k,v in summary.items() if k not in {'checks','manifest'}},indent=2));return summary


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--run-id',default='qwen3_trial1');args=parser.parse_args();audit(args.run_id)
