# Research notes: Afaan's scope

Option C answers a question by following connected graph relations and retaining the intermediate nodes. In this domain a course-to-course hop expands into course → expression → option → condition → candidate course. A transcript decision also joins student → completion → completed course. The implementation adds Boolean condition evaluation, cycle guards and a stored trace to reachability.

Lao and Cohen (2010) model relational retrieval using weighted sequences of edge labels. This informed our use of typed paths, but we do not fit their path weights or implement their path-ranking algorithm. Xiong, Hoang and Wang (2017) learn multi-hop paths with reinforcement learning in DeepPath; Das et al. (2018) learn query-conditioned navigation in MINERVA. They establish the broader research setting. Our graph is small and its prerequisite semantics require exact conjunctions, so we enumerate bounded paths deterministically instead of learning a navigation policy. No neural training, held-out link prediction, learned confidence or claim of reproducing those papers is made.

Hogan et al. (2021) discuss graph models, querying, deductive and inductive techniques. This informed the separation between stored RDF, OWL deductions, closed-world application rules and predictions. The W3C SPARQL specification defines the property-path reference used by the validation, including nonzero cycles. OWL RL supplies the schema closure; it does not by itself perform a student's closed-world prerequisite audit.

References (primary sources, checked 21 November 2026):

- Lao, N. & Cohen, W. W. (2010). *Relational retrieval using a combination of path-constrained random walks*. Machine Learning 81, 53–67. https://doi.org/10.1007/s10994-010-5205-8
- Xiong, W., Hoang, T. & Wang, W. Y. (2017). *DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning*. EMNLP, 564–573. https://doi.org/10.18653/v1/D17-1060
- Das, R. et al. (2018). *Go for a Walk and Arrive at the Answer: Reasoning Over Paths in Knowledge Bases using Reinforcement Learning*. ICLR. https://arxiv.org/abs/1711.05851
- Hogan, A. et al. (2021). *Knowledge Graphs*. ACM Computing Surveys 54(4), Article 71. https://doi.org/10.1145/3447772
- Harris, S. & Seaborne, A. (eds., 2013). *SPARQL 1.1 Query Language*. W3C. https://www.w3.org/TR/sparql11-query/
- W3C (2012). *OWL 2 Web Ontology Language Profiles (Second Edition)*. https://www.w3.org/TR/owl2-profiles/
