"""Record only project-relevant runtime versions, without environment secrets."""
import platform
from importlib.metadata import version
from reasoning.kg import ROOT


if __name__=="__main__":
    packages=["rdflib","owlrl","pyparsing","pandas","requests","pytest","pyshacl","reportlab","python-docx"]
    text="Python: "+platform.python_version()+"\nPlatform: "+platform.platform()+"\n"
    text+="\n".join(name+"=="+version(name) for name in packages)+"\n"
    (ROOT/"evaluation/results/environment.txt").write_text(text)
    print(text)
