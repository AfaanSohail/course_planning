# course_planning

**AI-3001 Knowledge Representation & Reasoning | Iteration 1**

**Names:** Afaan Sohail, Hassan Tariq, Diya Hurmat 

**Roll Numbers:** 24I-0081, 24I-2555, 24I-0094 

**Section:** AI-A / AI-C

## About the project

This project builds a knowledge graph for university course planning using the UIUC Fall 2026 course catalog and BS Computer Science degree requirements. It models courses, prerequisites, offerings and degree requirements so students can check eligibility and identify missing requirements.

## Requirements

- Python 3 with `pandas`, `rdflib` and `pyshacl`
- GraphDB for running SPARQL queries
- Protégé for inspecting the ontology

Install the Python packages from the submission folder:

```bash
pip install pandas rdflib pyshacl
```

## Build and validate the knowledge graph

The RDF files are already included in `RDF_Knowledge_Graph/`. To rebuild them from the supplied data, run:

```bash
python Code/build_kg.py --output-dir rebuilt
```

`prereq_parser.py` is used by the build script to parse prerequisite text. `curated_corrections.json` contains reviewed fixes needed to reproduce the submitted graph, so keep all three files together in `Code/`.

To validate the submitted graph against its SHACL shapes, run:

```bash
pyshacl -s RDF_Knowledge_Graph/shapes.ttl -i rdfs RDF_Knowledge_Graph/uiuc_course_kg.ttl
```

## Run the queries in GraphDB

1. Create a GraphDB repository with the **OWL2-RL** ruleset (or OWL-Horst).
2. Import `RDF_Knowledge_Graph/uiuc_course_kg.ttl`. The graph contains **28,638 asserted triples**.
3. Open `SPARQL_Queries/queries.txt` and copy each labelled query into GraphDB's SPARQL editor, including the common `BASE`/`PREFIX` declarations.
4. Run the queries one at a time. Compare the outputs with the CSV files in `Results/query_results/`.

Some queries depend on inference. In particular, **Q11 and INF1–INF6** need the reasoning ruleset enabled to return their recorded results.

## Folder contents

- `Dataset/`: source catalog and prerequisite cross-check data
- `Code/`: graph builder, prerequisite parser and curated corrections
- `Ontology/`: OWL/Turtle ontology
- `RDF_Knowledge_Graph/`: graph data and SHACL shapes
- `SPARQL_Queries/`: queries used in GraphDB
- `Results/`: saved query outputs and explanations
- `Visualization/`: GraphDB and Protégé screenshots
- `Report/`: combined Iteration 1 report

**Note:** The student records in the graph are synthetic examples. The course offerings reflect the supplied Fall 2026 snapshot, not live registration availability.
