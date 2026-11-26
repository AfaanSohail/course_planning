"""Read-only live GraphDB query execution; no repository is modified."""
import argparse
import requests
from evaluation.queries import catalog
from reasoning.kg import save_json

if __name__ == "__main__":
    p=argparse.ArgumentParser();p.add_argument("--endpoint",default="http://localhost:7200/repositories/Project_uiuc")
    p.add_argument("--query",default="Q11");p.add_argument("--output",required=True)
    a=p.parse_args();q=catalog()[a.query]["query"]
    response=requests.post(a.endpoint,data={"query":q,"infer":"true"},headers={"Accept":"application/sparql-results+json"},timeout=120)
    response.raise_for_status();save_json(a.output,{"endpoint":a.endpoint,"query":q,"result":response.json()})
    print(response.text)
