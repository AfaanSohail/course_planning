"""Display actual run artifacts and optionally capture the real desktop window.

This viewer never generates model answers or draws a substitute screenshot. Pillow
captures the visible Tk window after it has been rendered by the desktop.
"""
import argparse
import subprocess
import csv
import json
import tkinter as tk
from tkinter import ttk
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--record',type=Path)
    p.add_argument('--comparison',action='store_true')
    p.add_argument('--capture',type=Path)
    args=p.parse_args()
    if bool(args.record)==args.comparison:p.error('Choose --record or --comparison')
    root=tk.Tk();root.title('course_planning | Actual execution evidence')
    root.geometry(('1100x650+80+70' if args.comparison else '1100x800+80+70'));root.configure(background='#eef2f5')
    ttk.Label(root,text='course_planning | Actual execution evidence',font=('Sans',16,'bold')).pack(anchor='w',padx=16,pady=10)
    body=ttk.Frame(root,padding=12);body.pack(fill='both',expand=True)
    if args.comparison:
        meta=json.loads((ROOT/'report/submission.json').read_text())
        folder=ROOT/'evaluation/results'/meta['llm_run_id']
        summary=json.loads((folder/'summary.json').read_text())
        rows=list(csv.DictReader((folder/'grades.csv').open()))
        ttk.Label(body,text='Recorded Kaggle experiment: '+meta['llm_run_id'],font=('Sans',12)).pack(anchor='w')
        totals=' | '.join(f"{mode}: {summary['conditions'][mode]['correct']}/{summary['questions']} correct, {summary['conditions'][mode]['unsupported_claims']} unsupported claims" for mode in 'AB')
        ttk.Label(body,text=totals,font=('Sans',13,'bold')).pack(anchor='w',pady=8)
        columns=['CQ','Correct A','Correct B','Evidence A','Evidence B']
        ttk.Style().configure('Treeview',font=('Sans',12),rowheight=32)
        ttk.Style().configure('Treeview.Heading',font=('Sans',12,'bold'))
        tree=ttk.Treeview(body,columns=columns,show='headings',height=10)
        for c in columns:tree.heading(c,text=c);tree.column(c,width=180,anchor='w')
        bykey={(r['cq'],r['condition']):r for r in rows}
        for cq in dict.fromkeys(r['cq'] for r in rows):
            a,b=bykey[(cq,'A')],bykey[(cq,'B')]
            tree.insert('',tk.END,values=[cq,a['correct'],b['correct'],a['evidence_available'],b['evidence_available']])
        tree.pack(fill='both',expand=True,pady=8)
        ttk.Label(body,text='A = LLM only. B = KG grounded. Strict correctness requires a complete answer with no unsupported conclusions.').pack(anchor='w',pady=6)
        ttk.Label(body,text='Source: '+str(folder/'grades.csv')).pack(anchor='w')
        ttk.Label(body,text='Full questions, expected rows and raw answers are in comparison.csv and the preserved response JSON files.').pack(anchor='w')
    else:
        record=json.loads(args.record.read_text())
        ttk.Label(body,text='Question: '+record['question'],font=('Sans',13,'bold'),wraplength=1040).pack(anchor='w')
        completion=record.get('completion',{})
        settings=record.get('config',{})
        ttk.Label(body,text=f"Mode: {record['mode']} | LLM called: {record.get('llm_called')} | Model: {settings.get('model','not called')} | Finish: {completion.get('finish_reason','not called')}").pack(anchor='w',pady=6)
        text=tk.Text(body,wrap='word',font=('DejaVu Sans Mono',13),background='white')
        scroll=ttk.Scrollbar(body,command=text.yview);text.configure(yscrollcommand=scroll.set)
        scroll.pack(side='right',fill='y');text.pack(fill='both',expand=True)
        text.insert('end','ACTUAL RESPONSE\n\n'+record['answer']+'\n\nRETRIEVED QUERY RESULTS\n')
        retrieval=record.get('retrieval',{})
        for i,row in enumerate(retrieval.get('rows',[]),1):text.insert('end',f'[R{i}] '+json.dumps(row,ensure_ascii=False)+'\n')
        text.insert('end','\nGRAPH EVIDENCE (first three edges; full evidence in saved JSON)\n')
        for e in record.get('evidence',[])[:3]:
            def compact(term):
                return term.replace('<https://example.org/uiuc-course-advisor/resource/','res:').replace('<https://example.org/uiuc-course-advisor/ontology#','uca:').replace('>','')
            text.insert('end',f"[{e['id']}] {e['status']}: {compact(e['s'])} {compact(e['p'])} {compact(e['o'])}\n")
        text.insert('end','\nIRIs abbreviated with res:/uca:; exact triples are saved in the JSON.\nEvidence edges: '+str(len(record.get('evidence',[])))+' | Graph SHA256: '+retrieval.get('graph_sha256','unavailable'))
        text.configure(state='disabled')
        ttk.Label(body,text='Source: '+str(args.record.resolve())).pack(anchor='w',pady=6)
    if args.capture:
        def capture():
            root.lift();root.attributes('-topmost',True);root.update()
            args.capture.parent.mkdir(parents=True,exist_ok=True)
            # XWayland does not expose the root screen; capture our own mapped X11 window.
            import struct
            from PIL import Image
            raw=args.capture.with_suffix('.xwd')
            subprocess.run(['/usr/bin/xwd','-silent','-id',hex(root.winfo_id()),'-out',str(raw)],check=True)
            data=raw.read_bytes();header=struct.unpack('>25I',data[:100])
            size,version,fmt,depth,width,height,offset,order,unit,bitorder,pad,bpp,stride,visual,red,green,blue,bits,entries,ncolors,*rest=header
            if not (version==7 and fmt==2 and bpp==32 and order==0 and (red,green,blue)==(0xff0000,0xff00,0xff)):
                raise RuntimeError('Unsupported XWD pixel format; preserve raw capture for inspection.')
            Image.frombytes('RGB',(width,height),data[size+ncolors*12:],'raw','BGRX',stride,1).save(args.capture)
            raw.unlink()
            print('Captured actual visible window:',args.capture,flush=True)
            root.after(300,root.destroy)
        root.after(2000,capture)
    root.mainloop()


if __name__=='__main__':main()
