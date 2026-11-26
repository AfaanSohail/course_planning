# Explainability record

Question: Which courses are at least two prerequisite-course links upstream of a selected target course, and through which alternative branches are they reachable? Instance: CS 440.

Mode: grounded

## Generated text (LLM)

| upstreamCode | viaCode  | firstHop                     |
|-------------|----------|-----------------------------|
| BIOE 210    | BIOE 310 | via one-of group (potential)|
| CS 101      | BIOE 310 | via one-of group (potential)|
| CS 101      | ECE 313  | via one-of group (potential)|
| CS 124      | BIOE 310 | via one-of group (potential)|
| CS 124      | CS 225   | via required course        |
| CS 125      | CS 225   | via required course        |
| CS 126      | CS 225   | via required course        |
| CS 128      | CS 225   | via required course        |
| CS 173      | CS 225   | via required course        |
| CS 374      | CS 225   | via required course        |
| CS 413      | CS 225   | via required course        |
| ECE 120     | CS 225   | via required course        |
| ECE 220     | CS 225   | via required course        |
| MATH 112    | BIOE 310 | via one-of group (potential)|
| MATH 112    | CS 225   | via required course        |
| MATH 112    | CS 361   | via one-of group (potential)|
| MATH 112    | ECE 313  | via one-of group (potential)|
| MATH 112    | MATH 461 | via one-of group (potential)|
| MATH 112    | STAT 400 | via one-of group (potential)|
| MATH 115    | BIOE 310 | via one-of group (potential)|
| MATH 115    | CS 225   | via required course        |
| MATH 115    | CS 361   | via one-of group (potential)|
| MATH 115    | ECE 313  | via one-of group (potential)|
| MATH 115    | MATH 461 | via one-of group (potential)|
| MATH 115    | STAT 400 | via one-of group (potential)|
| MATH 213    | CS 225   | via required course        |
| MATH 220    | BIOE 310 | via one-of group (potential)|
| MATH 220    | CS 225   | via required course        |
| MATH 220    | CS 361   | via one-of group (potential)|
| MATH 220    | ECE 313  | via one-of group (potential)|
| MATH 220    | MATH 461 | via one-of group (potential)|
| MATH 220    | STAT 400 | via one-of group (potential)|
| MATH 221    | BIOE 310 | via one-of group (potential)|
| MATH 221    | CS 225   | via required course        |
| MATH 221    | CS 361   | via one-of group (potential)|
| MATH 221    | ECE 313  | via one-of group (potential)|
| MATH 221    | MATH 461 | via one-of group (potential)|
| MATH 221    | STAT 400 | via one-of group (potential)|
| MATH 231    | BIOE 310 | via one-of group (potential)|
| MATH 231    | CS 225   | via required course        |
| MATH 231    | ECE 313  | via one-of group (potential)|
| MATH 231    | MATH 461 | via one-of group (potential)|
| MATH 231    | STAT 400 | via one-of group (potential)|
| MATH 241    | BIOE 310 | via one-of group (potential)|
| MATH 241    | CS 225   | via required course        |
| MATH 241    | ECE 313  | via one-of group (potential)|
| MATH 241    | MATH 461 | via one-of group (potential)|
| MATH 257    | BIOE 310 | via one-of group (potential)|
| MATH 257    | ECE 313  | via one-of group (potential)|
| MATH 314    | CS 225   | via required course        |
| MATH 314    | ECE 313  | via one-of group (potential)|
| MATH 347    | CS 225   | via required course        |
| MATH 347    | ECE 313  | via one-of group (potential)|
| MATH 412    | CS 225   | via required course        |
| MATH 413    | CS 225   | via required course        |
| MATH 416    | ECE 313  | via one-of group (potential)|
[R1], [R2], [R3], [R4], [R5], [R6], [R7], [R8], [R9], [R10], [R11], [R12], [R13], [R14], [R15], [R16], [R17], [R18], [R19], [R20], [R21], [R22], [R23], [R24], [R25], [R26], [R27], [R28], [R29], [R30], [R31], [R32], [R33], [R34], [R35], [R36], [R37], [R38], [R39], [R40], [R41], [R42], [R43], [R44], [R45], [R46], [R47], [R48], [R49], [R50], [R51], [R52], [R53], [R54], [R55], [R56]

## Explicit knowledge (stored RDF)

- [Ebac390cd31212005] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ec92778016a6d84e5] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 210 Linear Algebra for Biomedical Data Science"`
- [E8d291110ac67bf92] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#courseCode> "BIOE 210"`
- [E4e48060676adad89] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E4decf53ef3700b48] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ee57183269117eb2c] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Using analytical and computational tools from linear algebra, students will Solve large systems of linear equations, systems of linear ODEs, and linear PDEs; Analyze large, multivariable datasets to quantify relationships between variables; Decompose complex datasets into simpler representations; Introduce and solve common problems in classification, image processing, and machine learning; Develop a geometric understanding of high-dimensional spaces. Prerequisite: CS 101 or CS 124, and MATH 231."`
- [Ee2fee289d15a39d1] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "210"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E67d8e7c03b5d4865] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Linear Algebra for Biomedical Data Science"`
- [E98d8b32d094eeb41] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/BIOE210/2026-fa>`
- [E67e36c0ac57f3473] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/BIOE210>`
- [E8d9a6bbb6151baa9] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/BIOE>`
- [Ef4867d5e49d49755] `<https://example.org/uiuc-course-advisor/resource/course/BIOE210> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E4bd4f87492d8a02c] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ebd352bbf3cacff47] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of BIOE 210"`
- [E74be519238125da9] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1>`
- [E133b8e432cdfada7] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [Eb95a86c69fe02db6] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "CS 101 or CS 124, and MATH 231."`
- [E781fbeb2e173a5d2] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E670d42f6bac97a15] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 210 prerequisite option 1"`
- [Ef5a99c288db5abe2] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/1>`
- [Ee6e5664b7afd3c7d] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/2>`
- [E50ba4949c2c5d717] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E6940e45f48258990] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 210 opt 1 cond 1: one of CS 101, CS 124"`
- [Ee0e45857edf21bb4] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E217756c1414d9965] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS101>`
- [E3d74418a20409591] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS124>`
- [Ea405322c1034e391] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "CS 101 or CS 124"`
- [E045163f918dba766] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [Ea3014f0a5e490ae7] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 210 opt 1 cond 2: requires MATH 231"`
- [Eb4ea448666c5fb33] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E45144ff004cdc882] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 231"`
- [E53e5027f35db40b3] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE210/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH231>`
- [E3075522cd20a5da4] `<https://example.org/uiuc-course-advisor/resource/offering/BIOE210/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E3e7532bd6b009f63] `<https://example.org/uiuc-course-advisor/resource/offering/BIOE210/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 210 (Fall 2026)"`
- [Ed1b4d6b689de15b3] `<https://example.org/uiuc-course-advisor/resource/offering/BIOE210/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E872cc596cefc6092] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E064d928d455c8918] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 310 Computational Tools for Biological Data"`
- [E0939cb3540da0213] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#courseCode> "BIOE 310"`
- [E6be082eb03928bac] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E3a11c503de2dace3] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E66c0d15a121653fe] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Fundamental and applied statistics, including probability distributions, parameter estimation, descriptive statistics, hypothesis testing, and linear regression. Statistical methods in genomics including sequence analysis, gene expression data analysis, human genomic variation, regulatory genomics, and cancer genomics. Credit is not given towards graduation for both BIOE 310 and IE 300. Prerequisite: BIOE 210 or MATH 257. Students in the BS-BIOE must take BIOE 210 as the prerequisite."`
- [E50448f14cdfcd14f] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "310"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Eec3b7bbd277c3b11] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Computational Tools for Biological Data"`
- [Ed8a0425b1b9202b9] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/BIOE310/2026-fa>`
- [E80b528e2bb575f47] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/BIOE310>`
- [Eb5fd6b6cb97e787d] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/BIOE>`
- [E1ea77bf6c4fe58f8] `<https://example.org/uiuc-course-advisor/resource/course/BIOE310> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Ef421a93348d9a872] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Eb82955dde9e1a067] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of BIOE 310"`
- [E83cf73af3777ad2b] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1>`
- [E2ac640048414c674] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [Ed508584126fab918] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "BIOE 210 or MATH 257."`
- [E4833d31b99a2d197] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Ea9e7aaa618cd6356] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 310 prerequisite option 1"`
- [Eeb15be84a4b5f420] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1/condition/1>`
- [Ee2cc22e2242e86ad] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E164098be08e8625e] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 310 opt 1 cond 1: one of BIOE 210, MATH 257"`
- [Eb57cf45e49f47aeb] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E136607b895f93a4b] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/BIOE210>`
- [E78e2edc3b30a17d0] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH257>`
- [Edbc90e931ab9b841] `<https://example.org/uiuc-course-advisor/resource/prereq/BIOE310/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "BIOE 210 or MATH 257"`
- [E572280dbea6a6ca0] `<https://example.org/uiuc-course-advisor/resource/offering/BIOE310/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Eefad4363b2ce9e3a] `<https://example.org/uiuc-course-advisor/resource/offering/BIOE310/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "BIOE 310 (Fall 2026)"`
- [Ec13a799fe4302dd6] `<https://example.org/uiuc-course-advisor/resource/offering/BIOE310/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E44e70fbde445dbd5] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ee706845a34d64e1f] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <http://www.w3.org/2000/01/rdf-schema#label> "CS 101 Intro Computing: Engrg & Sci"`
- [Ed8f9691e53731be6] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 101"`
- [E95653a605d0ac22c] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E165c6ba5ed0b1ed8] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E8e6b077968aa1ed1] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Fundamental principles, concepts, and methods of computing, with emphasis on applications in the physical sciences and engineering. Basic problem solving and programming techniques; fundamental algorithms and data structures; use of computers in solving engineering and scientific problems. Intended for engineering and science majors. Prerequisite: One of MATH 220 or MATH 221 or MATH 231 or MATH 241."`
- [E9f87e43f31cf9f5f] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "101"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E038395483ded606b] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Intro Computing: Engrg & Sci"`
- [E415215b76a69c862] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning II course."`
- [E5949b47d5299142c] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS101/2026-fa>`
- [E1c487d3810afe747] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS101>`
- [Ec47f11ad21448159] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [Ee819dc4b0acbe6c7] `<https://example.org/uiuc-course-advisor/resource/course/CS101> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E5c3c0d7daddd2e74] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E6525928c70773a3b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 101"`
- [Ed8cccba23979fe1a] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1>`
- [E82573be386e25bba] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E8c3c58060174baaa] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "One of MATH 220 or MATH 221 or MATH 231 or MATH 241."`
- [E2dcb2cf526d5c810] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E87003bfe47ec8123] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 101 prerequisite option 1"`
- [Eedd011e0107d1272] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1>`
- [E8cd098dd59b3670f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [Ed17d2e7acc4b6b89] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 101 opt 1 cond 1: one of MATH 220, MATH 221, MATH 231, MATH 241"`
- [Ef437a2579ddf5e12] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ec1fb7fb8e13ac600] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH220>`
- [E2bb4ccf3d85e4a94] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH221>`
- [E9b47cb87f7159439] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH231>`
- [Edb69620f34850fd4] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH241>`
- [Ebfe00c2f9d8e8a0b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS101/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "One of MATH 220 or MATH 221 or MATH 231 or MATH 241"`
- [E5f957f4be07c67f7] `<https://example.org/uiuc-course-advisor/resource/offering/CS101/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E0e968e561f984db8] `<https://example.org/uiuc-course-advisor/resource/offering/CS101/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 101 (Fall 2026)"`
- [Ecc7b19bfa7c27011] `<https://example.org/uiuc-course-advisor/resource/offering/CS101/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E838f0d98183cec68] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ef48951b9bd274b43] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <http://www.w3.org/2000/01/rdf-schema#label> "CS 124 Introduction to Computer Science I"`
- [E1fcf7be4468d66f4] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 124"`
- [Efa8e8d4dcf0fd599] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ed751d1e2b7268589] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E6d9269f13209c25a] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Basic concepts in computing and fundamental techniques for solving computational problems. Intended as a first course for computer science majors and others with a deep interest in computing. Credit is not given for both CS 124 and CS 125. Prerequisite: Three years of high school mathematics or MATH 112."`
- [E5a33683ccfdf5893] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "124"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Eec5332bf5e90a331] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Introduction to Computer Science I"`
- [E5742d453b32ca4a1] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning I course."`
- [E63f7e22751148a6a] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS124/2026-fa>`
- [Ecc9b3a294217d544] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS124>`
- [E2f64e8898710c461] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [E6ec92f1cba8f5fc0] `<https://example.org/uiuc-course-advisor/resource/course/CS124> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Eea253d9c0dae4149] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Edd9f7a1999e12b92] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 124"`
- [E417540648d3e00c2] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1>`
- [E63d56ae927bd119a] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E85cf3c3aebe2f82f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "Three years of high school mathematics or MATH 112."`
- [E73220d38a074e0ec] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Ed5db2bbd948a69f5] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 124 prerequisite option 1"`
- [E8abb2b5d5c5c224f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1/condition/1>`
- [E1f48a3e7941c6087] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [Ec3d95f3ad9532449] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 124 opt 1 cond 1: requires MATH 112"`
- [E12a223f9bbcde860] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E2bd998796eecc217] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "Three years of high school mathematics or MATH 112"`
- [Ef3cc26264f77a179] `<https://example.org/uiuc-course-advisor/resource/prereq/CS124/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH112>`
- [E4904b5aa5701ae63] `<https://example.org/uiuc-course-advisor/resource/offering/CS124/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E166d892a19c71cec] `<https://example.org/uiuc-course-advisor/resource/offering/CS124/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 124 (Fall 2026)"`
- [E0db3bf811001bfac] `<https://example.org/uiuc-course-advisor/resource/offering/CS124/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Eef02f8978cbfa501] `<https://example.org/uiuc-course-advisor/resource/course/CS125> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E9c10118c9485c2a6] `<https://example.org/uiuc-course-advisor/resource/course/CS125> <http://www.w3.org/2000/01/rdf-schema#comment> "Referenced by a prerequisite, cross-listing or degree requirement but not present in the Fall 2026 catalog snapshot; only its code is known."`
- [E3e852ce803d291ec] `<https://example.org/uiuc-course-advisor/resource/course/CS125> <http://www.w3.org/2000/01/rdf-schema#label> "CS 125"`
- [Efab002ec88bd1e0a] `<https://example.org/uiuc-course-advisor/resource/course/CS125> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 125"`
- [E4900703ac293cb78] `<https://example.org/uiuc-course-advisor/resource/course/CS125> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "125"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Edf2d98405542117c] `<https://example.org/uiuc-course-advisor/resource/course/CS125> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [E7e65d299837b5b69] `<https://example.org/uiuc-course-advisor/resource/course/CS126> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E0f86c583f5635bf4] `<https://example.org/uiuc-course-advisor/resource/course/CS126> <http://www.w3.org/2000/01/rdf-schema#comment> "Referenced by a prerequisite, cross-listing or degree requirement but not present in the Fall 2026 catalog snapshot; only its code is known."`
- [E3d61a42385afd54a] `<https://example.org/uiuc-course-advisor/resource/course/CS126> <http://www.w3.org/2000/01/rdf-schema#label> "CS 126"`
- [E7426ee563b2fec1a] `<https://example.org/uiuc-course-advisor/resource/course/CS126> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 126"`
- [E6d1b4d3a0649a9d3] `<https://example.org/uiuc-course-advisor/resource/course/CS126> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "126"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Edda0d6102e5ae3d8] `<https://example.org/uiuc-course-advisor/resource/course/CS126> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [Ea8ffece13b5cb779] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Edad867a5663e4499] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <http://www.w3.org/2000/01/rdf-schema#label> "CS 128 Introduction to Computer Science II"`
- [E8cce4cdfde5690ce] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 128"`
- [Ea0be06ba64f86f3c] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E6d621ff9c1a95dc6] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E6c933d12417b359b] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Continuation of CS 124. More advanced concepts in computing and techniques and approaches for solving computational problems. Prerequisite: CS 124 or CS 125."`
- [E6915325250573537] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "128"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E4b6f189e8ef73464] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Introduction to Computer Science II"`
- [Ef4e1fde7e0f708e1] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning II course."`
- [E4ce1181ae5ae610d] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS128/2026-fa>`
- [E0a755a445b3026dd] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS128>`
- [Ea168e3b07c1fb23e] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [Ef7ebb69006729377] `<https://example.org/uiuc-course-advisor/resource/course/CS128> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E2dda29e326c5d6dc] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ecde708966330687c] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 128"`
- [E3e6fe0a8307a1c9d] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1>`
- [E0dd51261b2f77579] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [Edf9b90d3ba077a36] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "CS 124 or CS 125."`
- [E2e152800f6f08710] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E32f673f7fdf7fcac] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 128 prerequisite option 1"`
- [E4f1e982f936c6b52] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1/condition/1>`
- [E8451e88f42f9455e] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E22ee8ee7721f2f3f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 128 opt 1 cond 1: one of CS 124, CS 125"`
- [E55e3c849105d41ed] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ee9d66e3bc4d9f7f8] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS124>`
- [E0cdae48605071fb0] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS125>`
- [Eb13b74a4ef871cee] `<https://example.org/uiuc-course-advisor/resource/prereq/CS128/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "CS 124 or CS 125"`
- [E266379eaab32074d] `<https://example.org/uiuc-course-advisor/resource/offering/CS128/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E5c7954f30682d3a8] `<https://example.org/uiuc-course-advisor/resource/offering/CS128/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 128 (Fall 2026)"`
- [E49018aab0d41bf2d] `<https://example.org/uiuc-course-advisor/resource/offering/CS128/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Ef9a5f97680c9fd68] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ebb867ffffe4238cd] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <http://www.w3.org/2000/01/rdf-schema#label> "CS 173 Discrete Structures"`
- [E6c6a3098c316db46] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 173"`
- [E7d2e098a0245dfe4] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ea81136622b7a67c4] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Eb0a25ccba29614fd] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "[IAI Code: CS915] Discrete mathematical structures frequently encountered in the study of Computer Science. Sets, propositions, Boolean algebra, induction, recursion, relations, functions, and graphs. Credit is not given toward graduation for: Credit is not given for both CS 173 and MATH 213. Prerequisite: One of CS 124, CS 125, ECE 220; one of MATH 220, MATH 221."`
- [E6684ee8c8c0c1784] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "173"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ee6e2acb7948f9506] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Discrete Structures"`
- [E8138e9b067368771] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS173/2026-fa>`
- [E05938bf20462b32c] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS173>`
- [E45697bb5a032f998] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [E0bc5dd2f301cd32f] `<https://example.org/uiuc-course-advisor/resource/course/CS173> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E0101dbbc31042b84] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E2bcbc3d5e71192d5] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 173"`
- [E24b6c81a80ad63fa] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1>`
- [Ebcdbc4296c8e11a2] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E1be730724459abf4] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "One of CS 124, CS 125, ECE 220; one of MATH 220, MATH 221."`
- [Eb8439025def1b855] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Ea91854f5cf960564] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 173 prerequisite option 1"`
- [Ea89a9102e1b7e195] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1>`
- [E7cef7e3622fba7d2] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/2>`
- [E3d3130c54b67bcdb] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E15f83b12bcc6110d] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 173 opt 1 cond 1: one of CS 124, CS 125, ECE 220"`
- [E577ce5d94b09efec] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ecf32e4cb15b244a4] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS124>`
- [E5d9cb5b9375359f8] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS125>`
- [E2ce43784beacd98b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/ECE220>`
- [E7ade5da7e517db8e] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "One of CS 124, CS 125, ECE 220"`
- [Ecd6b1d428fbd872b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [Eccdead9ffdf8da04] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "CS 173 opt 1 cond 2: one of MATH 220, MATH 221"`
- [Ecf3e97660a9fbf03] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E8c9476f27bdb2078] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH220>`
- [E464ea481a6c140ba] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH221>`
- [Ea9c98b018a204494] `<https://example.org/uiuc-course-advisor/resource/prereq/CS173/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "one of MATH 220, MATH 221"`
- [E92efc5cbf975c5d2] `<https://example.org/uiuc-course-advisor/resource/offering/CS173/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Ecbb0e06b4a8d434a] `<https://example.org/uiuc-course-advisor/resource/offering/CS173/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 173 (Fall 2026)"`
- [Efa67908533b7c7c4] `<https://example.org/uiuc-course-advisor/resource/offering/CS173/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E0625d1a10951c04a] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ef6250f1467e9f33b] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <http://www.w3.org/2000/01/rdf-schema#label> "CS 225 Data Structures"`
- [Eb746603c1c043e25] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 225"`
- [E2a0ab3affd56da76] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E525b54b4c992e80d] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E9d6d116d588144aa] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Data abstractions: elementary data structures (lists, stacks, queues, and trees) and their implementation using an object-oriented programming language. Solutions to a variety of computational problems such as search on graphs and trees. Elementary analysis of algorithms. Credit is not given toward graduation for: CS 277 if credit for CS 225 has been earned. Prerequisite: CS 126 or CS 128 or ECE 220; One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413."`
- [E0e8ade3b5b16673f] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "225"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ee41c87e02e326107] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Data Structures"`
- [E0906273cb30ed7e7] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning II course."`
- [E11a95c231ae76d72] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS225/2026-fa>`
- [E14232750a0c5ce2a] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS225>`
- [Ea09beebf99a55fd2] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [E0183854f1908f9f0] `<https://example.org/uiuc-course-advisor/resource/course/CS225> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E80c7a0dfb2f76099] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ec7cc789deaa5f42f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 225"`
- [Eb56731794700854c] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1>`
- [Ef1396d3b9b3f3689] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [Eb3b90ce941307476] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "CS 126 or CS 128 or ECE 220; One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413."`
- [Eb262281bd7545686] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Eaca0d99fe680b9d5] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 225 prerequisite option 1"`
- [Eabf1c4c5e09b8325] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1>`
- [E40700508eb48a59e] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2>`
- [E705b9f19a16409ee] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E215e5ba02c2c0e64] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 225 opt 1 cond 1: one of CS 126, CS 128, ECE 220"`
- [Ea7d8b61b207d0a42] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E03989594b7c28dfe] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS126>`
- [Ea7db7c7fc7edd0c2] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS128>`
- [E46c3b2b6460b39e9] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/ECE220>`
- [E6a645816b515ecc2] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "CS 126 or CS 128 or ECE 220"`
- [Eb2aced7db8fa481e] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E9f909a2df6fa9680] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "CS 225 opt 1 cond 2: one of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, MATH 413"`
- [E653cc9595b10e7c7] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E499175b462fd8a5f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS173>`
- [Eeefa4b77cf92a747] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS413>`
- [E29a37c890bb278f4] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH213>`
- [Ec9b178bad57f933f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH314>`
- [E39ff2c6e69714992] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH347>`
- [Ee57309b00ee201f7] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH412>`
- [E4ff2e2a99b8c6627] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH413>`
- [E2f2d1f47ac976448] `<https://example.org/uiuc-course-advisor/resource/prereq/CS225/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413"`
- [E27db7ecc298f4943] `<https://example.org/uiuc-course-advisor/resource/offering/CS225/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E30240a7b403d8f43] `<https://example.org/uiuc-course-advisor/resource/offering/CS225/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 225 (Fall 2026)"`
- [E869cf2393e38e119] `<https://example.org/uiuc-course-advisor/resource/offering/CS225/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Ef2e5335688ee637c] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E27237b819924ac11] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <http://www.w3.org/2000/01/rdf-schema#label> "CS 361 Probability & Statistics for Computer Science"`
- [E153b165cd1fd4a4e] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 361"`
- [Ee00d48ebd6d1fefd] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E2b25514b7f7ed39c] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E6d77b2aea734feb3] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Introduction to probability theory and statistics with applications to computer science. Topics include: visualizing datasets, summarizing data, basic descriptive statistics, conditional probability, independence, Bayes theorem, random variables, joint and conditional distributions, expectation, variance and covariance, central limit theorem. Markov inequality, Chebyshev inequality, law of large numbers, Markov chains, simulation, the PageRank algorithm, populations and sampling, sample mean, standard error, maximum likelihood estimation, Bayes estimation, hypothesis testing, confidence intervals, linear regression, principal component analysis, classification, and decision trees. Credit is not given toward graduation for: Credit is not given for both CS 361 and ECE 313. Prerequisite: MATH 220 or MATH 221. Credit or concurrent registration in one of MATH 225, MATH 227, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210."`
- [E06cf53099007cdca] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "361"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Eb631a64d325d852d] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Probability & Statistics for Computer Science"`
- [Efa60d3085a07b1ec] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS361/2026-fa>`
- [E0fb03d364f5d6656] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS361>`
- [Ea03f4cd1405a9b7d] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [E0cb7d0f5893ac89c] `<https://example.org/uiuc-course-advisor/resource/course/CS361> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E70d71e71c1f74333] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E2ab18d14f7346ef6] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 361"`
- [E801b9de9c509820f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1>`
- [Ef4e7b118df8c0235] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [Edcf59de72c44dc40] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 220 or MATH 221."`
- [Eaf5c2b10e003f847] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E4e44922c300f7480] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 361 prerequisite option 1"`
- [E200adf012eb481a8] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1/condition/1>`
- [E4166f7ec0579edcb] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E3e4eea6ed478fcee] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 361 opt 1 cond 1: one of MATH 220, MATH 221"`
- [Ec5898127c18065a6] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E3a35ce6438f1096c] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH220>`
- [E5f85c5f6ebd5a007] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH221>`
- [E125e1cfe7291a9f2] `<https://example.org/uiuc-course-advisor/resource/prereq/CS361/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 220 or MATH 221"`
- [E57732c4aef485c73] `<https://example.org/uiuc-course-advisor/resource/offering/CS361/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E840f2e61705c2e9a] `<https://example.org/uiuc-course-advisor/resource/offering/CS361/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 361 (Fall 2026)"`
- [E77cdc5dd425f626c] `<https://example.org/uiuc-course-advisor/resource/offering/CS361/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E0b9fc42488136d24] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E4e1cc7d3973b51ac] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <http://www.w3.org/2000/01/rdf-schema#label> "CS 374 Introduction to Algorithms & Models of Computation"`
- [E31aa30113e75ecc3] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 374"`
- [E8e5b2b66837b9579] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Edc085217a30d5eb9] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E531b03bd3110cc28] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Analysis of algorithms, major paradigms of algorithm design including recursive algorithms, divide-and-conquer algorithms, dynamic programming, greedy algorithms, and graph algorithms. Formal models of computation including finite automata and Turing machines. Limitations of computation arising from fundamental notions of algorithm and from complexity-theoretic constraints. Reductions, undecidability and NP-completeness. Same as ECE 374. Prerequisite: One of CS 173, MATH 213; CS 225."`
- [Ecec1cf5e41926d82] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "374"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ecae788f731685b4c] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Introduction to Algorithms & Models of Computation"`
- [E73062c5c72d37c46] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#crossListedWith> <https://example.org/uiuc-course-advisor/resource/course/ECE374>`
- [E729430ed50cc6de7] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS374/2026-fa>`
- [Ee7f1b18338eb9626] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS374>`
- [E96b3f9ab89a8616f] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [E50b1915db37848ac] `<https://example.org/uiuc-course-advisor/resource/course/CS374> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Ef330e500a98375b4] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Eb5831c21144de699] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 374"`
- [Edf50a27dce768471] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1>`
- [Ea9711505a486aa15] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [Ee48b5c5f465f2deb] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "One of CS 173, MATH 213; CS 225."`
- [E7f49cc8936a9b24a] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E76f00b2ceb28a805] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 374 prerequisite option 1"`
- [Ee99dbc11e463e398] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/1>`
- [E3d6d5050ff2e400e] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/2>`
- [Ea585739e03a9afc3] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E01a2cd0d5d5e4f22] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 374 opt 1 cond 1: one of CS 173, MATH 213"`
- [E7ade8db272966243] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E3c351877cce09436] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS173>`
- [Ed0ec6c95dffe0556] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH213>`
- [Efafb96bc45e6ab73] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "One of CS 173, MATH 213"`
- [E8ed185010f3cefd7] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [Ee3d9f1f23b65fbbe] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "CS 374 opt 1 cond 2: requires CS 225"`
- [E257d43c26a55fc69] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E45a49cab87ac18b4] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "CS 225"`
- [E29fae9c25211764d] `<https://example.org/uiuc-course-advisor/resource/prereq/CS374/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/CS225>`
- [Ecd67e18ee116c8e5] `<https://example.org/uiuc-course-advisor/resource/offering/CS374/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Eb1738872e510cde9] `<https://example.org/uiuc-course-advisor/resource/offering/CS374/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 374 (Fall 2026)"`
- [Ed0b7d3e7685be874] `<https://example.org/uiuc-course-advisor/resource/offering/CS374/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E130b862e9062c10a] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ef40cc87a6f5d8afa] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <http://www.w3.org/2000/01/rdf-schema#label> "CS 413 Intro to Combinatorics"`
- [E4d4e4e4e296a3304] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 413"`
- [E3ecce89e68285b60] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E7c2ddea903286aaa] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E82b6ce6c45ac6825] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Same as MATH 413. See MATH 413."`
- [E5abb061f8ff796b2] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "413"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E233f6d347d6c0c45] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Intro to Combinatorics"`
- [E605a912267d8fa9a] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#crossListedWith> <https://example.org/uiuc-course-advisor/resource/course/MATH413>`
- [E84b97eec24dbc4e1] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS413/2026-fa>`
- [Ed3cf6979f7f6302a] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [E8d570ffef8b072e0] `<https://example.org/uiuc-course-advisor/resource/course/CS413> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E05391c301ea260eb] `<https://example.org/uiuc-course-advisor/resource/offering/CS413/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E39ca1122444af8a1] `<https://example.org/uiuc-course-advisor/resource/offering/CS413/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 413 (Fall 2026)"`
- [E49244a5792e582c1] `<https://example.org/uiuc-course-advisor/resource/offering/CS413/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Ec372689eb8e90dbb] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ee318faed9d0b8836] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <http://www.w3.org/2000/01/rdf-schema#label> "CS 440 Artificial Intelligence"`
- [E3a7ffa79660a2151] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#courseCode> "CS 440"`
- [E97821e4074364846] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E326020cfadc8077a] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E128e89990273d526] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Major topics in and directions of research in artificial intelligence: basic problem solving techniques, knowledge representation and computer inference, machine learning, natural language understanding, computer vision, robotics, and societal impacts. Same as ECE 448. 3 undergraduate hours. 3 or 4 graduate hours. Prerequisite: CS 225; one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310."`
- [Ebc5c4cd7149b175a] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "440"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E3aa1bcf111bc2a58] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Artificial Intelligence"`
- [Ebe9e1c2e2535d332] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#crossListedWith> <https://example.org/uiuc-course-advisor/resource/course/ECE448>`
- [E2536e3ae4b5b08c6] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/CS440/2026-fa>`
- [E50dbfcbb5c2ca36b] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/CS440>`
- [Ebdd281643c1c3841] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/CS>`
- [Eedfc588f17948136] `<https://example.org/uiuc-course-advisor/resource/course/CS440> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Ed3e665f3cd57f529] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Eb81d26c34267340e] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of CS 440"`
- [E8836b1904d1d5679] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1>`
- [Ef685f720a2ea8f01] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [Ef9b0c62d0a0226cb] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "CS 225; one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310."`
- [E6cc039efc401625f] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Ed56b050710cc3d7b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 440 prerequisite option 1"`
- [Ec35e4b8a0ba2a77b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/1>`
- [Ebfe3fef80baf123d] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2>`
- [E9e7c544ee1075a91] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E1812e5806c10fbd0] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "CS 440 opt 1 cond 1: requires CS 225"`
- [E101a28db73928f0c] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E83342a37c4a3ae9b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "CS 225"`
- [Efda85bffbfb9ce07] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/CS225>`
- [E3610f571522e3b64] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E7f46ea1e791bf839] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "CS 440 opt 1 cond 2: one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400, BIOE 310"`
- [E0aa17791e88aa2f9] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E157f6472f23c255b] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/BIOE310>`
- [Edfc47be7f9450ee4] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS361>`
- [Eab1c428abd4c81c8] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/ECE313>`
- [E58faaae543217795] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH362>`
- [E7ca8e17ea8701b7a] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH461>`
- [E91cadeaed3d0b420] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH463>`
- [Ea0efb1d6f7177725] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/STAT361>`
- [E60a66064ab63f423] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/STAT400>`
- [E7030277cf5b65d5d] `<https://example.org/uiuc-course-advisor/resource/prereq/CS440/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310"`
- [E44b35942c9e98ca4] `<https://example.org/uiuc-course-advisor/resource/offering/CS440/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Eb15ad51d2048b818] `<https://example.org/uiuc-course-advisor/resource/offering/CS440/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "CS 440 (Fall 2026)"`
- [Ed21157d45bdad97d] `<https://example.org/uiuc-course-advisor/resource/offering/CS440/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E716ef4d0dd04d82d] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ee2ba542e6c85445b] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 120 Introduction to Computing"`
- [E0ff02c71102d4fb0] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#courseCode> "ECE 120"`
- [E17c8da6d3cc4e1ff] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ecf85d96e1104771c] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E7624280772f7e45a] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Introduction to digital logic, computer systems, and computer languages. Topics include representation of information, combinational and sequential logic analysis and design, finite state machines, the von Neumann model, basic computer organization, and machine language programming. Laboratory assignments provide hands-on experience with design, simulation, implementation, and programming of digital systems. Prerequisite: Restricted to Computer Engineering or Electrical Engineering majors or transfer students with ECE Department consent."`
- [E2a94270240da16ab] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "120"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ed15afafed09f321b] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Introduction to Computing"`
- [E6272f94ccb46e668] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/ECE120/2026-fa>`
- [Eb69d1151e2faa663] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/ECE120>`
- [Ee283a0d9f2e384c2] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/ECE>`
- [Ebd89ac0082c2616e] `<https://example.org/uiuc-course-advisor/resource/course/ECE120> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Eac97d6a5a605d347] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Efb90da48ec008217] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of ECE 120"`
- [Ea3acf276097b8262] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1>`
- [E16c6ca85b9b4a509] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [E62944d624cf1253b] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "Restricted to Computer Engineering or Electrical Engineering majors or transfer students with ECE Department consent."`
- [E6c015a6c1cfe5c22] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E6446da422ba11dbe] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 120 prerequisite option 1"`
- [Ef89347a6b7d0fb92] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1/condition/1>`
- [E5227be0472e4e3fe] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#OtherCondition>`
- [Eaf83abc67acfecc2] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 120 opt 1 cond 1: needs review: Restricted to Computer Engineering or Electrical Engineering"`
- [Ef1bce7d851015744] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE120/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "Restricted to Computer Engineering or Electrical Engineering majors or transfer students with ECE Department consent"`
- [E6e3aa78d35c7096e] `<https://example.org/uiuc-course-advisor/resource/offering/ECE120/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Ed672b267b69b2142] `<https://example.org/uiuc-course-advisor/resource/offering/ECE120/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 120 (Fall 2026)"`
- [E9089d3ce07b20530] `<https://example.org/uiuc-course-advisor/resource/offering/ECE120/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Efc69deee5422a9b6] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E06cf4e0f3824e354] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 220 Computer Systems & Programming"`
- [E376b88076fba12a1] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#courseCode> "ECE 220"`
- [E8d173a7747b29238] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E5f739b09a26656d1] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E0be9dda355fc58c7] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Advanced use of LC-3 assembly language for I/O and function calling convention. C programming, covering basic programming concepts, functions, arrays, pointers, I/O, recursion, simple data structures, linked lists, dynamic memory management, and basic algorithms. Information hiding and object-oriented design as commonly implemented in modern software and computer systems programming. Prerequisite: ECE 120. Restricted to Computer Engineering or Electrical Engineering majors or transfer students with ECE Department consent."`
- [E7f693e955251a57f] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "220"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E9825780048732656] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Computer Systems & Programming"`
- [E51e00e4d383dc3d5] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/ECE220/2026-fa>`
- [E16a3c55799f70355] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/ECE220>`
- [Eb039beee7cbb7f78] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/ECE>`
- [Ebee1cb38443e33c5] `<https://example.org/uiuc-course-advisor/resource/course/ECE220> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E64cfb00fbd995e5f] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E3920e5d3062bd6d5] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of ECE 220"`
- [E885a67b738448652] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1>`
- [E734f3910fc0fee09] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E8d30b57e9c065952] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "ECE 120."`
- [E994fa6f580bf7a86] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E7b63633dbedcb2bc] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 220 prerequisite option 1"`
- [E1b157121d40be189] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1/condition/1>`
- [E00cffd8e13edcfe6] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E6b2023c58aa9f5f9] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 220 opt 1 cond 1: requires ECE 120"`
- [E8e686ce8cbfc9ae7] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E6d05b0cfeb49f74c] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "ECE 120"`
- [Ebaeff5b90127a85c] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE220/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/ECE120>`
- [E70b3b5f3097d6645] `<https://example.org/uiuc-course-advisor/resource/offering/ECE220/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E40d8510f6045f0b6] `<https://example.org/uiuc-course-advisor/resource/offering/ECE220/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 220 (Fall 2026)"`
- [Ed88f39fd4c211ee4] `<https://example.org/uiuc-course-advisor/resource/offering/ECE220/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E7f91bfc5f149ea30] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ec489d29f287a0833] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 313 Probability with Engrg Applic"`
- [Ea10e421cf60501df] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#courseCode> "ECE 313"`
- [Ec45a14d6cf23fa77] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E1b75ffad1cc4db89] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ef2b6e555544a24fb] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Probability theory with applications to engineering problems such as the reliability of circuits and systems to statistical methods for hypothesis testing, decision making under uncertainty, and parameter estimation. Same as MATH 362. Credit is not given for both ECE 313 and MATH 461. Prerequisite: MATH 257 or MATH 416."`
- [Eb22bf925d893e21f] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "313"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E1b85b13d35e9f1ba] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Probability with Engrg Applic"`
- [E602c12506db0f74e] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#crossListedWith> <https://example.org/uiuc-course-advisor/resource/course/MATH362>`
- [Ebc7636c82a9f7325] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/ECE313/2026-fa>`
- [E5d623d60ccc2a4c1] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/ECE313>`
- [E2545a84a4a2f1a54] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/ECE>`
- [Ed6280d8a852d7d94] `<https://example.org/uiuc-course-advisor/resource/course/ECE313> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E2d66b308dda04b1d] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Eb9174d6ea77f995a] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of ECE 313"`
- [Eaa607095f7753e2a] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1>`
- [E76861d8ba1538508] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E2694c10b56efe018] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 257 or MATH 416."`
- [Eb72264c14225b51c] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E384cd181c8224a54] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 313 prerequisite option 1"`
- [E16c3419e6da7276b] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1/condition/1>`
- [E0f11a6aa9dad8971] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E82cb96f00c40f20c] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 313 opt 1 cond 1: one of MATH 257, MATH 416"`
- [E58ca10c4a47c0849] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ebbdd841b9c9e5d30] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH257>`
- [E945fd4e44a920249] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH416>`
- [E125c87851da4afe2] `<https://example.org/uiuc-course-advisor/resource/prereq/ECE313/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 257 or MATH 416"`
- [Ef12fde077f5f116c] `<https://example.org/uiuc-course-advisor/resource/offering/ECE313/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E0733a1c72ef6b87e] `<https://example.org/uiuc-course-advisor/resource/offering/ECE313/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "ECE 313 (Fall 2026)"`
- [Ecb9921c83f296252] `<https://example.org/uiuc-course-advisor/resource/offering/ECE313/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E50a1044ef2946450] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ef2977e009bbd519d] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 112 Algebra"`
- [E02dece5e92358bb3] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 112"`
- [Edac4273721ea3630] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Efa561e59af2c4965] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E427e8342581cba07] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Rapid review of basic techniques of factoring, rational expressions, equations and inequalities; functions and graphs; exponential and logarithm functions; systems of equations; matrices and determinants; polynomials; and the binomial theorem. Prerequisite: 1.5 units of high school algebra and 1 unit of high school geometry."`
- [Eef72816f9e8702cc] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "112"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E7cc7878b12858d13] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Algebra"`
- [Eb168c912ee4c6e65] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH112/2026-fa>`
- [E0a452dc17866cc47] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH112>`
- [Eacd6fc8860c8d7fc] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E83b45f03172941fa] `<https://example.org/uiuc-course-advisor/resource/course/MATH112> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E3e110a826120843a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ed0293f7e5824bdcd] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 112"`
- [Ec980dbef44e9bafe] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1>`
- [Ef66e5dfbc40d6a86] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [Ebe9242cbcfcbbaef] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "1.5 units of high school algebra and 1 unit of high school geometry."`
- [Ed88ce2235419660e] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E14be3eb5975b3e97] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 112 prerequisite option 1"`
- [E2578b790df5a2459] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1/condition/1>`
- [E4424bf61f28a1896] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#OtherCondition>`
- [E1294874fbc8f5748] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 112 opt 1 cond 1: needs review: 1.5 units of high school algebra and 1 unit of high school g"`
- [E05d73468853a45e1] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH112/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "1.5 units of high school algebra and 1 unit of high school geometry"`
- [E04c6df2a499c3add] `<https://example.org/uiuc-course-advisor/resource/offering/MATH112/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E05b3238643618242] `<https://example.org/uiuc-course-advisor/resource/offering/MATH112/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 112 (Fall 2026)"`
- [E6ffe741e6085936f] `<https://example.org/uiuc-course-advisor/resource/offering/MATH112/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E9737ba2a8a9d4608] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E8340e83cebe315a1] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 115 Preparation for Calculus"`
- [E839a11054041371d] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 115"`
- [Eb3a168849401136a] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ee95aa7f979ec452f] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E1687deb6173a7024] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Reviews trigonometric, rational, exponential, and logarithmic functions; provides a full treatment of limits, definition of derivative, and an introduction to finding area under a curve. Intended for students who need preparation for MATH 220, either because they lack the content background or because they are not prepared for the rigor of a university calculus course. Credit is not given toward graduation for: Credit is not given for both MATH 115 and either MATH 014 or MATH 114. Credit is not given for MATH 115 if credit for either MATH 220 or MATH 221 has been earned. Prerequisite: MATH 112."`
- [E014f54ca2c7ff085] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "115"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E01c020e57564c2fd] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Preparation for Calculus"`
- [Eb847c0056e01f4ad] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning I course."`
- [E958ac9435e7879fa] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH115/2026-fa>`
- [E79c137ae20c36eae] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH115>`
- [Eaee8bf46dfe779b1] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E26366efe712aeedc] `<https://example.org/uiuc-course-advisor/resource/course/MATH115> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Edd36bb6ace9f77f3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E2d963620869a1585] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 115"`
- [E3631fb97862f72ea] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1>`
- [E1f0f0fc3db6d65d2] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E00cf13a2a6891cab] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 112."`
- [Edcb4a66ab708191c] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E72e8ececba6ea733] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 115 prerequisite option 1"`
- [E232c32275556d8ed] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1/condition/1>`
- [E85c0326488bd6339] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [Ec0c1ff6f7dce492d] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 115 opt 1 cond 1: requires MATH 112"`
- [E3792f2ee8b9123e3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ee22262fea54a7bc5] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 112"`
- [E109b9fc54b7e8d94] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH115/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH112>`
- [Ee82a7ab0510c0d5a] `<https://example.org/uiuc-course-advisor/resource/offering/MATH115/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E23cb40759144652a] `<https://example.org/uiuc-course-advisor/resource/offering/MATH115/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 115 (Fall 2026)"`
- [E6ac874586ab65940] `<https://example.org/uiuc-course-advisor/resource/offering/MATH115/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E7500ee8fb1ae5f17] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ee0bcdf06c1f180db] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 213 Basic Discrete Mathematics"`
- [E64cb510777521f50] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 213"`
- [E6492d98a40914454] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E9849df038d8673c0] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Eb659eb8eb735d5c4] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "[IAI Code: M1905] Beginning course on discrete mathematics, including sets and relations, functions, basic counting techniques, recurrence relations, graphs and trees, and matrix algebra; emphasis throughout is on algorithms and their efficacy. Credit is not given toward graduation for: Credit is not given for both MATH 213 and CS 173. Prerequisite: MATH 220 or MATH 221, or equivalent."`
- [E205a453cd71cf701] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "213"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E7f1fe9ffcd96b571] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Basic Discrete Mathematics"`
- [E2becc3b104f4cb6d] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning II course."`
- [E932db0e3be64d911] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH213/2026-fa>`
- [Ef19b48296c9c4095] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH213>`
- [E67387cad92d89b6a] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [Ece90a6db63811947] `<https://example.org/uiuc-course-advisor/resource/course/MATH213> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E695010677539f815] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ee637b497dbed94dd] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 213"`
- [Ed96833ac125efcba] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1>`
- [Ee72a54f7be4b6afa] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [E4dd34f12772e8889] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 220 or MATH 221, or equivalent."`
- [E2bc36c400ee58188] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Ed822b83eeb2b6e3f] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 213 prerequisite option 1"`
- [Ed9105c8c4a42950a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1/condition/1>`
- [E937d43a76ddc6639] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E71a3939833141319] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 213 opt 1 cond 1: one of MATH 220, MATH 221"`
- [Ecce7cca47a920804] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E16b898dada5d48e3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH220>`
- [E805a42188a08c1b0] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH221>`
- [Ec08105b9cbf34156] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH213/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 220 or MATH 221, or equivalent"`
- [E769d6da5d627c2eb] `<https://example.org/uiuc-course-advisor/resource/offering/MATH213/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Ed3d55f79f0fc0cd1] `<https://example.org/uiuc-course-advisor/resource/offering/MATH213/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 213 (Fall 2026)"`
- [E6d6c859b96fb2683] `<https://example.org/uiuc-course-advisor/resource/offering/MATH213/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Eb709dce8fb5627cb] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Eaf845a024e2cecf3] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 220 Calculus"`
- [E8db7d38e4de2ffab] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 220"`
- [E94862b38d5ab6319] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "5.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E5e2165954d296a87] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "5.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ecdcda6a69d100d9f] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "[IAI Code: M1900-1 and MTH901] First course in calculus and analytic geometry; basic techniques of differentiation and integration with applications including curve sketching; antidifferentation, the Riemann integral, fundamental theorem, exponential and trigonometric functions. Credit is not given toward graduation for: Credit is not given for both MATH 220 and either MATH 221 or MATH 234. Prerequisite: An adequate ALEKS placement score as described at http://math.illinois.edu/ALEKS/, demonstrating knowledge of topics of MATH 115. Students with previous calculus experience should consider MATH 221."`
- [E204c9a442dfdf77d] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "220"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ea63a22b470d67da1] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Calculus"`
- [E229c6274cad43bef] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning I course."`
- [E3b2a70a0ae7125d3] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH220/2026-fa>`
- [E54d7f0d3ad250cea] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH220>`
- [Ea8210524573b3b63] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E9003fdaae0a37855] `<https://example.org/uiuc-course-advisor/resource/course/MATH220> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E2dc5b5641f252b59] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E5398122eab5097a7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 220"`
- [E338bff734fa11ad7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1>`
- [E405d3d1dd6f8c461] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E58fa009b26eeca52] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "An adequate ALEKS placement score as described at http://math.illinois.edu/ALEKS/, demonstrating knowledge of topics of MATH 115."`
- [Ebdf161d8c432ce0f] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E8a3a276c1b9045ec] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 220 prerequisite option 1"`
- [E5509b9e310adafc1] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1/condition/1>`
- [E652cbaa6e208c9e6] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E47565bf62c4a6450] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 220 opt 1 cond 1: requires MATH 115"`
- [E8ac99f8935040c44] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E3695de1c14c7a1f2] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "An adequate ALEKS placement score as described at http://math.illinois.edu/ALEKS/, demonstrating knowledge of topics of MATH 115"`
- [Ef284a7015791734f] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH220/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH115>`
- [E6b1c790b273e4bb1] `<https://example.org/uiuc-course-advisor/resource/offering/MATH220/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Ecfaca1123791350a] `<https://example.org/uiuc-course-advisor/resource/offering/MATH220/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 220 (Fall 2026)"`
- [E7a312a775858f440] `<https://example.org/uiuc-course-advisor/resource/offering/MATH220/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Efd05322843e87974] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E03ab752866a91d77] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 221 Calculus I"`
- [E3a6d81152bbe4148] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 221"`
- [E7ba9e1c9913e4208] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E0ed28cddec56db8f] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E98486d6a2f130a49] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "First course in calculus and analytic geometry for students with some calculus background; basic techniques of differentiation and integration with applications including curve sketching; antidifferentation, the Riemann integral, fundamental theorem, exponential and trigonometric functions. Credit is not given for both MATH 221 and either MATH 220 or MATH 234. Prerequisite: An adequate ALEKS placement score as described at http://math.illinois.edu/ALEKS/ and either one year of high school calculus or a minimum score of 2 on the AB Calculus AP exam."`
- [E881d1a926e702a1a] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "221"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E1ed92b205b0a4b48] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Calculus I"`
- [E284cffad0684663a] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning I course."`
- [E5e78994a83100fe9] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH221/2026-fa>`
- [E3c5a74f9a95846b7] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH221>`
- [Ea5f7b6d76cc6a84d] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E26945858ba71ef92] `<https://example.org/uiuc-course-advisor/resource/course/MATH221> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Eddf2700c012ea2ff] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E9436941afe461f56] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 221"`
- [E57880cec8a484512] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1>`
- [Eae6b35b720d5bdcc] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [E5b64e575df39697e] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "An adequate ALEKS placement score as described at http://math.illinois.edu/ALEKS/ and either one year of high school calculus or a minimum score of 2 on the AB Calculus AP exam."`
- [E8fbdcc80d1075450] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E1495a7b63a2374f0] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 221 prerequisite option 1"`
- [Eae8301127e9873a7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/1>`
- [E13441e37bcf1b871] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/2>`
- [Ef161caa6d83b74eb] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#OtherCondition>`
- [Eadf4f976ebc313f3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 221 opt 1 cond 1: needs review: An adequate ALEKS placement score as described at http://mat"`
- [Ed805afd8d0ddbc94] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "An adequate ALEKS placement score as described at http://math.illinois.edu/ALEKS/"`
- [Ee58237836bdd55ed] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#OtherCondition>`
- [E468476d279c7d85b] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 221 opt 1 cond 2: needs review: either one year of high school calculus or a minimum score o"`
- [E59de684d9e5400f5] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH221/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "either one year of high school calculus or a minimum score of 2 on the AB Calculus AP exam"`
- [Ef6ecafd03fc6f5dc] `<https://example.org/uiuc-course-advisor/resource/offering/MATH221/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E868a9eebdcae9a39] `<https://example.org/uiuc-course-advisor/resource/offering/MATH221/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 221 (Fall 2026)"`
- [Eefec4ab0bfdf9fb8] `<https://example.org/uiuc-course-advisor/resource/offering/MATH221/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E66db1680efb49610] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E271beca1fd067cac] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 231 Calculus II"`
- [E3bd1e0028e2f963e] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 231"`
- [E3581bf9851cbf8fe] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ee0ec18b5c9f68ad1] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Eba2ae1b18ad8c8c6] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "[IAI Code: M1900-2 and MTH902] Second course in calculus and analytic geometry: techniques of integration, conic sections, polar coordinates, and infinite series. Prerequisite: MATH 220 or MATH 221."`
- [E85b495ced84191c6] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "231"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ea21eec98a236190a] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Calculus II"`
- [Eec4dccbc372b9106] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning I course."`
- [E605d66abd2d6487d] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH231/2026-fa>`
- [E8d1ed41b317775fd] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH231>`
- [E88da28499a7333b8] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [Eb81ecfe3dd0ce945] `<https://example.org/uiuc-course-advisor/resource/course/MATH231> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E62b21eaf9d6bfb22] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ee84beb174227d3d1] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 231"`
- [E4c093724ae1ea6dd] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1>`
- [E4d86ab19287baf4a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E60a09efd383d179b] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 220 or MATH 221."`
- [E480c70ef9dce0d10] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E20d7770e95b6760c] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 231 prerequisite option 1"`
- [E5ca017f753898cdd] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1/condition/1>`
- [E407d21b7e9f2bd65] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [Eed1d868d32f447f3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 231 opt 1 cond 1: one of MATH 220, MATH 221"`
- [E80cfdf03e5581b0a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Eedce71f5f38f07ca] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH220>`
- [E54fa0042d02461b2] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH221>`
- [E1f5cc97e4a3e3495] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH231/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 220 or MATH 221"`
- [E34e11ee397eda0d2] `<https://example.org/uiuc-course-advisor/resource/offering/MATH231/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E267eb3d6e0910dc8] `<https://example.org/uiuc-course-advisor/resource/offering/MATH231/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 231 (Fall 2026)"`
- [Ee8ebae3e886992bd] `<https://example.org/uiuc-course-advisor/resource/offering/MATH231/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Ed4b0b309c7931cff] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E15fe2a75f4234cc2] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 241 Calculus III"`
- [E985dc3499ee666e4] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 241"`
- [Ec2dea0910b62232f] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ee394b955f4f52095] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E552f599e375f1ca6] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "[IAI Code: M1900-3 and MTH903] Third course in calculus and analytic geometry including vector analysis: Euclidean space, partial differentiation, multiple integrals, line integrals and surface integrals, the integral theorems of vector calculus. Credit is not given toward graduation for: Credit is not given for both MATH 241 and MATH 292. Prerequisite: MATH 231."`
- [E511a68c2021066bf] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "241"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E537273b270d9b188] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Calculus III"`
- [E832f45aeb9f30dfd] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#hasDegreeAttribute> "Quantitative Reasoning II course."`
- [E888b6aa944af5481] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH241/2026-fa>`
- [Efcbbf039fb959683] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH241>`
- [Ee5ca7200d4584c41] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [Eb27e9754e784975a] `<https://example.org/uiuc-course-advisor/resource/course/MATH241> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E6531146446b2fee9] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ec06984c29c6352da] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 241"`
- [Eb53b5b680af53cc7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1>`
- [E797457228975a075] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E1b022cb86e1ff08d] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 231."`
- [E2839652c0efbb44d] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E2eb74a1fd4e7202b] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 241 prerequisite option 1"`
- [E9d2756d6fc0d2595] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1/condition/1>`
- [E258c98da333dff0e] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E3aeb6db6d370cdb6] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 241 opt 1 cond 1: requires MATH 231"`
- [Ec0ed3c391e116427] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ea8348728c389bddd] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 231"`
- [E20c14e72738ff555] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH241/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH231>`
- [Ee5510f9ca74a2228] `<https://example.org/uiuc-course-advisor/resource/offering/MATH241/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E2f6018f5caf13520] `<https://example.org/uiuc-course-advisor/resource/offering/MATH241/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 241 (Fall 2026)"`
- [E8f48da112d93c30d] `<https://example.org/uiuc-course-advisor/resource/offering/MATH241/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E9a968da90e775725] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ef2857f69091eedb7] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 257 Linear Algebra with Computational Applications"`
- [E6a2caa167cd3c405] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 257"`
- [Ece542ac2128552f5] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ed9296365f123a99d] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E2d2acdf7f71bf4e4] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Introductory course incorporating linear algebra concepts with computational tools, with real world applications to science, engineering and data science. Topics include linear equations, matrix operations, vector spaces, linear transformations, eigenvalues, eigenvectors, inner products and norms, orthogonality, linear regression, equilibrium, linear dynamical systems and the singular value decomposition. Credit is not given for both MATH 257 and any of MATH 125, MATH 225, MATH 227, MATH 415 or ASRM 406. Prerequisite: MATH 220 or MATH 221; CS 101 or equivalent programming experience."`
- [Eff910eff3110bf32] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "257"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ef5acd29dfdb69afb] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Linear Algebra with Computational Applications"`
- [E99671bf361e55010] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH257/2026-fa>`
- [Ec85536ccd0f65eab] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH257>`
- [E4e8269f9ae84d7d5] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E8ac6a68ec246598b] `<https://example.org/uiuc-course-advisor/resource/course/MATH257> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Ee760772976ad88fb] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Eaa092618e10c5312] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 257"`
- [Ec23fb23c89b9631c] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1>`
- [Ecb03b1f891f32d82] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [E7533dcd5d3145b68] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 220 or MATH 221; CS 101 or equivalent programming experience."`
- [E0c2c0d4cd30581f7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E5e18bc0284be8c1e] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 257 prerequisite option 1"`
- [E7e215d54ee0f4194] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/1>`
- [E479dac1a9a982267] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/2>`
- [Ebcb95b2340ed97e8] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E2c94439d672c97f7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 257 opt 1 cond 1: one of MATH 220, MATH 221"`
- [E2cff9185db2f1325] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ed0df979e34b6ac7a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH220>`
- [E00e62f02cec86ba4] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH221>`
- [E1427604ac114c967] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 220 or MATH 221"`
- [E1d2d6c09f59509d0] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E695ea87ca5fba723] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 257 opt 1 cond 2: requires CS 101"`
- [E1dca545b958fa791] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ea1a66fac5582a40d] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "CS 101 or equivalent programming experience"`
- [E5d48b809f21155d5] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH257/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/CS101>`
- [Ec241ea5c115369e0] `<https://example.org/uiuc-course-advisor/resource/offering/MATH257/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Ef62bf87ee5170d35] `<https://example.org/uiuc-course-advisor/resource/offering/MATH257/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 257 (Fall 2026)"`
- [Ec5116eaa40e6bc21] `<https://example.org/uiuc-course-advisor/resource/offering/MATH257/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E6aca12869552cf69] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E7c0f285a7b0b5e2b] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 314 Introduction to Higher Mathematics"`
- [E37bb4ae5d93346af] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 314"`
- [Eb84cba1fb49f169f] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E88d5a5b841d1e4f6] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E2ca3951ca1ea77c5] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Skills and techniques necessary to identify valid mathematical proofs and to produce valid mathematical proofs. Students will also be exposed to beginning ideas in several advanced mathematical topics, including modular arithmetic, group theory, combinatorial reasoning, solving equations, epsilon-delta arguments, and limits. This course is particularly focused on students who have no prior proof-writing experience; students with prior proof-writing experience, or with less need for training in writing proofs, should consider MATH 347 instead. Credit is not given toward graduation for both MATH 314 and MATH 347. Prerequisite: MATH 241."`
- [Ee4ab46712dd91de6] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "314"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ef9b159a4f575fb6a] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Introduction to Higher Mathematics"`
- [E3ce803c5891f4b8e] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH314/2026-fa>`
- [Ebad96c1fe8e1c05a] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH314>`
- [Eb5c39c2c7ad7e8a8] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [Eae7bc9b5038b39f9] `<https://example.org/uiuc-course-advisor/resource/course/MATH314> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E98e0f2ffe4867232] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E28f1bee3e3f21e18] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 314"`
- [E49bf49e1c80091e1] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1>`
- [E2c6c8c9057325f36] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E5d912c24db42c7ef] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 241."`
- [E2f04e2a8c65bbe49] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E998ba94b5a1418d6] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 314 prerequisite option 1"`
- [E02bc398436cb6fa9] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1/condition/1>`
- [E1203071cfd8feb40] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E22d7ffa9c35b8be4] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 314 opt 1 cond 1: requires MATH 241"`
- [E6865922b03403b22] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E3fd606511b2ab0b8] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 241"`
- [Ef5b67bf9b5b2a949] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH314/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH241>`
- [E6d721ff69335385e] `<https://example.org/uiuc-course-advisor/resource/offering/MATH314/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Efe8ff8e69e127690] `<https://example.org/uiuc-course-advisor/resource/offering/MATH314/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 314 (Fall 2026)"`
- [Ec044eb77a274ebd9] `<https://example.org/uiuc-course-advisor/resource/offering/MATH314/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E83c4353350da13cc] `<https://example.org/uiuc-course-advisor/resource/course/MATH347> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [Ec54c28dfc9738116] `<https://example.org/uiuc-course-advisor/resource/course/MATH347> <http://www.w3.org/2000/01/rdf-schema#comment> "Referenced by a prerequisite, cross-listing or degree requirement but not present in the Fall 2026 catalog snapshot; only its code is known."`
- [Eba13b57d3e502073] `<https://example.org/uiuc-course-advisor/resource/course/MATH347> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 347"`
- [Eee6b1402f2493dfe] `<https://example.org/uiuc-course-advisor/resource/course/MATH347> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 347"`
- [Eaa7884bbf025b6dd] `<https://example.org/uiuc-course-advisor/resource/course/MATH347> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "347"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ea6c57b66fbe58856] `<https://example.org/uiuc-course-advisor/resource/course/MATH347> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E464ae039f994cd83] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E3c28947a53dc04fa] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 412 Graph Theory"`
- [Edf95168260b04925] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 412"`
- [E81ad97909dff70f7] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ee8635db6f9015aea] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E698566e66482c548] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Examines basic concepts and applications of graph theory, where graph refers to a set of vertices and edges that join some pairs of vertices; topics include subgraphs, connectivity, trees, cycles, vertex and edge coloring, planar graphs and their colorings. Draws applications from computer science, operations research, chemistry, the social sciences, and other branches of mathematics, but emphasis is placed on theoretical aspects of graphs. 3 or 4 undergraduate hours. 3 or 4 graduate hours. 4 hours of credit requires approval of the instructor and department with completion of additional work of substance. Prerequisite: MATH 314 or MATH 347 or equivalent experience or CS 374."`
- [E2073d0992bfd0f01] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "412"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E51aaf93f1ca74a45] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Graph Theory"`
- [Ec2c3ca8705fd864e] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH412/2026-fa>`
- [E655410f704bfb245] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH412>`
- [Ea969a4ec3b2a1046] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E9c6239587d9268d9] `<https://example.org/uiuc-course-advisor/resource/course/MATH412> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E9775b13c86f76e38] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Eb3fd8129eeb4f2f9] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 412"`
- [E8f70e432225e204f] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1>`
- [Edcf7d7faad39d1e4] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [E10797a6ce00cb703] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 314 or MATH 347 or equivalent experience or CS 374."`
- [E8a3e385a880f28eb] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E1a0e59a7602b32e5] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 412 prerequisite option 1"`
- [E8a487075f7543ca3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1>`
- [E0ff737bbf9debc06] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [Eb2849b7a8aded687] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 412 opt 1 cond 1: one of MATH 314, MATH 347, CS 374"`
- [E0814189d102eb43a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E955432245ed3b037] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/CS374>`
- [E46a55b6c217a8ecc] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH314>`
- [Ecefb81a178d2d73a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH347>`
- [E26185836dc9f8074] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH412/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 314 or MATH 347 or equivalent experience or CS 374"`
- [Ee6ee7061db6af776] `<https://example.org/uiuc-course-advisor/resource/offering/MATH412/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E97f5f44ff213718a] `<https://example.org/uiuc-course-advisor/resource/offering/MATH412/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 412 (Fall 2026)"`
- [E30d609cc3b113eef] `<https://example.org/uiuc-course-advisor/resource/offering/MATH412/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E266e26ee61151843] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E5dd4c21f3c9c6eda] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 413 Intro to Combinatorics"`
- [E3759f90e8d10c8fd] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 413"`
- [E0be5abb330d90a84] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E4aad3f56fb2831af] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [Ee66c0ff1730836e3] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Permutations and combinations, generating functions, recurrence relations, inclusion and exclusion, Polya's theory of counting, and block designs. Same as CS 413. 3 undergraduate hours. 3 or 4 graduate hours. 4 hours of credit requires approval of the instructor and completion of additional work of substance. Prerequisite: MATH 314 or MATH 347 or equivalent experience."`
- [E85857b40a754f550] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "413"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E3e98971ec95486f2] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Intro to Combinatorics"`
- [E379d335f18f87a79] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#crossListedWith> <https://example.org/uiuc-course-advisor/resource/course/CS413>`
- [Edf61a4156c5438fb] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH413/2026-fa>`
- [E73e3ab2082288405] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH413>`
- [E3ef408704e028a95] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [Eb40612f900f450f9] `<https://example.org/uiuc-course-advisor/resource/course/MATH413> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [Ec56de3951f0a23a4] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E283f27259d99a6f3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 413"`
- [Ed439774e6573b2bb] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1>`
- [E255026415034aee2] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [E63bcd40e943abd92] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 314 or MATH 347 or equivalent experience."`
- [Ed305b33d84c7dac3] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E5cdffee2b52a7bbd] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 413 prerequisite option 1"`
- [E069521a2a121f75f] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1/condition/1>`
- [E37b18e614e398b3a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [Ec4a3fe0b242ed4e8] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 413 opt 1 cond 1: one of MATH 314, MATH 347"`
- [E8c9cc28a485a5f52] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ee37ec70922c4580e] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH314>`
- [E2b1ff8509db27da7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH347>`
- [E1f026864b110f128] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH413/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 314 or MATH 347 or equivalent experience"`
- [E11d55fb9bb934e92] `<https://example.org/uiuc-course-advisor/resource/offering/MATH413/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E2facbc5719350449] `<https://example.org/uiuc-course-advisor/resource/offering/MATH413/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 413 (Fall 2026)"`
- [Eda633446b8b1bd7e] `<https://example.org/uiuc-course-advisor/resource/offering/MATH413/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [E4e2a98c920b1be73] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E0cc04aafda643a73] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 416 Abstract Linear Algebra"`
- [Edd1591f23c0828b5] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 416"`
- [E9358c5221628a8d5] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E76c13169867e33ce] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E82deace1100970f4] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Rigorous proof-oriented course in linear algebra. Topics include determinants, vector spaces over fields, linear transformations, inner product spaces, eigenvectors and eigenvalues, Hermitian matrices, Jordan Normal Form. 3 or 4 undergraduate hours. 3 or 4 graduate hours. Credit is not given for both MATH 416 and either ASRM 406 or MATH 415. 4 hours of credit requires approval of the instructor and department with completion of additional work of substance. Prerequisite: MATH 241; MATH 314 or MATH 347; or consent of instructor."`
- [E23a9a2f16b532aba] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "416"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [E2a697ce7e9797e46] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Abstract Linear Algebra"`
- [E8145ac659467f8ce] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH416/2026-fa>`
- [E61b7038ef5127064] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH416>`
- [Ecaa7fb2d625da8a5] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [E31264aa2b9ec6375] `<https://example.org/uiuc-course-advisor/resource/course/MATH416> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E2985f45f8f70a014] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E204f3bb6ffcd5180] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 416"`
- [Ef5c7d9160f6e6ea0] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1>`
- [E3b506d8597074bb4] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2>`
- [E3bdaa8579df6cc80] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E117187665a583461] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 241; MATH 314 or MATH 347; or consent of instructor."`
- [E5fa250fc8a56a67c] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E08fb458ce86bc876] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 416 prerequisite option 1"`
- [Ee92188212e8cf1d9] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/1>`
- [Ea747ae51ee5b338c] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/2>`
- [E314466bc36de2573] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E228033daa68629fc] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 416 opt 1 cond 1: requires MATH 241"`
- [Ea0e4760aa52cdefe] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Ef2ee3763484b6d1a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 241"`
- [E6974674cf7b3fabf] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH241>`
- [Ed3938c924be76da4] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseChoiceCondition>`
- [E1b1b7fb0e2054c74] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/2> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 416 opt 1 cond 2: one of MATH 314, MATH 347"`
- [E7a706a67b40291f9] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [Eff7bae08496cabed] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH314>`
- [E2f5dacac500e3c3a] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#alternativeCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH347>`
- [Ee6a438548d796f0e] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/1/condition/2> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 314 or MATH 347"`
- [E2f3290a160eeeca2] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Ea7a99b8751dc2040] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 416 prerequisite option 2"`
- [E8dafaafaeabff2e6] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2/condition/1>`
- [Eac84f26ac33003de] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#ConsentCondition>`
- [E33d5f5da5314a662] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 416 opt 2 cond 1: consent / approval"`
- [E462832cbfa99f9b2] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH416/option/2/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "consent of instructor"`
- [E6b27d6769d77b414] `<https://example.org/uiuc-course-advisor/resource/offering/MATH416/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [Eb996cc41af2b9ffa] `<https://example.org/uiuc-course-advisor/resource/offering/MATH416/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 416 (Fall 2026)"`
- [E433de9786210ce4f] `<https://example.org/uiuc-course-advisor/resource/offering/MATH416/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Eabb2bdd078bb36cc] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E986ea61236f982a6] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 461 Probability Theory"`
- [Eec8dbfccb20f2aff] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#courseCode> "MATH 461"`
- [E5b91c10094425695] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E605db42b8595e921] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "3.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E0bbea46ca156d97c] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Introduction to mathematical probability; includes the calculus of probability, combinatorial analysis, random variables, expectation, distribution functions, moment-generating functions, and central limit theorem. 3 or 4 undergraduate hours. 3 or 4 graduate hours. Credit is not given for both MATH 461 and either STAT 408 or ECE 313. 4 hours of credit requires approval of the instructor and department with completion of additional work of substance. Prerequisite: MATH 241 or equivalent."`
- [E4365caaa77ff6429] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "461"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Ee6544d195a33ad2c] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Probability Theory"`
- [E6cd85b1442e224d8] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/MATH461/2026-fa>`
- [Ebf59282a3c004c5a] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/MATH461>`
- [E15165c00dcf6c5a4] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/MATH>`
- [Ee7f47020e342e57f] `<https://example.org/uiuc-course-advisor/resource/course/MATH461> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E97b5e537f5a500f6] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [E8205eb1963f2db0b] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of MATH 461"`
- [Ec409463619337595] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1>`
- [E8762323df6562b13] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "needs_review"`
- [E280f5b4b1dfa1e45] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 241 or equivalent."`
- [E43afa093c8f49b89] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [Ec406377296fdebd7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 461 prerequisite option 1"`
- [Ee4f6bd0605ddf0b7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1/condition/1>`
- [Eb997515c445e0d95] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [Eed011e7f60aa69d0] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 461 opt 1 cond 1: requires MATH 241"`
- [E3c9bfbe38551d6a2] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E1b9bbcb87bf473cc] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 241 or equivalent"`
- [E6bd4f031c3725be7] `<https://example.org/uiuc-course-advisor/resource/prereq/MATH461/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH241>`
- [E6e557b45c3d0663f] `<https://example.org/uiuc-course-advisor/resource/offering/MATH461/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E920c072643537d98] `<https://example.org/uiuc-course-advisor/resource/offering/MATH461/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "MATH 461 (Fall 2026)"`
- [Efaa112942a43e6ec] `<https://example.org/uiuc-course-advisor/resource/offering/MATH461/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`
- [Eda3fc3c93ba4b319] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#Course>`
- [E96edd002c5c5ff28] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <http://www.w3.org/2000/01/rdf-schema#label> "STAT 400 Statistics and Probability I"`
- [E2bcf7d94e435e96c] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#courseCode> "STAT 400"`
- [Ef7c922f116e772a2] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMax> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E05edf34a564899d5] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#courseCreditsMin> "4.0"^^<http://www.w3.org/2001/XMLSchema#decimal>`
- [E26fdf23f993688b0] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#courseDescription> "Introduction to mathematical statistics that develops probability as needed; includes the calculus of probability, random variables, expectation, distribution functions, central limit theorem, point estimation, confidence intervals, and hypothesis testing. Offers a basic one-term introduction to statistics and also prepares students for STAT 410 and STAT 425. Same as MATH 463. 4 undergraduate hours. 4 graduate hours. Prerequisite: MATH 231. Not intended for first-time freshmen."`
- [Ea8c116b06e53c6a9] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#courseNumber> "400"^^<http://www.w3.org/2001/XMLSchema#integer>`
- [Eb164661b4e508690] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#courseTitle> "Statistics and Probability I"`
- [Ea6add1b86b719ffc] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#crossListedWith> <https://example.org/uiuc-course-advisor/resource/course/MATH463>`
- [Ecf9f00f049751e61] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#hasOffering> <https://example.org/uiuc-course-advisor/resource/offering/STAT400/2026-fa>`
- [Ec72676953043f81b] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression> <https://example.org/uiuc-course-advisor/resource/prereq/STAT400>`
- [E7f3ca34f136738f6] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#inDepartment> <https://example.org/uiuc-course-advisor/resource/department/STAT>`
- [E7b36293f0aa71945] `<https://example.org/uiuc-course-advisor/resource/course/STAT400> <https://example.org/uiuc-course-advisor/ontology#sourceURL> "https://discovery.cs.illinois.edu/dataset/course-catalog/"^^<http://www.w3.org/2001/XMLSchema#anyURI>`
- [E3d21612b1b52f229] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteExpression>`
- [Ef3a22db4099eb22b] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400> <http://www.w3.org/2000/01/rdf-schema#label> "Prerequisites of STAT 400"`
- [Ed9cc6ad54c0eab64] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400> <https://example.org/uiuc-course-advisor/ontology#hasOption> <https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1>`
- [E99f6d106b30aabac] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400> <https://example.org/uiuc-course-advisor/ontology#parseStatus> "parsed"`
- [E43c145d82a56402c] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400> <https://example.org/uiuc-course-advisor/ontology#prerequisiteSourceText> "MATH 231."`
- [E3f791afec890058f] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#PrerequisiteOption>`
- [E87f9c489fa7c0805] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1> <http://www.w3.org/2000/01/rdf-schema#label> "STAT 400 prerequisite option 1"`
- [E38beee581f19536a] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1> <https://example.org/uiuc-course-advisor/ontology#hasCondition> <https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1/condition/1>`
- [Ed044451e3ac5932e] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1/condition/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseCondition>`
- [E559b51d605111b5c] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1/condition/1> <http://www.w3.org/2000/01/rdf-schema#label> "STAT 400 opt 1 cond 1: requires MATH 231"`
- [Ebf575aebfde758ec] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#allowsConcurrent> "false"^^<http://www.w3.org/2001/XMLSchema#boolean>`
- [E3d7651f865a88c42] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#conditionSourceText> "MATH 231"`
- [E8d906037543866af] `<https://example.org/uiuc-course-advisor/resource/prereq/STAT400/option/1/condition/1> <https://example.org/uiuc-course-advisor/ontology#requiredCourse> <https://example.org/uiuc-course-advisor/resource/course/MATH231>`
- [E802d23dc5a84fd15] `<https://example.org/uiuc-course-advisor/resource/offering/STAT400/2026-fa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://example.org/uiuc-course-advisor/ontology#CourseOffering>`
- [E4c2a872379dd7819] `<https://example.org/uiuc-course-advisor/resource/offering/STAT400/2026-fa> <http://www.w3.org/2000/01/rdf-schema#label> "STAT 400 (Fall 2026)"`
- [Ebb214125edff0987] `<https://example.org/uiuc-course-advisor/resource/offering/STAT400/2026-fa> <https://example.org/uiuc-course-advisor/ontology#offeredInTerm> <https://example.org/uiuc-course-advisor/resource/term/2026-fa>`

## Inferred knowledge (OWL schema closure)

No facts of this kind were retrieved.

## Application rule results and query provenance

These conclusions are computed; they are not asserted RDF triples.

```json
{
  "intent": "Q08",
  "query": "# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)\n# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)\n# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.\nBASE <https://example.org/uiuc-course-advisor/resource/>\nPREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>\nPREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\nPREFIX owl:  <http://www.w3.org/2002/07/owl#>\nPREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>\n\n\n# CQ08 | courses >= 2 prerequisite hops upstream of CS 440\n# Features: property path one-or-more (+) after an explicit first hop (= 2+ hops), alternative paths\nSELECT DISTINCT ?upstreamCode ?viaCode ?firstHop WHERE {\n  <course/CS440> uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition ?k1 .\n  ?k1 uca:requiredCourse|uca:alternativeCourse ?via .\n  ?via (uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition/(uca:requiredCourse|uca:alternativeCourse))+ ?up .\n  BIND(IF(EXISTS { ?k1 a uca:CourseChoiceCondition }, \"via one-of group (potential)\", \"via required course\") AS ?firstHop)\n  ?up uca:courseCode ?upstreamCode .\n  ?via uca:courseCode ?viaCode .\n  FILTER(?up != <course/CS440> && ?up != ?via)\n}\nORDER BY ?upstreamCode ?viaCode\n",
  "rows": [
    {
      "upstreamCode": "BIOE 210",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "CS 101",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "CS 101",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "CS 124",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "CS 124",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "CS 125",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "CS 126",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "CS 128",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "CS 173",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "CS 374",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "CS 413",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "ECE 120",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "ECE 220",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 112",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 112",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 112",
      "viaCode": "CS 361",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 112",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 112",
      "viaCode": "MATH 461",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 112",
      "viaCode": "STAT 400",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 115",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 115",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 115",
      "viaCode": "CS 361",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 115",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 115",
      "viaCode": "MATH 461",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 115",
      "viaCode": "STAT 400",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 213",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 220",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 220",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 220",
      "viaCode": "CS 361",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 220",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 220",
      "viaCode": "MATH 461",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 220",
      "viaCode": "STAT 400",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 221",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 221",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 221",
      "viaCode": "CS 361",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 221",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 221",
      "viaCode": "MATH 461",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 221",
      "viaCode": "STAT 400",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 231",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 231",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 231",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 231",
      "viaCode": "MATH 461",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 231",
      "viaCode": "STAT 400",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 241",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 241",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 241",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 241",
      "viaCode": "MATH 461",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 257",
      "viaCode": "BIOE 310",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 257",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 314",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 314",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 347",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 347",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    },
    {
      "upstreamCode": "MATH 412",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 413",
      "viaCode": "CS 225",
      "firstHop": "via required course"
    },
    {
      "upstreamCode": "MATH 416",
      "viaCode": "ECE 313",
      "firstHop": "via one-of group (potential)"
    }
  ],
  "reasoning": [],
  "graph_sha256": "ac0352a0246d3e67fae34d3fd27f3847bb9a3d7897478f19e865478f2a1ea2a8"
}
```

## Prediction

None. Option C verifies graph paths; hypothetical completions are labelled assumptions.

## Limitations

