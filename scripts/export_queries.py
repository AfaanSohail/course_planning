from evaluation.queries import catalog
from reasoning.kg import ROOT

if __name__ == "__main__":
    folder=ROOT/"evaluation/queries";folder.mkdir(parents=True,exist_ok=True)
    for key,item in catalog().items():
        (folder/f"{key}.rq").write_text(item["query"],encoding="utf-8")
    print("Exported original standalone queries to evaluation/queries/.")
