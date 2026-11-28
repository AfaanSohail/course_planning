
# course_planning — Consolidated Iterations 1 and 2

DRAFT: scored trial 3 results are included. Final video, source commit and live review evidence remain pending.

AI-3001 Knowledge Representation & Reasoning | Instructor: Ms. Mehreen Javaid

| Team member | Roll number | GitHub |
| --- | --- | --- |
| Afaan Sohail | 24i-0081 | AfaanSohail |
| Hassan Tariq | 24i-2555 | hassan-cpp |
| Diya Hurmat | 24i-0094 | Diya22466 |

Repository: https://github.com/AfaanSohail/course_planning

Submitted implementation source commit: PENDING: immutable submission source commit

External demo video: PENDING: record and upload actual demo


# Problem, data and Iteration 1 design

Knowledge-Grounded University Course Planning and Prerequisite Advisory System: use the supplied UIUC Fall 2026 catalog and curated BS Computer Science requirements to explain possible prerequisites, synthetic-student eligibility and recorded degree allocations. Data flows through RDF, ontology rules, SPARQL, multi-hop reasoning, retrieval and an LLM answer with evidence.

| Measured artifact | Result |
| --- | --- |
| explicit_triples | 28638 |
| schema_triples | 561 |
| abox_triples | 28077 |
| owlrl_closure_triples | 63055 |
| rebuild_isomorphic | True |
| shacl_conforms | True |

| Named ontology declarations | Count |
| --- | --- |
| classes | 22 |
| object_properties | 32 |
| datatype_properties | 39 |

| Entity class | Observed instances |
| --- | --- |
| Course | 588 |
| CourseOffering | 501 |
| Section | 1035 |
| Instructor | 208 |
| Department | 48 |
| PrerequisiteExpression | 339 |
| PrerequisiteOption | 369 |
| CourseCondition | 255 |
| CourseChoiceCondition | 161 |
| StandingCondition | 6 |
| ConsentCondition | 56 |
| OtherCondition | 33 |
| Student | 4 |
| CourseCompletion | 46 |
| PlannedEnrollment | 12 |
| CoreRequirement | 6 |
| ElectiveRequirement | 12 |

Parse statuses: {"needs_review": 61, "parsed": 278}. Source SHA256: ac0352a0246d3e67fae34d3fd27f3847bb9a3d7897478f19e865478f2a1ea2a8

The current local OWL RL count supersedes the historical closure count in project notes. The input TTL and ontology remain unchanged. SHACL conformity covers the supplied structural shapes; the separate Python degree-policy check can still detect the seeded distinct-electives conflict.


# Original competency questions

| CQ | Competency question | Tags | Tested with |
| --- | --- | --- | --- |
| CQ01 | Given a student's completed courses and a target term, which catalog courses are offered in that term and have a satisfied prerequisite alternative? | MH, INF, KG-hard | student S002, Fall 2026 |
| CQ02 | For a selected course, what are its possible prerequisite chains back to courses with no recorded course prerequisites, preserving AND/OR branches? | MH | CS 421 |
| CQ03 | Which prerequisite alternatives for a target course are fully met by a given student, and which precise course, standing, or consent conditions remain unmet? | INF, KG-hard | S003 -> CS 421 |
| CQ04 | If a student completes one additional course, which downstream courses may become available and what other conditions would still have to hold? | MH, INF | S002 + CS 225 |
| CQ05 | Which courses offered in a target term are both prerequisite-eligible for a student and candidates for that student's unmet degree requirements? | MH, KG-hard | S002, Fall 2026 |
| CQ06 | How many courses and credit hours are still needed in each core or elective group for a given student and degree-program catalog year? | AGG, KG-hard | S003, BS CS 2026 |
| CQ07 | Which 300- or 400-level courses in CS, MATH, ECE or STAT are offered in a selected term and require non-course approvals or standing? | FILTER | Fall 2026 |
| CQ08 | Which courses are at least two prerequisite-course links upstream of a selected target course, and through which alternative branches are they reachable? | MH | CS 440 |
| CQ09 | Which degree requirement groups could be satisfied by more than one catalog course, and how many eligible choices does each group have? | AGG | BS CS 2026 |
| CQ10 | For a selected course, which cross-listed course codes and downstream prerequisites reference its codes, and are any substitutions still subject to explicit policy? | MH | CS 374 |
| CQ11 | For each department, how many available courses could fulfill a particular elective group in a selected term? | MH, AGG, INF (OWL) | advanced electives, Fall 2026 |
| CQ12 | Which required course offerings are blocked only by non-course conditions, such as standing or instructor consent, rather than missing completed courses? | INF, FILTER | all 4 students, Fall 2026 |
| CQ13 | How does the set of satisfiable prerequisite options and course recommendations change when one planned completion is hypothetically added to a student's transcript? | MH, INF, KG-hard | S002 + CS 225 |
| CQ14 | Which completed courses could count toward multiple remaining requirement groups, and which assignment would respect the program's no-double-counting rules? | AGG, KG-hard | S004 |
| CQ15 | What catalog wording, degree requirement and prerequisite-option evidence supports each recommendation, and which conditions remain unverified? | INF, KG-hard | S002's planned courses |


# Original CQ-to-KG mapping

| CQ / field | Original mapping |
| --- | --- |
| CQ01 | CQ01 |
| Classes:  | Student, CourseCompletion, Course, PrerequisiteExpression, PrerequisiteOption, CourseCondition, CourseChoiceCondition, StandingCondition, ConsentCondition, CourseOffering, AcademicTerm |
| Properties / data:  | hasCompletion/completedCourse, hasPlannedEnrollment/plannedCourse, allowsConcurrent, hasPrerequisiteExpression/hasOption/hasCondition, requiredCourse\|alternativeCourse, standingRank, hasPermissionFor, hasOffering/offeredInTerm |
| SPARQL pattern:  | per-condition score via OPTIONAL+BIND/IF/EXISTS; GROUP BY option HAVING MIN(met)=1; join offering; FILTER NOT EXISTS completed |
| Query:  | Q01 |
| Answer from the KG (Fall 2026 data):  | 15 courses, e.g. CS 225, CS 233 (via concurrent CS 225), CS 361, MATH 241, STAT 400 |
| CQ02 | CQ02 |
| Classes:  | Course, PrerequisiteExpression, PrerequisiteOption, CourseCondition, CourseChoiceCondition |
| Properties / data:  | path (hasPrerequisiteExpression/hasOption/hasCondition/(requiredCourse\|alternativeCourse))* |
| SPARQL pattern:  | property path *; edge type AND/OR from condition class; base course = NOT EXISTS hasPrerequisiteExpression |
| Query:  | Q02 (+ INF2 shortcut) |
| Answer from the KG (Fall 2026 data):  | 79 edges in CS 421's tree down to base courses (e.g. CS 124 -> MATH 112 -> …) |
| CQ03 | CQ03 |
| Classes:  | Student, PrerequisiteOption, all 5 condition classes |
| Properties / data:  | hasOption, hasCondition, conditionSourceText, requiredCourse\|alternativeCourse, standingRank, minimumStandingRank, hasPermissionFor |
| SPARQL pattern:  | two subqueries: per-condition status + per-option MIN |
| Query:  | Q03 |
| Answer from the KG (Fall 2026 data):  | CS 421 option 1 not met: "CS 374 or ECE 374" unmet; the other two groups met |
| CQ04 | CQ04 |
| Classes:  | Course, PrerequisiteOption, conditions, Student |
| Properties / data:  | hasCondition/(requiredCourse\|alternativeCourse) = added course; hypothetical met-score |
| SPARQL pattern:  | FILTER EXISTS mention; GROUP_CONCAT of still-unmet conditions |
| Query:  | Q04 |
| Answer from the KG (Fall 2026 data):  | 28 dependants of CS 225; 17 become satisfiable (e.g. CS 374, CS 411), 11 still blocked (CS 440 still needs a probability course) |
| CQ05 | CQ05 |
| Classes:  | DegreeProgram, DegreeRequirement, Course, CourseOffering, Student |
| Properties / data:  | hasRequirement, allowsCourse, minCourses, allocatedToRequirement, + CQ01 pattern |
| SPARQL pattern:  | UNION (option satisfied ∪ no prerequisite); subquery COUNT allocations; FILTER(allocated < minCourses) |
| Query:  | Q05 |
| Answer from the KG (Fall 2026 data):  | 126 (course, unmet group) pairs for S002 |
| CQ06 | CQ06 |
| Classes:  | DegreeProgram, CoreRequirement, ElectiveRequirement, CourseCompletion |
| Properties / data:  | hasRequirement, minCourses, minCredits, allocatedToRequirement, creditsEarned |
| SPARQL pattern:  | OPTIONAL left join; COUNT, SUM, COALESCE, arithmetic BIND |
| Query:  | Q06 |
| Answer from the KG (Fall 2026 data):  | S003: CS technical core 6/11 (5 to go), technical electives 0/6, math-physics 3/4; Calc I, linear algebra, ENG 100 done |
| CQ07 | CQ07 |
| Classes:  | Course, Department, CourseOffering, StandingCondition, ConsentCondition |
| Properties / data:  | courseNumber, inDepartment/subjectCode, hasOffering/offeredInTerm, hasCondition |
| SPARQL pattern:  | VALUES condition types; FILTER(?n >= 300 && ?n < 500), FILTER(?subject IN (...)) |
| Query:  | Q07 |
| Answer from the KG (Fall 2026 data):  | 27 rows, e.g. CS 397 (consent), CS 492 (senior standing), CS 497 (junior standing), MATH 447 |
| CQ08 | CQ08 |
| Classes:  | Course, PrerequisiteOption, CourseCondition, CourseChoiceCondition |
| Properties / data:  | first hop + path + |
| SPARQL pattern:  | explicit hop followed by (...)+ = ≥ 2 hops; branch type from condition class |
| Query:  | Q08 (+ INF2) |
| Answer from the KG (Fall 2026 data):  | 56 (upstream, via) pairs, e.g. CS 124 via CS 225 (required), MATH 220 via CS 361 (one-of group) |
| CQ09 | CQ09 |
| Classes:  | DegreeProgram, DegreeRequirement, Course, CourseOffering |
| Properties / data:  | hasRequirement, allowsCourse, hasOffering/offeredInTerm |
| SPARQL pattern:  | COUNT(DISTINCT), GROUP BY, HAVING > 1, OPTIONAL |
| Query:  | Q09 |
| Answer from the KG (Fall 2026 data):  | 17 groups; advanced electives 225 choices (offered 191 of them), technical electives 66, NST science 53 |
| CQ10 | CQ10 |
| Classes:  | Course, CourseCondition, CourseChoiceCondition |
| Properties / data:  | crossListedWith (symmetric), requiredCourse\|alternativeCourse |
| SPARQL pattern:  | path crossListedWith\|^crossListedWith; FILTER IN; EXISTS both codes |
| Query:  | Q10 (+ INF4) |
| Answer from the KG (Fall 2026 data):  | ECE 374 alias; 9 dependants; 7 accept both codes, while MATH 412 and MATH 417 name only CS 374 (substitution is a policy question) |
| CQ11 | CQ11 |
| Classes:  | Department, Course, ElectiveRequirement, AcademicTerm |
| Properties / data:  | inferred hasCourse (inverse), maySatisfyRequirement (inverse), scheduledInTerm (property chain) |
| SPARQL pattern:  | aggregation over inferred properties |
| Query:  | Q11 |
| Answer from the KG (Fall 2026 data):  | CS 50, ECE 46, MATH 30, STAT 19, PHYS 17, … (16 departments); 0 rows without reasoning |
| CQ12 | CQ12 |
| Classes:  | Course, CourseOffering, Student, StandingCondition, ConsentCondition, CourseCondition |
| Properties / data:  | condition scores split into course vs. non-course |
| SPARQL pattern:  | nested subqueries, SUM/MAX, HAVING (no option fully met, one option blocked only by standing/consent) |
| Query:  | Q12 |
| Answer from the KG (Fall 2026 data):  | 83 (student, course) pairs, e.g. CS 397 (consent), CS 492 (senior standing) |
| CQ13 | CQ13 |
| Classes:  | Student, CourseCompletion, Course, PrerequisiteOption |
| Properties / data:  | completion check OR hypothetical course |
| SPARQL pattern:  | VALUES ?scenario; HAVING COUNT(DISTINCT scenario)=1 && SAMPLE=… |
| Query:  | Q13 |
| Answer from the KG (Fall 2026 data):  | 17 courses open up only with CS 225, e.g. CS 233, CS 340, CS 374, CS 411 |
| CQ14 | CQ14 |
| Classes:  | CourseCompletion, DegreeRequirement, Course |
| Properties / data:  | completedCourse, allowsCourse, allocatedToRequirement |
| SPARQL pattern:  | COUNT DISTINCT, GROUP_CONCAT, HAVING > 1, EXISTS rule check |
| Query:  | Q14 (+ V6) |
| Answer from the KG (Fall 2026 data):  | CS 411 fits 4 groups and is allocated to technical and advanced electives, so it violates the distinct-electives rule (seeded test); CS 440, PHYS 211/212 fit 2 to 3 groups |
| CQ15 | CQ15 |
| Classes:  | Course, PrerequisiteExpression, PrerequisiteCondition, DegreeRequirement |
| Properties / data:  | prerequisiteSourceText, parseStatus, requirementNote, sourceURL, OtherCondition |
| SPARQL pattern:  | several OPTIONALs + subquery count of satisfied options |
| Query:  | Q15 |
| Answer from the KG (Fall 2026 data):  | CS 225 & MATH 241: satisfied, evidence shown; MATH 257: 0 options met (needs CS 101) and flagged needs manual check ("or equivalent programming experience") |


# Catalog column to RDF mapping

| CSV column(s) | RDF class / property |
| --- | --- |
| Subject | uca:Department (department/{Subject}), uca:subjectCode; course uca:inDepartment dept |
| Subject + Number | uca:Course (course/{Subject}{Number}), uca:courseCode "CS 225", uca:courseNumber 225 |
| Name | uca:courseTitle, part of rdfs:label |
| Description | uca:courseDescription; prerequisite sentence -> uca:PrerequisiteExpression tree; "Same as ..." -> uca:crossListedWith |
| Credit Hours | uca:courseCreditsMin, uca:courseCreditsMax |
| Degree Attributes | uca:hasDegreeAttribute; "Nat Sci & Tech" -> Elective-Science uca:allowsCourse course |
| Year, Term, YearTerm | uca:AcademicTerm (term/2026-fa, uca:year, uca:termName); uca:CourseOffering (offering/CS225/2026-fa) via uca:hasOffering, uca:offeredInTerm |
| CRN, Section, Type, Type Code | uca:Section (section/2026-fa/{CRN}-{TypeCode}), uca:crn, uca:sectionCode, uca:sectionType, uca:sectionOf |
| Days of Week, Start/End Time, Building, Room, Enrollment Status | uca:meetingDays, uca:startTime, uca:endTime, uca:buildingName, uca:roomNumber, uca:enrollmentStatus |
| Instructors | uca:Instructor (instructor/{slug}), uca:instructorName; section uca:taughtBy instructor |
| (dataset URL) | uca:sourceURL provenance on every catalog course |
| Course numbers (rule R4) | Elective-Technical (CS 397 + CS 4xx except 400 to 403, 491) and Elective-Advanced (any 4xx + CS 397) uca:allowsCourse |


# Preserved URI design

| URI pattern | Example | Rationale |
| --- | --- | --- |
| Ontology namespace https://example.org/uiuc-course-advisor/ontology# (uca:) | uca:Course | hash namespace for the vocabulary; versioned via owl:versionIRI .../ontology/1.3 |
| Resource base https://example.org/uiuc-course-advisor/resource/ |  | slash URIs for instances; one base (works with SPARQL BASE) |
| course/{SUBJ}{NUM} | course/CS225 | stable natural key, no spaces, matches the phase-2 design and the requirement file |
| department/{SUBJ} | department/CS | subject code is the catalog's department key |
| term/{YYYY}-{fa\|sp\|su\|wi} | term/2026-fa | same as the dataset's YearTerm |
| offering/{course}/{term} | offering/CS225/2026-fa | one course per term; course and term stay separate entities |
| section/{term}/{CRN}-{TypeCode} | section/2026-fa/30094-LEC | CRNs are reused across terms, and one CRN can have several meeting types |
| instructor/{slug(name)} | instructor/adve-v | lower-case, hyphenated name as printed |
| prereq/{course} -> /option/{i} -> /condition/{j} | prereq/CS421/option/1/condition/2 | hierarchical, human-readable, deterministic (rebuilds produce identical IRIs) |
| program/UIUC-BS-CS-2026, requirement/UIUC-BS-CS-2026/{group} | requirement/UIUC-BS-CS-2026/Core-CSTechnical | program + catalog year; groups scoped by program |
| student/{id}, completion/{id}/{course}, plan/{id}/{course}/{term} | completion/S003/CS225 | pseudonymous ids, one completion per student-course |


# Ontology classes

| Class | Subclass of | Meaning |
| --- | --- | --- |
| AcademicTerm | owl:Thing | An academic term with year and season, identified independently of offerings. |
| ConsentCondition | PrerequisiteCondition | Permission/consent requirement that must be checked explicitly. |
| CoreRequirement | DegreeRequirement | A degree requirement for compulsory/core courses. |
| Course | owl:Thing | Unique academic course, not a section or offering. URI is subject plus course number. |
| CourseChoiceCondition | PrerequisiteCondition | A prerequisite condition satisfied by ANY ONE of its alternativeCourse values (catalog wording 'A or B' / 'one of A, B, C'). Used inside an option, so an option stays an AND of conditions while each group keeps its OR. |
| CourseCompletion | owl:Thing | Student-specific evidence that a course was completed, optionally with grade and credits. |
| CourseCondition | PrerequisiteCondition | A prerequisite course, with optional concurrency flag and grade requirement. |
| CourseOffering | owl:Thing | One course offered in one academic term; may have one or more sections if source data allows. |
| CourseWithPrerequisites | owl:Thing | Defined class: a Course that has at least one PrerequisiteExpression. Membership is INFERRED by the reasoner (owl:equivalentClass), never asserted in the A-Box. |
| DegreeProgram | owl:Thing | A declared degree plan and catalog version. |
| DegreeRequirement | owl:Thing | A requirement bucket/group in a degree program; groups normally all need fulfilment. |
| Department | owl:Thing | Academic subject or department offering courses. |
| ElectiveRequirement | DegreeRequirement | A degree requirement for electives chosen from an allowed course set. |
| Instructor | owl:Thing | A person who teaches one or more sections; populated from the catalog Instructors column. |
| OtherCondition | PrerequisiteCondition | Any unsupported or free-text condition kept for review rather than silently ignored. |
| PlannedEnrollment | owl:Thing | A proposed course enrollment in a target term, separate from a completed course. |
| PrerequisiteCondition | owl:Thing | Abstract prerequisite condition, specialized into course/standing/consent/other. |
| PrerequisiteExpression | owl:Thing | Complete prerequisite expression for a course. Its options are OR alternatives. |
| PrerequisiteOption | owl:Thing | One permissible alternative: ALL conditions linked by hasCondition must hold (AND). |
| Section | owl:Thing | A section/meeting row of a course offering (catalog CRN + Type). One Section per CRN and meeting type, because a CRN may list several meeting rows. The chosen catalog CSV is section-level, so this class is populated. |
| StandingCondition | PrerequisiteCondition | A standing/year restriction that cannot be reduced to a course code. |
| Student | owl:Thing | A student whose transcript and permissions are available for planning. |


# Ontology object properties

| Property | Domain | Range | Characteristics |
| --- | --- | --- | --- |
| allocatedToRequirement | CourseCompletion | DegreeRequirement |  |
| allowsCourse | DegreeRequirement | Course | inverse of maySatisfyRequirement |
| alternativeCourse | CourseChoiceCondition | Course | subPropertyOf mentionsCourse |
| belongsToProgram | DegreeRequirement | DegreeProgram | inverse of hasRequirement |
| completedCourse | CourseCompletion | Course |  |
| completionTerm | CourseCompletion | AcademicTerm |  |
| crossListedWith | Course | Course | symmetric |
| hasCompletedCourse | Student | Course | chain: hasCompletion ∘ completedCourse |
| hasCompletion | Student | CourseCompletion |  |
| hasCondition | PrerequisiteOption | PrerequisiteCondition |  |
| hasCourse | Department | Course | inverse of inDepartment |
| hasOffering | Course | CourseOffering | inverse of offeringOf |
| hasOption | PrerequisiteExpression | PrerequisiteOption |  |
| hasPermissionFor | Student | Course |  |
| hasPlannedEnrollment | Student | PlannedEnrollment |  |
| hasPrerequisiteCandidate | Course | Course | subPropertyOf hasPrerequisitePath; chain: hasPrerequisiteExpression ∘ hasOption ∘ hasCondition ∘ mentionsCourse |
| hasPrerequisiteExpression | Course | PrerequisiteExpression |  |
| hasPrerequisitePath | Course | Course | transitive |
| hasRequirement | DegreeProgram | DegreeRequirement | inverse of belongsToProgram |
| hasSection | CourseOffering | Section | inverse of sectionOf |
| inDepartment | Course | Department | inverse of hasCourse |
| maySatisfyRequirement | Course | DegreeRequirement | inverse of allowsCourse |
| mentionsCourse | PrerequisiteCondition | Course |  |
| offeredInTerm | CourseOffering | AcademicTerm |  |
| offeringOf | CourseOffering | Course | inverse of hasOffering |
| plannedCourse | PlannedEnrollment | Course |  |
| plannedTerm | PlannedEnrollment | AcademicTerm |  |
| requiredCourse | CourseCondition | Course | subPropertyOf mentionsCourse |
| scheduledInTerm | Course | AcademicTerm | chain: hasOffering ∘ offeredInTerm |
| sectionOf | Section | CourseOffering | inverse of hasSection |
| taughtBy | Section | Instructor | inverse of teaches |
| teaches | Instructor | Section | inverse of taughtBy |


# Ontology datatype properties

| Property | Domain | Datatype | Meaning |
| --- | --- | --- | --- |
| allowsConcurrent | PrerequisiteCondition | boolean | True if this course or choice condition accepts concurrent registration ('credit or concurrent registration in ...'); no automatic completion is assumed. |
| buildingName | Section | string | Building name from the catalog; may be blank for online sections. |
| conditionSourceText | PrerequisiteCondition | string | Original condition clause for auditability. |
| courseCode | Course | string | Canonical code, for example CS 225. |
| courseCreditsMax | Course | decimal | Upper bound of credit hours (or fixed value). |
| courseCreditsMin | Course | decimal | Lower bound of credit hours (or fixed value). |
| courseDescription | Course | string | Original human-readable catalog course description. |
| courseNumber | Course | integer | Numeric course number. |
| courseTitle | Course | string | Catalog course title. |
| creditsEarned | CourseCompletion | decimal | Credits earned from this completion. |
| crn | Section | string | Course registration number if available in a separate section-level source. |
| endTime | Section | string | End time as printed (string, because ARRANGED/blank values occur). |
| enrollmentStatus | Section | string | Enrollment Status column (Open, Closed, CrossListOpen ...), observed snapshot only. |
| gradeAwarded | CourseCompletion | string | Grade from transcript, if known. |
| hasDegreeAttribute | Course | string | Catalog degree/gen-ed attribute text, preserved verbatim. |
| instructorName | Instructor | string | Instructor name as printed in the catalog (e.g. "Kim, G"). |
| meetingDays | Section | string | Days-of-week string from the catalog (e.g. MWF, TR, ARRANGED). |
| minCourses | DegreeRequirement | nonNegativeInteger | Minimum courses to allocate to this group, if applicable. |
| minCredits | DegreeRequirement | decimal | Minimum awarded credits to allocate to this group, if applicable. |
| minTechnicalGPA | DegreeProgram | decimal | Minimum technical GPA (CS and Math courses for this program). |
| minUpperDivisionCredits | DegreeProgram | decimal | Minimum upper-division (300/400-level) credit hours. |
| minimumGrade | CourseCondition | string | Raw minimum grade string, if explicit. |
| minimumStandingRank | StandingCondition | integer | Standing/year rank. Fixed encoding: 1=Freshman, 2=Sophomore, 3=Junior, 4=Senior, 5=Graduate. A requirement such as "Junior, Senior or Graduate" is stored as minimumStandingRank 3. |
| parseStatus | PrerequisiteExpression | string | parsed, needs_review, unknown; NOT OWL reasoning result. |
| prerequisiteSourceText | PrerequisiteExpression | string | Original prerequisite prose, retained for explanations. |
| programCatalogYear | DegreeProgram | integer | Year/version to which degree rules apply. |
| programName | DegreeProgram | string | Degree title. |
| requirementNote | DegreeRequirement | string | Verbatim or condensed catalog policy for this group (letter-grade rule, caps, substitution, permission, distinct-from-other-group rules) that cannot be reduced to minCourses/minCredits. |
| roomNumber | Section | string | Room from the catalog; may be blank. |
| sectionCode | Section | string | Section label if section data exists. |
| sectionType | Section | string | Meeting type from the catalog Type column (Lecture, Discussion/Recitation, Laboratory, Online ...). |
| sourceURL |  | anyURI | Link to catalog or official degree-program source; provenance property. |
| standingRank | Student | integer | Standing/year rank. Fixed encoding: 1=Freshman, 2=Sophomore, 3=Junior, 4=Senior, 5=Graduate. A requirement such as "Junior, Senior or Graduate" is stored as minimumStandingRank 3. |
| startTime | Section | string | Start time as printed (string, because ARRANGED/blank values occur). |
| studentIdentifier | Student | string | Pseudonymous student reference; avoid real records in demos. |
| subjectCode | Department | string | Academic subject code, e.g. CS. |
| termName | AcademicTerm | string | Fall, Spring, Summer, or Winter. |
| totalCreditsRequired | DegreeProgram | decimal | Minimum total credit hours required for graduation. |
| year | AcademicTerm | integer | Calendar year of academic term. |


# Schema constructs

| # | Construct | Where it is used |
| --- | --- | --- |
| 1 | rdfs:subClassOf | class hierarchy (e.g. CoreRequirement, ElectiveRequirement ⊑ DegreeRequirement; five condition classes ⊑ PrerequisiteCondition) |
| 2 | rdfs:subPropertyOf | hasPrerequisiteCandidate ⊑ hasPrerequisitePath, alternativeCourse ⊑ mentionsCourse, requiredCourse ⊑ mentionsCourse |
| 3 | rdfs:domain / rdfs:range | on every property (see tables above) |
| 4 | owl:inverseOf | allowsCourse <-> maySatisfyRequirement, hasRequirement <-> belongsToProgram, hasSection <-> sectionOf, inDepartment <-> hasCourse, taughtBy <-> teaches, hasOffering <-> offeringOf |
| 5 | owl:propertyChainAxiom | hasCompletedCourse <- hasCompletion ∘ completedCourse; hasPrerequisiteCandidate <- hasPrerequisiteExpression ∘ hasOption ∘ hasCondition ∘ mentionsCourse; scheduledInTerm <- hasOffering ∘ offeredInTerm |
| 6 | owl:TransitiveProperty | hasPrerequisitePath |
| 7 | owl:SymmetricProperty | crossListedWith |
| 8 | owl:equivalentClass (defined class) | CourseWithPrerequisites ≡ Course ⊓ ∃hasPrerequisiteExpression.PrerequisiteExpression |
| 9 | Disjointness and restrictions | pairwise owl:disjointWith, one owl:AllDisjointClasses, 11 owl:Restriction axioms (10 listed below as superclass restrictions, plus one inside the owl:equivalentClass definition) |


# Ontology restrictions

| Class | Restriction |
| --- | --- |
| CourseChoiceCondition | ⊑ alternativeCourse some Course |
| CourseCompletion | ⊑ completedCourse exactly 1 Course |
| CourseCompletion | ⊑ completedCourse some Course |
| CourseCondition | ⊑ requiredCourse some Course |
| CourseCondition | ⊑ requiredCourse exactly 1 Course |
| CourseOffering | ⊑ offeringOf exactly 1 Course |
| CourseOffering | ⊑ offeredInTerm exactly 1 AcademicTerm |
| DegreeRequirement | ⊑ belongsToProgram some DegreeProgram |
| PrerequisiteExpression | ⊑ hasOption some PrerequisiteOption |
| PrerequisiteOption | ⊑ hasCondition some PrerequisiteCondition |


# Operational rules

| Rule | Statement | Implemented in |
| --- | --- | --- |
| R1 | An option is satisfied only if every condition is verified: completed course (or planned concurrent enrolment when allowsConcurrent is true), standingRank ≥ minimumStandingRank, recorded consent. Unknown conditions never pass. | Q01, Q03, Q12 |
| R2 | A course is prerequisite-eligible if it has no prerequisite expression or at least one satisfied option; it is recommended for a term only if an offering exists in that term. | Q01, Q05 |
| R3 | A requirement group is fulfilled when enough distinct completions allocated to it meet minCourses and minCredits. | Q06, Q14 |
| R4 | Technical and advanced elective groups are filled from course numbers (CS 397 and CS 4xx except 400 to 403, 491; any 4xx). | links in abox_requirement_links.ttl |


# Data sources, cleaning and transformation

Source files: iteration1/Dataset/course-catalog.csv (catalog snapshot), uiuc-prerequisites.csv (QA only), and the curated requirement/student A-Boxes. The original build_kg.py and prereq_parser.py are preserved and executed by the reproduction script. Curated corrections are retained. HTML entities and whitespace are normalized; duplicate rows are removed; repeated section rows are merged; null fields produce no empty RDF literal. Referenced missing courses become labelled stubs with no invented titles or offerings. The builder's graph-isomorphism result and raw build log are retained.

| Issue | Decision |
| --- | --- |
| Exact duplicate rows | dropped |
| Leading/trailing whitespace | stripped on every column |
| HTML entities (&amp; in titles) | html.unescape on Name, Description, Section Info, Section Title, Degree Attributes |
| Course identity | key = upper-case Subject + 3-digit Number (CS225); rows with invalid numbers would be dropped |
| Section rows -> course | course-level attributes taken once per course; verified identical across that course's rows |
| Credit hours text | "3 hours." -> min=max=3; "3 OR 4 hours." -> 3/4; "2 TO 4 hours." -> 2/4 (xsd:decimal) |
| Empty values (null handling) | no triple is created (no empty literals); "UNKNOWN" enrollment status treated as null |
| Repeated meeting rows of one CRN + meeting type | one Section per (term, CRN, Type Code); first meeting kept |
| Instructors | Instructors column split on ;, one Instructor node per normalised name (adve-v) |
| Times | kept as printed strings (ARRANGED/blank exist) |
| Course numbers | xsd:integer, enabling numeric FILTERs (CQ07) |

```
abox_catalog.ttl: 26,948 triples
abox_degree_requirements.ttl: 323 triples
abox_requirement_links.ttl: 344 triples
abox_students_synthetic.ttl: 462 triples
uiuc_course_kg.ttl: 28,638 triples (including ontology)
Reference comparison: exact RDF graph match (isomorphic, including OWL blank nodes).

```


# Re-executed SPARQL queries and outputs

| Query | Current rows | Archived rows | Match after URI/concat normalization |
| --- | --- | --- | --- |
| Q01 | 15 | 15 | True |
| Q02 | 79 | 79 | True |
| Q03 | 3 | 3 | True |
| Q04 | 28 | 28 | True |
| Q05 | 126 | 126 | True |
| Q06 | 18 | 18 | True |
| Q07 | 27 | 27 | True |
| Q08 | 56 | 56 | True |
| Q09 | 17 | 17 | True |
| Q10 | 9 | 9 | True |
| Q11 | 16 | 16 | True |
| Q12 | 83 | 83 | True |
| Q13 | 17 | 17 | True |
| Q14 | 4 | 4 | True |
| Q15 | 3 | 3 | True |
| INF1 | 146 | 146 | True |
| INF2 | 38 | 38 | True |
| INF3 | 4 | 4 | True |
| INF4 | 17 | 17 | True |
| INF5 | 3 | 3 | True |
| INF6 | 8 | 8 | True |


# Q01_eligible_offered_courses

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ01 | Fall 2026 courses S002 is prerequisite-eligible for
# Features: BGP, subquery, OPTIONAL, BIND/IF, EXISTS, aggregation (MIN, COUNT, GROUP BY, HAVING)
SELECT ?courseCode ?title (COUNT(DISTINCT ?option) AS ?satisfiedOptions) WHERE {
  { SELECT ?course ?option WHERE {
      BIND(<student/S002> AS ?s)
      ?course uca:hasPrerequisiteExpression/uca:hasOption ?option .
      ?option uca:hasCondition ?k .
      OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
      OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
      OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
      OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
      BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
              IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }
                 || EXISTS { ?k uca:allowsConcurrent true ; uca:requiredCourse|uca:alternativeCourse ?rc .
                             ?s uca:hasPlannedEnrollment/uca:plannedCourse ?rc }, 1, 0),
           IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
           IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?met)
    } GROUP BY ?course ?option HAVING (MIN(?met) = 1) }
  ?course uca:hasOffering/uca:offeredInTerm <term/2026-fa> ;
          uca:courseCode ?courseCode .
  OPTIONAL { ?course uca:courseTitle ?title }
  FILTER NOT EXISTS { <student/S002> uca:hasCompletion/uca:completedCourse ?course }
}
GROUP BY ?courseCode ?title
ORDER BY ?courseCode

```

| courseCode | title | satisfiedOptions |
| --- | --- | --- |
| ASRM 210 | Theory of Interest | 1 |
| BIOE 210 | Linear Algebra for Biomedical Data Science | 1 |
| CS 101 | Intro Computing: Engrg & Sci | 1 |
| CS 225 | Data Structures | 1 |
| CS 233 | Computer Architecture | 1 |
| CS 361 | Probability & Statistics for Computer Science | 1 |
| CS 427 | Software Engineering I | 1 |
| IE 310 | Deterministic Models in Optimization | 1 |
| MATH 213 | Basic Discrete Mathematics | 1 |
| MATH 225 | Introductory Matrix Theory | 1 |
| MATH 241 | Calculus III | 1 |
| PHYS 100 | Thinking About Physics | 1 |
| PHYS 212 | University Physics: Elec & Mag | 1 |
| PHYS 213 | Univ Physics: Thermal Physics | 1 |
| STAT 400 | Statistics and Probability I | 1 |


# Q02_prerequisite_tree_CS421

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ02 | prerequisite tree of CS 421 (AND/OR edges)
# Features: property path with zero-or-more (*) over a 4-step sequence with alternative, FILTER IN
SELECT DISTINCT ?fromCode ?option ?edgeType ?toCode ?toIsBaseCourse WHERE {
  <course/CS421> (uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition/(uca:requiredCourse|uca:alternativeCourse))* ?from .
  ?from uca:hasPrerequisiteExpression/uca:hasOption ?opt .
  ?opt uca:hasCondition ?k ; rdfs:label ?optLabel .
  ?k uca:requiredCourse|uca:alternativeCourse ?to ; a ?ct .
  FILTER(?ct IN (uca:CourseCondition, uca:CourseChoiceCondition))
  BIND(IF(?ct = uca:CourseCondition, "AND: required course", "OR: one of a group") AS ?edgeType)
  BIND(STRAFTER(?optLabel, "prerequisite ") AS ?option)
  ?from uca:courseCode ?fromCode .
  ?to uca:courseCode ?toCode .
  BIND(NOT EXISTS { ?to uca:hasPrerequisiteExpression ?e } AS ?toIsBaseCourse)
}
ORDER BY ?fromCode ?option ?edgeType ?toCode

```

| fromCode | option | edgeType | toCode | toIsBaseCourse |
| --- | --- | --- | --- | --- |
| ASRM 210 | option 1 | AND: required course | MATH 231 | false |
| ASRM 406 | option 1 | AND: required course | MATH 241 | false |
| ASRM 406 | option 1 | OR: one of a group | ASRM 210 | false |
| ASRM 406 | option 1 | OR: one of a group | FIN 221 | false |
| ASRM 406 | option 1 | OR: one of a group | MATH 210 | true |
| BIOE 210 | option 1 | AND: required course | MATH 231 | false |
| BIOE 210 | option 1 | OR: one of a group | CS 101 | false |
| BIOE 210 | option 1 | OR: one of a group | CS 124 | false |
| CS 101 | option 1 | OR: one of a group | MATH 220 | false |
| CS 101 | option 1 | OR: one of a group | MATH 221 | false |
| CS 101 | option 1 | OR: one of a group | MATH 231 | false |
| CS 101 | option 1 | OR: one of a group | MATH 241 | false |
| CS 124 | option 1 | AND: required course | MATH 112 | false |
| CS 128 | option 1 | OR: one of a group | CS 124 | false |
| CS 128 | option 1 | OR: one of a group | CS 125 | true |
| CS 173 | option 1 | OR: one of a group | CS 124 | false |
| CS 173 | option 1 | OR: one of a group | CS 125 | true |
| CS 173 | option 1 | OR: one of a group | ECE 220 | false |
| CS 173 | option 1 | OR: one of a group | MATH 220 | false |
| CS 173 | option 1 | OR: one of a group | MATH 221 | false |
| CS 225 | option 1 | OR: one of a group | CS 126 | true |
| CS 225 | option 1 | OR: one of a group | CS 128 | false |
| CS 225 | option 1 | OR: one of a group | CS 173 | false |
| CS 225 | option 1 | OR: one of a group | CS 413 | true |
| CS 225 | option 1 | OR: one of a group | ECE 220 | false |
| CS 225 | option 1 | OR: one of a group | MATH 213 | false |
| CS 225 | option 1 | OR: one of a group | MATH 314 | false |
| CS 225 | option 1 | OR: one of a group | MATH 347 | true |
| CS 225 | option 1 | OR: one of a group | MATH 412 | false |
| CS 225 | option 1 | OR: one of a group | MATH 413 | false |
| CS 233 | option 1 | AND: required course | CS 225 | false |
| CS 233 | option 1 | OR: one of a group | CS 125 | true |
| CS 233 | option 1 | OR: one of a group | CS 128 | false |
| CS 233 | option 1 | OR: one of a group | CS 173 | false |
| CS 233 | option 1 | OR: one of a group | MATH 213 | false |
| CS 340 | option 1 | AND: required course | CS 128 | false |
| CS 340 | option 1 | AND: required course | CS 225 | false |
| CS 374 | option 1 | AND: required course | CS 225 | false |
| CS 374 | option 1 | OR: one of a group | CS 173 | false |
| CS 374 | option 1 | OR: one of a group | MATH 213 | false |
| CS 421 | option 1 | OR: one of a group | ASRM 406 | false |
| CS 421 | option 1 | OR: one of a group | BIOE 210 | false |
| CS 421 | option 1 | OR: one of a group | CS 233 | false |
| CS 421 | option 1 | OR: one of a group | CS 240 | true |
| CS 421 | option 1 | OR: one of a group | CS 340 | false |
| CS 421 | option 1 | OR: one of a group | CS 374 | false |
| CS 421 | option 1 | OR: one of a group | ECE 374 | true |
| CS 421 | option 1 | OR: one of a group | ECE 391 | false |
| CS 421 | option 1 | OR: one of a group | MATH 225 | false |
| CS 421 | option 1 | OR: one of a group | MATH 257 | false |
| CS 421 | option 1 | OR: one of a group | MATH 415 | false |
| CS 421 | option 1 | OR: one of a group | MATH 416 | false |
| ECE 220 | option 1 | AND: required course | ECE 120 | false |
| ECE 391 | option 1 | OR: one of a group | CS 233 | false |
| ECE 391 | option 1 | OR: one of a group | ECE 220 | false |
| FIN 221 | option 1 | OR: one of a group | ECON 102 | true |
| FIN 221 | option 1 | OR: one of a group | ECON 103 | true |
| MATH 115 | option 1 | AND: required course | MATH 112 | false |
| MATH 213 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 213 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 220 | option 1 | AND: required course | MATH 115 | false |
| MATH 225 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 225 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 231 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 231 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 241 | option 1 | AND: required course | MATH 231 | false |
| MATH 257 | option 1 | AND: required course | CS 101 | false |
| MATH 257 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 257 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 314 | option 1 | AND: required course | MATH 241 | false |
| MATH 412 | option 1 | OR: one of a group | CS 374 | false |
| MATH 412 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 412 | option 1 | OR: one of a group | MATH 347 | true |
| MATH 413 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 413 | option 1 | OR: one of a group | MATH 347 | true |
| MATH 415 | option 1 | AND: required course | MATH 241 | false |
| MATH 416 | option 1 | AND: required course | MATH 241 | false |
| MATH 416 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 416 | option 1 | OR: one of a group | MATH 347 | true |


# Q03_option_status_S003_CS421

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ03 | which options/conditions of CS 421 S003 meets
# Features: two subqueries joined on ?option, OPTIONAL, BIND/IF, EXISTS, aggregation (MIN, GROUP BY), STRAFTER
SELECT ?option ?optionStatus ?conditionType ?conditionText ?conditionStatus WHERE {
  { SELECT ?option ?k ?type ?met WHERE {
      BIND(<student/S003> AS ?s) BIND(<course/CS421> AS ?course)
      ?course uca:hasPrerequisiteExpression/uca:hasOption ?option .
      ?option uca:hasCondition ?k .
      ?k a ?type . FILTER(?type IN (uca:CourseCondition, uca:CourseChoiceCondition, uca:StandingCondition,
                                    uca:ConsentCondition, uca:OtherCondition))
      OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
      OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
      OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
      OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
      BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
              IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }
                 || EXISTS { ?k uca:allowsConcurrent true ; uca:requiredCourse|uca:alternativeCourse ?rc .
                             ?s uca:hasPlannedEnrollment/uca:plannedCourse ?rc }, 1, 0),
           IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
           IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?met)
  } }
  { SELECT ?option (MIN(?m2) AS ?optMin) WHERE {
      BIND(<student/S003> AS ?s) BIND(<course/CS421> AS ?course)
      ?course uca:hasPrerequisiteExpression/uca:hasOption ?option .
      ?option uca:hasCondition ?k .
      OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
      OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
      OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
      OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
      BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
              IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }
                 || EXISTS { ?k uca:allowsConcurrent true ; uca:requiredCourse|uca:alternativeCourse ?rc .
                             ?s uca:hasPlannedEnrollment/uca:plannedCourse ?rc }, 1, 0),
           IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
           IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?m2)
    } GROUP BY ?option }
  ?k uca:conditionSourceText ?conditionText .
  BIND(STRAFTER(STR(?type), "#") AS ?conditionType)
  BIND(IF(?met = 1, "met", "UNMET / needs review") AS ?conditionStatus)
  BIND(IF(?optMin = 1, "FULLY MET", "not met") AS ?optionStatus)
}
ORDER BY ?option ?conditionType

```

| option | optionStatus | conditionType | conditionText | conditionStatus |
| --- | --- | --- | --- | --- |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | not met | CourseChoiceCondition | One of CS 233, CS 240, CS 340 or ECE 391 | met |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | not met | CourseChoiceCondition | CS 374 or ECE 374 | UNMET / needs review |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | not met | CourseChoiceCondition | one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 | met |


# Q04_downstream_if_S002_completes_CS225

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ04 | courses that open up if S002 completes CS 225
# Features: BGP, OPTIONAL, BIND/IF with hypothetical fact, EXISTS, aggregation (MIN, GROUP_CONCAT, GROUP BY)
SELECT ?courseCode ?option (IF(MIN(?met) = 1, "would become satisfiable", "still blocked") AS ?status)
       (GROUP_CONCAT(?unmet; separator=" | ") AS ?stillRequired) WHERE {
  BIND(<student/S002> AS ?s) BIND(<course/CS225> AS ?added)
  ?course uca:hasPrerequisiteExpression/uca:hasOption ?opt ; uca:courseCode ?courseCode .
  ?opt uca:hasCondition ?k ; rdfs:label ?optLabel .
  FILTER EXISTS { ?opt uca:hasCondition/(uca:requiredCourse|uca:alternativeCourse) ?added }
  ?k uca:conditionSourceText ?text .
  OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
  OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
  OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
  OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
  BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
          IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?added }
             || EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }, 1, 0),
       IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
       IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?met)
  BIND(IF(?met = 0, ?text, ?none) AS ?unmet)
  BIND(STRAFTER(?optLabel, "prerequisite ") AS ?option)
  FILTER NOT EXISTS { ?s uca:hasCompletion/uca:completedCourse ?course }
}
GROUP BY ?courseCode ?option
ORDER BY ?status ?courseCode

```

| courseCode | option | status | stillRequired |
| --- | --- | --- | --- |
| CS 341 | option 1 | still blocked | CS 233 |
| CS 418 | option 1 | still blocked | One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| MATH 241 |
| CS 440 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 |
| CS 441 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, BIOE 310, MATH 362, MATH 461, MATH 463 or STAT 400 |
| CS 444 | option 1 | still blocked | MATH 241 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 |
| CS 445 | option 1 | still blocked | CS 225, MATH 225 |
| CS 446 | option 1 | still blocked | One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 |
| CS 447 | option 1 | still blocked | CS 374 or ECE 374 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 |
| CS 463 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 |
| CS 470 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 |
| CS 477 | option 1 | still blocked | one of CS 374, ECE 374 or MATH 414 |
| ADV 492 | option 1 | would become satisfiable |  |
| CS 210 | option 1 | would become satisfiable |  |
| CS 211 | option 1 | would become satisfiable |  |
| CS 233 | option 1 | would become satisfiable |  |
| CS 340 | option 1 | would become satisfiable |  |
| CS 374 | option 1 | would become satisfiable |  |
| CS 409 | option 1 | would become satisfiable |  |
| CS 410 | option 1 | would become satisfiable |  |
| CS 411 | option 1 | would become satisfiable |  |
| CS 412 | option 1 | would become satisfiable |  |
| CS 415 | option 1 | would become satisfiable |  |
| CS 452 | option 1 | would become satisfiable |  |
| CS 464 | option 1 | would become satisfiable |  |
| CS 465 | option 1 | would become satisfiable |  |
| CS 466 | option 1 | would become satisfiable |  |
| ECE 407 | option 1 | would become satisfiable |  |
| ECE 549 | option 1 | would become satisfiable |  |


# Q05_eligible_courses_for_unmet_requirements_S002

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ05 | eligible courses that serve S002's unmet requirement groups
# Features: UNION, subqueries, OPTIONAL, aggregation (COUNT, MIN, GROUP BY, HAVING), FILTER, property paths
SELECT DISTINCT ?courseCode ?requirement ?eligibilityBasis WHERE {
  {
    { SELECT ?course WHERE {
        BIND(<student/S002> AS ?s)
        ?course uca:hasPrerequisiteExpression/uca:hasOption ?option .
        ?option uca:hasCondition ?k .
        OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
        OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
        OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
        OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
        BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
                IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }
                   || EXISTS { ?k uca:allowsConcurrent true ; uca:requiredCourse|uca:alternativeCourse ?rc .
                               ?s uca:hasPlannedEnrollment/uca:plannedCourse ?rc }, 1, 0),
             IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
             IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?met)
      } GROUP BY ?course ?option HAVING (MIN(?met) = 1) }
    BIND("prerequisite option satisfied" AS ?eligibilityBasis)
  } UNION {
    ?course a uca:Course .
    FILTER NOT EXISTS { ?course uca:hasPrerequisiteExpression ?e }
    BIND("no recorded prerequisite" AS ?eligibilityBasis)
  }
  ?course uca:hasOffering/uca:offeredInTerm <term/2026-fa> ; uca:courseCode ?courseCode .
  FILTER NOT EXISTS { <student/S002> uca:hasCompletion/uca:completedCourse ?course }
  ?req uca:allowsCourse ?course ; rdfs:label ?requirement ; uca:minCourses ?minCourses .
  { SELECT ?req (COUNT(DISTINCT ?cp) AS ?allocated) WHERE {
      <program/UIUC-BS-CS-2026> uca:hasRequirement ?req .
      OPTIONAL { <student/S002> uca:hasCompletion ?cp . ?cp uca:allocatedToRequirement ?req }
    } GROUP BY ?req }
  FILTER(?allocated < ?minCourses)
}
ORDER BY ?requirement ?courseCode

```

| courseCode | requirement | eligibilityBasis |
| --- | --- | --- |
| AE 482 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ASRM 402 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ASRM 451 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ASRM 453 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 407 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 413 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 427 | Advanced electives (min 2 courses, 6 hours) | prerequisite option satisfied |
| CS 439 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 468 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 481 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 483 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 498 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 401 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 408 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 414 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 422 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 423 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 426 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 427 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 428 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 440 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 441 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 448 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CSE 485 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 410 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 414 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 415 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 419 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 422 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 424 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 428 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 435 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 438 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 448 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 449 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 478 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 491 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 493 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 494 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ECE 498 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| MATH 439 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| MATH 450 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| MATH 463 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| MATH 464 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| MATH 473 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| MATH 475 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| ME 445 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| PHIL 419 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| PHIL 420 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| PHYS 466 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| PHYS 496 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| STAT 400 | Advanced electives (min 2 courses, 6 hours) | prerequisite option satisfied |
| STAT 408 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| TAM 413 | Advanced electives (min 2 courses, 6 hours) | no recorded prerequisite |
| CS 225 | CS technical core (11 courses, 35 hours) | prerequisite option satisfied |
| CS 233 | CS technical core (11 courses, 35 hours) | prerequisite option satisfied |
| CS 361 | CS technical core (11 courses, 35 hours) | prerequisite option satisfied |
| CS 407 | Focus area: Algorithms and Models of Computation | no recorded prerequisite |
| CS 413 | Focus area: Algorithms and Models of Computation | no recorded prerequisite |
| CS 481 | Focus area: Algorithms and Models of Computation | no recorded prerequisite |
| CS 571 | Focus area: Algorithms and Models of Computation | no recorded prerequisite |
| CS 407 | Focus area: Distributed Systems, Networking, and Security | no recorded prerequisite |
| CS 439 | Focus area: Distributed Systems, Networking, and Security | no recorded prerequisite |
| CS 483 | Focus area: Distributed Systems, Networking, and Security | no recorded prerequisite |
| CS 468 | Focus area: Human and Social Impact | no recorded prerequisite |
| CS 543 | Focus area: Intelligence and Big Data | no recorded prerequisite |
| CS 468 | Focus area: Media | no recorded prerequisite |
| CS 483 | Focus area: Scientific, Parallel, and High Performance Computing | no recorded prerequisite |
| CS 556 | Focus area: Scientific, Parallel, and High Performance Computing | no recorded prerequisite |
| CS 407 | Focus area: Software Foundations | no recorded prerequisite |
| CS 427 | Focus area: Software Foundations | prerequisite option satisfied |
| MATH 241 | Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | prerequisite option satisfied |
| PHYS 212 | Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | prerequisite option satisfied |
| ACES 102 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ANSC 207 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ANTH 143 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ANTH 241 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ANTH 246 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ASTR 121 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ASTR 122 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ASTR 150 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ASTR 200 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ASTR 330 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ATMS 100 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ATMS 120 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ATMS 140 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| CPSC 112 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| CPSC 199 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ECE 101 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ESE 103 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ESE 117 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ESE 118 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ESE 120 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ESE 140 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ESE 143 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| ESE 208 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| FSHN 101 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| FSHN 120 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| GEOL 100 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| GEOL 117 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| GEOL 118 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| GEOL 143 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| GGIS 100 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| GGIS 103 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| GLBL 118 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| HDFS 143 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| HK 150 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| IB 100 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| IB 108 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| IB 110 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| IB 150 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| MCB 100 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| MSE 101 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| NRES 100 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| NRES 103 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| PHYS 212 | Science elective (one Natural Science & Technology course) | prerequisite option satisfied |
| SHS 280 | Science elective (one Natural Science & Technology course) | no recorded prerequisite |
| CS 427 | Team project course (at least 1 of the technical electives) | prerequisite option satisfied |
| CS 407 | Technical electives (min 6 courses, 18 hours) | no recorded prerequisite |
| CS 413 | Technical electives (min 6 courses, 18 hours) | no recorded prerequisite |
| CS 427 | Technical electives (min 6 courses, 18 hours) | prerequisite option satisfied |
| CS 439 | Technical electives (min 6 courses, 18 hours) | no recorded prerequisite |
| CS 468 | Technical electives (min 6 courses, 18 hours) | no recorded prerequisite |
| CS 481 | Technical electives (min 6 courses, 18 hours) | no recorded prerequisite |
| CS 483 | Technical electives (min 6 courses, 18 hours) | no recorded prerequisite |
| CS 498 | Technical electives (min 6 courses, 18 hours) | no recorded prerequisite |


# Q06_requirement_progress_S003

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ06 | S003 progress per requirement group
# Features: OPTIONAL (left join keeps groups with no allocation), aggregation (COUNT, SUM, GROUP BY)
SELECT ?requirement ?minCourses ?allocatedCourses ?remainingCourses ?minCredits ?allocatedCredits WHERE {
  <program/UIUC-BS-CS-2026> uca:hasRequirement ?req .
  ?req rdfs:label ?requirement .
  OPTIONAL { ?req uca:minCourses ?minCourses }
  OPTIONAL { ?req uca:minCredits ?minCredits }
  { SELECT ?req (COUNT(DISTINCT ?cp) AS ?allocatedCourses) (COALESCE(SUM(?cr), 0) AS ?allocatedCredits) WHERE {
      <program/UIUC-BS-CS-2026> uca:hasRequirement ?req .
      OPTIONAL { <student/S003> uca:hasCompletion ?cp . ?cp uca:allocatedToRequirement ?req ; uca:creditsEarned ?cr }
    } GROUP BY ?req }
  BIND(IF(BOUND(?minCourses), IF(?minCourses - ?allocatedCourses > 0, ?minCourses - ?allocatedCourses, 0), "n/a")
       AS ?remainingCourses)
}
ORDER BY DESC(?remainingCourses) ?requirement

```

| requirement | minCourses | allocatedCourses | remainingCourses | minCredits | allocatedCredits |
| --- | --- | --- | --- | --- | --- |
| Technical electives (min 6 courses, 18 hours) | 6 | 0 | 6 | 18.0 | 0 |
| CS technical core (11 courses, 35 hours) | 11 | 6 | 5 | 35.0 | 18.0 |
| Focus area: Algorithms and Models of Computation | 3 | 0 | 3 |  | 0 |
| Focus area: Distributed Systems, Networking, and Security | 3 | 0 | 3 |  | 0 |
| Focus area: Human and Social Impact | 3 | 0 | 3 |  | 0 |
| Focus area: Intelligence and Big Data | 3 | 0 | 3 |  | 0 |
| Focus area: Machines | 3 | 0 | 3 |  | 0 |
| Focus area: Media | 3 | 0 | 3 |  | 0 |
| Focus area: Scientific, Parallel, and High Performance Computing | 3 | 0 | 3 |  | 0 |
| Focus area: Software Foundations | 3 | 0 | 3 |  | 0 |
| Advanced electives (min 2 courses, 6 hours) | 2 | 0 | 2 | 6.0 | 0 |
| Ethical and professional issues: CS 210 or CS 211 | 1 | 0 | 1 | 2.0 | 0 |
| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | 4 | 3 | 1 | 15.0 | 11.0 |
| Science elective (one Natural Science & Technology course) | 1 | 0 | 1 | 3.0 | 0 |
| Team project course (at least 1 of the technical electives) | 1 | 0 | 1 |  | 0 |
| Calculus I: MATH 221 (MATH 220 may be substituted) | 1 | 1 | 0 | 4.0 | 4.0 |
| Linear algebra: MATH 257, MATH 415 or MATH 416 | 1 | 1 | 0 | 3.0 | 3.0 |
| Orientation: ENG 100 | 1 | 1 | 0 | 1.0 | 1.0 |


# Q07_upper_level_courses_needing_standing_or_consent

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ07 | 300/400-level CS/MATH/ECE/STAT courses needing standing or consent
# Features: BGP, VALUES, FILTER (numeric range, IN), property path, STRAFTER
SELECT DISTINCT ?courseCode ?title ?conditionType ?conditionText WHERE {
  VALUES ?type { uca:StandingCondition uca:ConsentCondition }
  ?course uca:courseNumber ?n ;
          uca:courseCode ?courseCode ;
          uca:courseTitle ?title ;
          uca:inDepartment/uca:subjectCode ?subject ;
          uca:hasOffering/uca:offeredInTerm <term/2026-fa> ;
          uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition ?k .
  ?k a ?type ; uca:conditionSourceText ?conditionText .
  FILTER(?n >= 300 && ?n < 500)
  FILTER(?subject IN ("CS", "MATH", "ECE", "STAT"))
  BIND(STRAFTER(STR(?type), "#") AS ?conditionType)
}
ORDER BY ?courseCode

```

| courseCode | title | conditionType | conditionText |
| --- | --- | --- | --- |
| CS 397 | Individual Study | ConsentCondition | Consent of instructor |
| CS 400 | Accelerated Fundamentals of Computing I | ConsentCondition | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| CS 401 | Accelerated Fundamentals of Algorithms I | ConsentCondition | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| CS 492 | Senior Project I | StandingCondition | For Computer Science majors with senior standing |
| CS 497 | CS Team Project | StandingCondition | junior or senior standing required |
| CS 499 | Senior Thesis | ConsentCondition | Consent of instructor |
| ECE 305 | Quantum Systems I | StandingCondition | junior standing |
| ECE 396 | Honors Project | ConsentCondition | Consent of instructor |
| ECE 397 | Individual Study in ECE | ConsentCondition | Consent of instructor |
| ECE 496 | Senior Research Project | ConsentCondition | consent of instructor |
| ECE 499 | Senior Thesis | ConsentCondition | consent of instructor |
| MATH 390 | Individual Study | ConsentCondition | Consent of instructor |
| MATH 402 | Non Euclidean Geometry | ConsentCondition | consent of instructor |
| MATH 403 | Euclidean Geometry | ConsentCondition | consent of instructor |
| MATH 405 | Teacher's Course | ConsentCondition | consent of instructor |
| MATH 415 | Applied Linear Algebra | ConsentCondition | consent of instructor |
| MATH 416 | Abstract Linear Algebra | ConsentCondition | consent of instructor |
| MATH 424 | Honors Real Analysis | ConsentCondition | consent of the department |
| MATH 427 | Honors Abstract Algebra | ConsentCondition | Consent of the department is required |
| MATH 447 | Real Variables | StandingCondition | junior standing |
| MATH 447 | Real Variables | ConsentCondition | consent of instructor |
| MATH 499 | Introduction Graduate Research | StandingCondition | Graduate standing |
| MATH 499 | Introduction Graduate Research | ConsentCondition | consent of instructor |
| STAT 390 | Individual Study | ConsentCondition | Consent of instructor |
| STAT 391 | Honors Individual Study | ConsentCondition | Consent of instructor |
| STAT 443 | Professional Statistics | ConsentCondition | consent of instructor |
| STAT 480 | Big Data Analytics | ConsentCondition | permission of the instructor |


# Q08_upstream_two_or_more_hops_CS440

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ08 | courses >= 2 prerequisite hops upstream of CS 440
# Features: property path one-or-more (+) after an explicit first hop (= 2+ hops), alternative paths
SELECT DISTINCT ?upstreamCode ?viaCode ?firstHop WHERE {
  <course/CS440> uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition ?k1 .
  ?k1 uca:requiredCourse|uca:alternativeCourse ?via .
  ?via (uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition/(uca:requiredCourse|uca:alternativeCourse))+ ?up .
  BIND(IF(EXISTS { ?k1 a uca:CourseChoiceCondition }, "via one-of group (potential)", "via required course") AS ?firstHop)
  ?up uca:courseCode ?upstreamCode .
  ?via uca:courseCode ?viaCode .
  FILTER(?up != <course/CS440> && ?up != ?via)
}
ORDER BY ?upstreamCode ?viaCode

```

| upstreamCode | viaCode | firstHop |
| --- | --- | --- |
| BIOE 210 | BIOE 310 | via one-of group (potential) |
| CS 101 | BIOE 310 | via one-of group (potential) |
| CS 101 | ECE 313 | via one-of group (potential) |
| CS 124 | BIOE 310 | via one-of group (potential) |
| CS 124 | CS 225 | via required course |
| CS 125 | CS 225 | via required course |
| CS 126 | CS 225 | via required course |
| CS 128 | CS 225 | via required course |
| CS 173 | CS 225 | via required course |
| CS 374 | CS 225 | via required course |
| CS 413 | CS 225 | via required course |
| ECE 120 | CS 225 | via required course |
| ECE 220 | CS 225 | via required course |
| MATH 112 | BIOE 310 | via one-of group (potential) |
| MATH 112 | CS 225 | via required course |
| MATH 112 | CS 361 | via one-of group (potential) |
| MATH 112 | ECE 313 | via one-of group (potential) |
| MATH 112 | MATH 461 | via one-of group (potential) |
| MATH 112 | STAT 400 | via one-of group (potential) |
| MATH 115 | BIOE 310 | via one-of group (potential) |
| MATH 115 | CS 225 | via required course |
| MATH 115 | CS 361 | via one-of group (potential) |
| MATH 115 | ECE 313 | via one-of group (potential) |
| MATH 115 | MATH 461 | via one-of group (potential) |
| MATH 115 | STAT 400 | via one-of group (potential) |
| MATH 213 | CS 225 | via required course |
| MATH 220 | BIOE 310 | via one-of group (potential) |
| MATH 220 | CS 225 | via required course |
| MATH 220 | CS 361 | via one-of group (potential) |
| MATH 220 | ECE 313 | via one-of group (potential) |
| MATH 220 | MATH 461 | via one-of group (potential) |
| MATH 220 | STAT 400 | via one-of group (potential) |
| MATH 221 | BIOE 310 | via one-of group (potential) |
| MATH 221 | CS 225 | via required course |
| MATH 221 | CS 361 | via one-of group (potential) |
| MATH 221 | ECE 313 | via one-of group (potential) |
| MATH 221 | MATH 461 | via one-of group (potential) |
| MATH 221 | STAT 400 | via one-of group (potential) |
| MATH 231 | BIOE 310 | via one-of group (potential) |
| MATH 231 | CS 225 | via required course |
| MATH 231 | ECE 313 | via one-of group (potential) |
| MATH 231 | MATH 461 | via one-of group (potential) |
| MATH 231 | STAT 400 | via one-of group (potential) |
| MATH 241 | BIOE 310 | via one-of group (potential) |
| MATH 241 | CS 225 | via required course |
| MATH 241 | ECE 313 | via one-of group (potential) |
| MATH 241 | MATH 461 | via one-of group (potential) |
| MATH 257 | BIOE 310 | via one-of group (potential) |
| MATH 257 | ECE 313 | via one-of group (potential) |
| MATH 314 | CS 225 | via required course |
| MATH 314 | ECE 313 | via one-of group (potential) |
| MATH 347 | CS 225 | via required course |
| MATH 347 | ECE 313 | via one-of group (potential) |
| MATH 412 | CS 225 | via required course |
| MATH 413 | CS 225 | via required course |
| MATH 416 | ECE 313 | via one-of group (potential) |


# Q09_requirement_groups_with_multiple_choices

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ09 | requirement groups with more than one allowed course
# Features: BGP, OPTIONAL, aggregation (COUNT DISTINCT, GROUP BY, HAVING), BIND/IF
SELECT ?requirement (COUNT(DISTINCT ?course) AS ?allowedCourses)
       (COUNT(DISTINCT ?offered) AS ?offeredFall2026) WHERE {
  <program/UIUC-BS-CS-2026> uca:hasRequirement ?req .
  ?req rdfs:label ?requirement ; uca:allowsCourse ?course .
  OPTIONAL { ?course uca:hasOffering/uca:offeredInTerm <term/2026-fa> . BIND(?course AS ?offered) }
}
GROUP BY ?requirement
HAVING (COUNT(DISTINCT ?course) > 1)
ORDER BY DESC(?allowedCourses)

```

| requirement | allowedCourses | offeredFall2026 |
| --- | --- | --- |
| Advanced electives (min 2 courses, 6 hours) | 225 | 192 |
| Technical electives (min 6 courses, 18 hours) | 66 | 47 |
| Science elective (one Natural Science & Technology course) | 53 | 53 |
| Focus area: Intelligence and Big Data | 34 | 21 |
| Focus area: Distributed Systems, Networking, and Security | 23 | 17 |
| Focus area: Algorithms and Models of Computation | 21 | 11 |
| Focus area: Human and Social Impact | 21 | 15 |
| Focus area: Software Foundations | 19 | 10 |
| Focus area: Media | 17 | 10 |
| Focus area: Machines | 16 | 6 |
| Team project course (at least 1 of the technical electives) | 13 | 8 |
| Focus area: Scientific, Parallel, and High Performance Computing | 12 | 5 |
| CS technical core (11 courses, 35 hours) | 11 | 11 |
| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | 4 | 4 |
| Linear algebra: MATH 257, MATH 415 or MATH 416 | 3 | 3 |
| Calculus I: MATH 221 (MATH 220 may be substituted) | 2 | 2 |
| Ethical and professional issues: CS 210 or CS 211 | 2 | 2 |


# Q10_crosslisted_aliases_and_downstream_CS374

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ10 | CS 374 cross-listings and dependent courses
# Features: property paths (alternative + inverse ^), FILTER IN, EXISTS, OPTIONAL, aggregation (GROUP_CONCAT)
SELECT ?alias ?downstreamCode (GROUP_CONCAT(DISTINCT ?mentionedCode; separator=", ") AS ?mentions)
       (MAX(?both) AS ?acceptsBothCodes) WHERE {
  BIND(<course/CS374> AS ?c)
  ?c uca:crossListedWith|^uca:crossListedWith ?aliasC .
  ?aliasC uca:courseCode ?alias .
  ?down uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition ?k ; uca:courseCode ?downstreamCode .
  ?k uca:requiredCourse|uca:alternativeCourse ?m .
  FILTER(?m IN (?c, ?aliasC))
  ?m uca:courseCode ?mentionedCode .
  BIND(EXISTS { ?k uca:alternativeCourse ?c . ?k uca:alternativeCourse ?aliasC } AS ?both)
}
GROUP BY ?alias ?downstreamCode
ORDER BY ?downstreamCode

```

| alias | downstreamCode | mentions | acceptsBothCodes |
| --- | --- | --- | --- |
| ECE 374 | CS 421 | CS 374, ECE 374 | true |
| ECE 374 | CS 447 | CS 374, ECE 374 | true |
| ECE 374 | CS 473 | CS 374, ECE 374 | true |
| ECE 374 | CS 475 | CS 374, ECE 374 | true |
| ECE 374 | CS 477 | CS 374, ECE 374 | true |
| ECE 374 | CS 521 | CS 374, ECE 374 | true |
| ECE 374 | CS 581 | CS 374, ECE 374 | true |
| ECE 374 | MATH 412 | CS 374 | false |
| ECE 374 | MATH 417 | CS 374 | false |


# Q11_department_counts_for_advanced_electives_INFERENCE

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ11 | per department: advanced electives offered Fall 2026 [needs reasoning]
# Features: aggregation (COUNT, GROUP BY), ORDER BY DESC, multi-hop over INFERRED properties
SELECT ?department (COUNT(DISTINCT ?course) AS ?advancedElectivesOfferedFall2026) WHERE {
  ?dept uca:hasCourse ?course ; uca:subjectCode ?department .
  ?course uca:maySatisfyRequirement <requirement/UIUC-BS-CS-2026/Elective-Advanced> ;
          uca:scheduledInTerm <term/2026-fa> .
}
GROUP BY ?department
ORDER BY DESC(?advancedElectivesOfferedFall2026) ?department

```

| department | advancedElectivesOfferedFall2026 |
| --- | --- |
| CS | 50 |
| ECE | 46 |
| MATH | 30 |
| STAT | 19 |
| PHYS | 17 |
| CSE | 12 |
| ASRM | 5 |
| PHIL | 3 |
| BIOE | 2 |
| MSE | 2 |
| ADV | 1 |
| AE | 1 |
| IE | 1 |
| ME | 1 |
| NE | 1 |
| TAM | 1 |


# Q12_blocked_only_by_noncourse_conditions

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ12 | courses blocked only by standing/consent
# Features: nested subqueries (two-level aggregation), SUM/MAX/GROUP_CONCAT, HAVING, FILTER EXISTS / NOT EXISTS
SELECT ?studentId ?courseCode (GROUP_CONCAT(?blocking; separator=" | ") AS ?blockingConditions) WHERE {
  { SELECT ?s ?course ?option (SUM(?uc) AS ?unmetCourse) (SUM(?un) AS ?unmetNonCourse) (SUM(?ot) AS ?other)
           (GROUP_CONCAT(?ntext; separator=" | ") AS ?nonCourseText) WHERE {
      ?s a uca:Student .
      ?course uca:hasOffering/uca:offeredInTerm <term/2026-fa> ;
              uca:hasPrerequisiteExpression/uca:hasOption ?option .
      FILTER EXISTS { ?req uca:allowsCourse ?course }
      FILTER NOT EXISTS { ?s uca:hasCompletion/uca:completedCourse ?course }
      ?option uca:hasCondition ?k .
      ?k uca:conditionSourceText ?text .
      OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
      OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
      OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
      OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
      BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
              IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }
                 || EXISTS { ?k uca:allowsConcurrent true ; uca:requiredCourse|uca:alternativeCourse ?rc .
                             ?s uca:hasPlannedEnrollment/uca:plannedCourse ?rc }, 1, 0),
           IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
           IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?met)
      BIND(IF((BOUND(?isCourse) || BOUND(?isChoice)) && ?met = 0, 1, 0) AS ?uc)
      BIND(IF((BOUND(?isStanding) || BOUND(?isConsent)) && ?met = 0, 1, 0) AS ?un)
      BIND(IF(!BOUND(?isCourse) && !BOUND(?isChoice) && !BOUND(?isStanding) && !BOUND(?isConsent), 1, 0) AS ?ot)
      BIND(IF((BOUND(?isStanding) || BOUND(?isConsent)) && ?met = 0, ?text, ?none) AS ?ntext)
    } GROUP BY ?s ?course ?option }
  BIND(IF(?unmetCourse = 0 && ?unmetNonCourse > 0 && ?other = 0, ?nonCourseText, ?none) AS ?blocking)
  BIND(IF(?unmetCourse + ?unmetNonCourse + ?other = 0, 1, 0) AS ?fullyMet)
  BIND(IF(?unmetCourse = 0 && ?unmetNonCourse > 0 && ?other = 0, 1, 0) AS ?onlyNonCourse)
  ?s uca:studentIdentifier ?studentId .
  ?course uca:courseCode ?courseCode .
}
GROUP BY ?studentId ?courseCode
HAVING (MAX(?fullyMet) = 0 && MAX(?onlyNonCourse) = 1)
ORDER BY ?studentId ?courseCode

```

| studentId | courseCode | blockingConditions |
| --- | --- | --- |
| S001 | ASRM 406 | consent of instructor |
| S001 | CS 397 | Consent of instructor |
| S001 | CS 400 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S001 | CS 401 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S001 | CS 492 | For Computer Science majors with senior standing |
| S001 | CS 499 | Consent of instructor |
| S001 | CS 567 | permission of instructor |
| S001 | CS 581 | consent of instructor |
| S001 | CS 582 | consent of instructor |
| S001 | GEOL 208 | consent of instructor |
| S001 | LA 250 | consent of instructor |
| S001 | MATH 402 | consent of instructor |
| S001 | MATH 403 | consent of instructor |
| S001 | MATH 405 | consent of instructor |
| S001 | MATH 415 | consent of instructor |
| S001 | MATH 416 | consent of instructor |
| S001 | MATH 427 | Consent of the department is required |
| S001 | MATH 447 | consent of instructor |
| S001 | MATH 499 | Graduate standing \| consent of instructor |
| S001 | PHYS 497 | Consent of instructor |
| S001 | STAT 443 | consent of instructor |
| S001 | STAT 480 | permission of the instructor |
| S002 | ASRM 406 | consent of instructor |
| S002 | CS 397 | Consent of instructor |
| S002 | CS 400 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S002 | CS 401 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S002 | CS 492 | For Computer Science majors with senior standing |
| S002 | CS 499 | Consent of instructor |
| S002 | CS 567 | permission of instructor |
| S002 | CS 581 | consent of instructor |
| S002 | CS 582 | consent of instructor |
| S002 | GEOL 208 | consent of instructor |
| S002 | LA 250 | consent of instructor |
| S002 | MATH 402 | consent of instructor |
| S002 | MATH 403 | consent of instructor |
| S002 | MATH 405 | consent of instructor |
| S002 | MATH 415 | consent of instructor |
| S002 | MATH 416 | consent of instructor |
| S002 | MATH 427 | Consent of the department is required |
| S002 | MATH 447 | consent of instructor |
| S002 | MATH 499 | Graduate standing \| consent of instructor |
| S002 | PHYS 497 | Consent of instructor |
| S002 | STAT 443 | consent of instructor |
| S002 | STAT 480 | permission of the instructor |
| S003 | ASRM 406 | consent of instructor |
| S003 | CS 400 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S003 | CS 401 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S003 | CS 492 | For Computer Science majors with senior standing |
| S003 | CS 499 | Consent of instructor |
| S003 | CS 567 | permission of instructor |
| S003 | CS 581 | consent of instructor |
| S003 | CS 582 | consent of instructor |
| S003 | GEOL 208 | consent of instructor |
| S003 | LA 250 | consent of instructor |
| S003 | MATH 402 | consent of instructor |
| S003 | MATH 403 | consent of instructor |
| S003 | MATH 405 | consent of instructor |
| S003 | MATH 416 | consent of instructor |
| S003 | MATH 427 | Consent of the department is required |
| S003 | MATH 447 | consent of instructor |
| S003 | MATH 499 | Graduate standing \| consent of instructor |
| S003 | PHYS 497 | Consent of instructor |
| S003 | STAT 443 | consent of instructor |
| S003 | STAT 480 | permission of the instructor |
| S004 | ASRM 406 | consent of instructor |
| S004 | CS 397 | Consent of instructor |
| S004 | CS 400 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S004 | CS 401 | Current enrollment in the Illinois Computing Accelerator for Non-specialists (iCAN) program or consent of instructor |
| S004 | CS 499 | Consent of instructor |
| S004 | CS 567 | permission of instructor |
| S004 | CS 582 | consent of instructor |
| S004 | GEOL 208 | consent of instructor |
| S004 | LA 250 | consent of instructor |
| S004 | MATH 402 | consent of instructor |
| S004 | MATH 403 | consent of instructor |
| S004 | MATH 405 | consent of instructor |
| S004 | MATH 416 | consent of instructor |
| S004 | MATH 427 | Consent of the department is required |
| S004 | MATH 447 | consent of instructor |
| S004 | MATH 499 | Graduate standing \| consent of instructor |
| S004 | PHYS 497 | Consent of instructor |
| S004 | STAT 443 | consent of instructor |
| S004 | STAT 480 | permission of the instructor |


# Q13_what_if_S002_adds_CS225

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ13 | what-if: courses eligible only after adding CS 225 (S002)
# Features: VALUES (scenarios), subquery, EXISTS, aggregation (COUNT, SAMPLE, GROUP_CONCAT, HAVING)
SELECT ?courseCode ?title (GROUP_CONCAT(DISTINCT ?scenario; separator=", ") AS ?eligibleIn) WHERE {
  { SELECT ?scenario ?course ?option WHERE {
      VALUES ?scenario { "baseline" "plus CS 225" }
      BIND(<student/S002> AS ?s)
      ?course uca:hasPrerequisiteExpression/uca:hasOption ?option .
      ?option uca:hasCondition ?k .
      OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
      OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
      OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
      OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
      BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
              IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }
                 || (?scenario = "plus CS 225" && EXISTS { ?k uca:requiredCourse|uca:alternativeCourse <course/CS225> }), 1, 0),
           IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
           IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?met)
    } GROUP BY ?scenario ?course ?option HAVING (MIN(?met) = 1) }
  ?course uca:courseCode ?courseCode .
  OPTIONAL { ?course uca:courseTitle ?title }
  FILTER NOT EXISTS { <student/S002> uca:hasCompletion/uca:completedCourse ?course }
  FILTER(?course != <course/CS225>)
}
GROUP BY ?courseCode ?title
HAVING (COUNT(DISTINCT ?scenario) = 1 && SAMPLE(?scenario) = "plus CS 225")
ORDER BY ?courseCode

```

| courseCode | title | eligibleIn |
| --- | --- | --- |
| ADV 492 | Tech and Advertising Campaigns | plus CS 225 |
| CS 210 | Ethical & Professional Issues | plus CS 225 |
| CS 211 | Ethical and Professional Conduct | plus CS 225 |
| CS 233 | Computer Architecture | plus CS 225 |
| CS 340 | Introduction to Computer Systems | plus CS 225 |
| CS 374 | Introduction to Algorithms & Models of Computation | plus CS 225 |
| CS 409 | The Art of Web Programming | plus CS 225 |
| CS 410 | Text Information Systems | plus CS 225 |
| CS 411 | Database Systems | plus CS 225 |
| CS 412 | Introduction to Data Mining | plus CS 225 |
| CS 415 | Game Development | plus CS 225 |
| CS 452 | Topics in Robotics | plus CS 225 |
| CS 464 | Topics in Societal and Ethical Impacts of Computer Technology | plus CS 225 |
| CS 465 | User Interface Design | plus CS 225 |
| CS 466 | Introduction to Bioinformatics | plus CS 225 |
| ECE 407 | Cryptography | plus CS 225 |
| ECE 549 | Computer Vision | plus CS 225 |


# Q14_multi_group_completions_and_double_counting_S004

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ14 | S004 courses fitting several groups + double-count check
# Features: BGP, OPTIONAL, EXISTS, aggregation (COUNT DISTINCT, GROUP_CONCAT, GROUP BY, HAVING)
SELECT ?courseCode (COUNT(DISTINCT ?req) AS ?candidateGroups)
       (GROUP_CONCAT(DISTINCT ?reqLabel; separator=" | ") AS ?couldCountToward)
       ?allocatedTo ?violatesDistinctRule WHERE {
  <student/S004> uca:hasCompletion ?cp .
  ?cp uca:completedCourse ?course .
  ?course uca:courseCode ?courseCode .
  ?req uca:allowsCourse ?course ; rdfs:label ?reqLabel .
  OPTIONAL { SELECT ?cp (GROUP_CONCAT(?al; separator=" | ") AS ?alloc) WHERE {
      ?cp uca:allocatedToRequirement ?a . ?a rdfs:label ?al } GROUP BY ?cp }
  BIND(COALESCE(?alloc, "(not allocated)") AS ?allocatedTo)
  BIND(EXISTS { ?cp uca:allocatedToRequirement <requirement/UIUC-BS-CS-2026/Elective-Technical> ,
                                               <requirement/UIUC-BS-CS-2026/Elective-Advanced> } AS ?violatesDistinctRule)
}
GROUP BY ?courseCode ?allocatedTo ?violatesDistinctRule
HAVING (COUNT(DISTINCT ?req) > 1)
ORDER BY DESC(?violatesDistinctRule) DESC(?candidateGroups) ?courseCode

```

| courseCode | candidateGroups | couldCountToward | allocatedTo | violatesDistinctRule |
| --- | --- | --- | --- | --- |
| CS 411 | 4 | Focus area: Intelligence and Big Data \| Team project course (at least 1 of the technical electives) \| Advanced electives (min 2 courses, 6 hours) \| Technical electives (min 6 courses, 18 hours) | Advanced electives (min 2 courses, 6 hours) \| Technical electives (min 6 courses, 18 hours) | true |
| CS 440 | 3 | Focus area: Intelligence and Big Data \| Advanced electives (min 2 courses, 6 hours) \| Technical electives (min 6 courses, 18 hours) | Technical electives (min 6 courses, 18 hours) | false |
| PHYS 211 | 2 | Science elective (one Natural Science & Technology course) \| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | false |
| PHYS 212 | 2 | Science elective (one Natural Science & Technology course) \| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | false |


# Q15_evidence_for_S002_planned_courses

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# CQ15 | evidence for S002's planned courses
# Features: OPTIONAL (several), subquery with aggregation, BIND/IF/COALESCE, EXISTS
SELECT ?courseCode ?prerequisiteText ?parseStatus ?satisfiedOptions ?requirement ?requirementNote ?source ?unverified WHERE {
  <student/S002> uca:hasPlannedEnrollment/uca:plannedCourse ?course .
  ?course uca:courseCode ?courseCode .
  OPTIONAL { ?course uca:hasPrerequisiteExpression ?e .
             ?e uca:prerequisiteSourceText ?prerequisiteText ; uca:parseStatus ?parseStatus }
  OPTIONAL { ?req uca:allowsCourse ?course ; rdfs:label ?requirement .
             OPTIONAL { ?req uca:requirementNote ?requirementNote } }
  OPTIONAL { ?course uca:sourceURL ?source }
  OPTIONAL { SELECT ?course (COUNT(DISTINCT ?option) AS ?sat) WHERE {
      { SELECT ?course ?option WHERE {
          BIND(<student/S002> AS ?s)
          ?s uca:hasPlannedEnrollment/uca:plannedCourse ?course .
          ?course uca:hasPrerequisiteExpression/uca:hasOption ?option .
          ?option uca:hasCondition ?k .
          OPTIONAL { ?k a uca:CourseCondition . BIND(true AS ?isCourse) }
          OPTIONAL { ?k a uca:CourseChoiceCondition . BIND(true AS ?isChoice) }
          OPTIONAL { ?k a uca:StandingCondition ; uca:minimumStandingRank ?min . BIND(true AS ?isStanding) }
          OPTIONAL { ?k a uca:ConsentCondition . BIND(true AS ?isConsent) }
          BIND(IF(BOUND(?isCourse) || BOUND(?isChoice),
                  IF(EXISTS { ?k uca:requiredCourse|uca:alternativeCourse ?rc . ?s uca:hasCompletion/uca:completedCourse ?rc }, 1, 0),
               IF(BOUND(?isStanding), IF(EXISTS { ?s uca:standingRank ?r . FILTER(?r >= ?min) }, 1, 0),
               IF(BOUND(?isConsent), IF(EXISTS { ?s uca:hasPermissionFor ?course }, 1, 0), 0))) AS ?met)
        } GROUP BY ?course ?option HAVING (MIN(?met) = 1) }
    } GROUP BY ?course }
  BIND(COALESCE(?sat, 0) AS ?satisfiedOptions)
  BIND(IF(EXISTS { ?course uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition ?o . ?o a uca:OtherCondition },
          "yes: free-text condition needs manual check",
       IF(COALESCE(?parseStatus = "needs_review", false),
          "yes: wording such as 'or equivalent' needs manual check", "none")) AS ?unverified)
}
ORDER BY ?courseCode ?requirement

```

| courseCode | prerequisiteText | parseStatus | satisfiedOptions | requirement | requirementNote | source | unverified |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CS 225 | CS 126 or CS 128 or ECE 220; One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413. | parsed | 1 | CS technical core (11 courses, 35 hours) | Technical GPA of 2.0 is required for CS and Math courses. | https://discovery.cs.illinois.edu/dataset/course-catalog/ | none |
| MATH 241 | MATH 231. | parsed | 1 | Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 |  | https://discovery.cs.illinois.edu/dataset/course-catalog/ | none |
| MATH 257 | MATH 220 or MATH 221; CS 101 or equivalent programming experience. | needs_review | 0 | Linear algebra: MATH 257, MATH 415 or MATH 416 |  | https://discovery.cs.illinois.edu/dataset/course-catalog/ | yes: wording such as 'or equivalent' needs manual check |


# INF1_inverse_department_hasCourse

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# Inference: inverse (department hasCourse) [needs reasoning]
# Features: BGP, inference-dependent
SELECT ?courseCode ?title WHERE {
  <department/CS> uca:hasCourse ?course .
  ?course uca:courseCode ?courseCode .
  OPTIONAL { ?course uca:courseTitle ?title }
}
ORDER BY ?courseCode

```

| courseCode | title |
| --- | --- |
| CS 100 | Computer Science Orientation |
| CS 101 | Intro Computing: Engrg & Sci |
| CS 105 | Intro Computing: Non-Tech |
| CS 107 | Data Science Discovery |
| CS 124 | Introduction to Computer Science I |
| CS 125 |  |
| CS 126 |  |
| CS 128 | Introduction to Computer Science II |
| CS 173 | Discrete Structures |
| CS 199 | Undergraduate Open Seminar in Computer Science |
| CS 210 | Ethical & Professional Issues |
| CS 211 | Ethical and Professional Conduct |
| CS 222 | Software Design Lab |
| CS 225 | Data Structures |
| CS 233 | Computer Architecture |
| CS 240 |  |
| CS 241 |  |
| CS 277 | Algorithms and Data Structures for Data Science |
| CS 307 | Modeling and Learning in Data Science |
| CS 340 | Introduction to Computer Systems |
| CS 341 | System Programming |
| CS 357 | Numerical Methods I |
| CS 361 | Probability & Statistics for Computer Science |
| CS 374 | Introduction to Algorithms & Models of Computation |
| CS 397 | Individual Study |
| CS 400 | Accelerated Fundamentals of Computing I |
| CS 401 | Accelerated Fundamentals of Algorithms I |
| CS 407 | Cryptography |
| CS 409 | The Art of Web Programming |
| CS 410 | Text Information Systems |
| CS 411 | Database Systems |
| CS 412 | Introduction to Data Mining |
| CS 413 | Intro to Combinatorics |
| CS 414 |  |
| CS 415 | Game Development |
| CS 416 |  |
| CS 417 | Introduction to Extended Reality |
| CS 418 | Interactive Computer Graphics |
| CS 419 |  |
| CS 421 | Programming Languages & Compilers |
| CS 422 | Programming Language Design |
| CS 423 | Operating Systems Design |
| CS 424 | Real-Time Systems |
| CS 425 | Distributed Systems |
| CS 426 | Compiler Construction |
| CS 427 | Software Engineering I |
| CS 428 |  |
| CS 429 |  |
| CS 431 |  |
| CS 433 | Computer System Organization |
| CS 434 |  |
| CS 435 |  |
| CS 436 |  |
| CS 437 | Topics in Internet of Things |
| CS 438 | Communication Networks |
| CS 439 | Wireless Networks |
| CS 440 | Artificial Intelligence |
| CS 441 | Applied Machine Learning |
| CS 442 |  |
| CS 443 |  |
| CS 444 | Deep Learning for Computer Vision |
| CS 445 | Computational Photography |
| CS 446 | Machine Learning |
| CS 447 | Natural Language Processing |
| CS 448 |  |
| CS 450 | Numerical Analysis |
| CS 452 | Topics in Robotics |
| CS 460 | Security Laboratory |
| CS 461 | Computer Security I |
| CS 463 | Computer Security II |
| CS 464 | Topics in Societal and Ethical Impacts of Computer Technology |
| CS 465 | User Interface Design |
| CS 466 | Introduction to Bioinformatics |
| CS 467 |  |
| CS 468 | Tech and Advertising Campaigns |
| CS 469 |  |
| CS 470 | Social and Information Networks |
| CS 473 | Algorithms |
| CS 474 |  |
| CS 475 | Formal Models of Computation |
| CS 476 |  |
| CS 477 | Formal Software Development Methods |
| CS 481 | Advanced Topics in Stochastic Processes & Applications |
| CS 482 |  |
| CS 483 | Applied Parallel Programming |
| CS 484 | Parallel Programming |
| CS 491 | Seminar |
| CS 492 | Senior Project I |
| CS 493 |  |
| CS 494 |  |
| CS 497 | CS Team Project |
| CS 498 | Special Topics |
| CS 499 | Senior Thesis |
| CS 500 |  |
| CS 507 | Topics in Cryptography |
| CS 510 |  |
| CS 511 | Advanced Data Management |
| CS 512 | Data Mining Principles |
| CS 514 |  |
| CS 519 |  |
| CS 521 | Advanced Topics in Programming Systems |
| CS 522 |  |
| CS 523 |  |
| CS 524 | Concurrent Progrmg Languages |
| CS 525 |  |
| CS 526 |  |
| CS 527 | Topics in Software Engineering |
| CS 533 |  |
| CS 534 |  |
| CS 536 |  |
| CS 537 | Advanced Topics in Internet of Things (IoT) |
| CS 538 | Advanced Computer Networks |
| CS 539 |  |
| CS 540 |  |
| CS 541 |  |
| CS 542 | Statistical Reinforcement Learning |
| CS 543 | Computer Vision |
| CS 544 |  |
| CS 545 | Machine Learning for Signal Processing |
| CS 546 | Advanced Topics in Natural Language Processing |
| CS 547 | Deep Learning |
| CS 549 | Seminar in Cognitive Science |
| CS 554 |  |
| CS 555 |  |
| CS 556 | Iterative & Multigrid Methods |
| CS 558 |  |
| CS 562 | Advanced Topics in Security, Privacy, and Machine Learning |
| CS 563 | Advanced Computer Security |
| CS 565 | Human-Computer Interaction |
| CS 567 | Social Signals and Social Media |
| CS 571 | Combinatorial Mathematics |
| CS 572 |  |
| CS 574 | Randomized Algorithms |
| CS 575 |  |
| CS 576 |  |
| CS 579 | Computational Complexity |
| CS 580 | Topics in Algorithmic Game Theory |
| CS 581 | Algorithmic Genomic Biology |
| CS 582 | Machine Learning for Bioinformatics |
| CS 583 |  |
| CS 584 |  |
| CS 586 |  |
| CS 588 |  |
| CS 591 | Advanced Seminar |
| CS 597 | Individual Study |
| CS 598 | Special Topics |


# INF2_property_chain_and_transitivity_CS421

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# Inference: property chain + transitivity (CS 421 prerequisite path) [needs reasoning]
# Features: BGP over inferred transitive property, OPTIONAL, BIND/EXISTS
SELECT ?prereqCode ?direct WHERE {
  <course/CS421> uca:hasPrerequisitePath ?p .
  ?p uca:courseCode ?prereqCode .
  BIND(EXISTS { <course/CS421> uca:hasPrerequisiteCandidate ?p } AS ?direct)
}
ORDER BY DESC(?direct) ?prereqCode

```

| prereqCode | direct |
| --- | --- |
| ASRM 406 | true |
| BIOE 210 | true |
| CS 233 | true |
| CS 240 | true |
| CS 340 | true |
| CS 374 | true |
| ECE 374 | true |
| ECE 391 | true |
| MATH 225 | true |
| MATH 257 | true |
| MATH 415 | true |
| MATH 416 | true |
| ASRM 210 | false |
| CS 101 | false |
| CS 124 | false |
| CS 125 | false |
| CS 126 | false |
| CS 128 | false |
| CS 173 | false |
| CS 225 | false |
| CS 413 | false |
| ECE 120 | false |
| ECE 220 | false |
| ECON 102 | false |
| ECON 103 | false |
| FIN 221 | false |
| MATH 112 | false |
| MATH 115 | false |
| MATH 210 | false |
| MATH 213 | false |
| MATH 220 | false |
| MATH 221 | false |
| MATH 231 | false |
| MATH 241 | false |
| MATH 314 | false |
| MATH 347 | false |
| MATH 412 | false |
| MATH 413 | false |


# INF3_property_chain_hasCompletedCourse

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# Inference: property chain (student hasCompletedCourse) [needs reasoning]
# Features: BGP, aggregation (COUNT, GROUP BY)
SELECT ?studentId (COUNT(DISTINCT ?course) AS ?completedCourses)
       (GROUP_CONCAT(DISTINCT ?code; separator=", ") AS ?courses) WHERE {
  ?s uca:hasCompletedCourse ?course ; uca:studentIdentifier ?studentId .
  ?course uca:courseCode ?code .
}
GROUP BY ?studentId
ORDER BY ?studentId

```

| studentId | completedCourses | courses |
| --- | --- | --- |
| S001 | 5 | MATH 221, CS 124, MATH 231, CS 128, ENG 100 |
| S002 | 8 | MATH 221, CS 222, CS 124, CS 173, MATH 231, PHYS 211, CS 128, ENG 100 |
| S003 | 12 | MATH 221, CS 222, MATH 257, CS 124, CS 173, MATH 231, CS 233, PHYS 211, CS 128, ENG 100, CS 225, MATH 241 |
| S004 | 21 | MATH 221, CS 357, CS 222, MATH 257, CS 124, CS 173, MATH 231, CS 233, PHYS 211, CS 210, CS 128, ENG 100, CS 411, CS 341, STAT 400, CS 225, MATH 241, CS 361, CS 440, CS 374, PHYS 212 |


# INF4_symmetric_crosslisting

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# Inference: symmetric (crossListedWith) [needs reasoning]
# Features: BGP, FILTER (NOT IN). Lists links FROM courses outside the five parsed subjects TO CS courses.
SELECT ?courseCode ?crossListedWithCode WHERE {
  ?c uca:crossListedWith ?x ; uca:inDepartment/uca:subjectCode ?subj ; uca:courseCode ?courseCode .
  ?x uca:courseCode ?crossListedWithCode ; uca:inDepartment/uca:subjectCode ?xsubj .
  FILTER(?subj NOT IN ("CS", "ECE", "MATH", "STAT", "PHYS"))
  FILTER(?xsubj = "CS")
}
ORDER BY ?courseCode

```

| courseCode | crossListedWithCode |
| --- | --- |
| ADV 492 | CS 468 |
| ANTH 514 | CS 549 |
| CSE 401 | CS 450 |
| CSE 408 | CS 483 |
| CSE 414 | CS 473 |
| CSE 422 | CS 433 |
| CSE 423 | CS 423 |
| CSE 426 | CS 427 |
| CSE 427 | CS 418 |
| CSE 511 | CS 556 |
| EPSY 551 | CS 549 |
| IE 410 | CS 481 |
| IE 534 | CS 547 |
| IS 107 | CS 107 |
| LING 570 | CS 549 |
| PHIL 514 | CS 549 |
| PSYC 514 | CS 549 |


# INF5_class_inference_subclass_and_equivalentClass

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# Inference: subClassOf + equivalentClass [needs reasoning]
# Features: VALUES, aggregation (COUNT, GROUP BY), OPTIONAL
SELECT ?class (COUNT(DISTINCT ?x) AS ?instances) WHERE {
  VALUES ?class { uca:DegreeRequirement uca:PrerequisiteCondition uca:CourseWithPrerequisites }
  OPTIONAL { ?x a ?class }
}
GROUP BY ?class
ORDER BY ?class

```

| class | instances |
| --- | --- |
| https://example.org/uiuc-course-advisor/ontology#CourseWithPrerequisites | 339 |
| https://example.org/uiuc-course-advisor/ontology#DegreeRequirement | 18 |
| https://example.org/uiuc-course-advisor/ontology#PrerequisiteCondition | 511 |


# INF6_property_chain_scheduledInTerm_and_inverse_maySatisfy

```
# AI-3001 Iteration 1 - SPARQL queries (Q01-Q15 = CQ01-CQ15, INF1-INF6 = inference demos)
# Team: Hassan Tariq (24i-2555), Afaan Sohail (24i-0081), Diya Hurmat (24i-0094)
# Queries marked [needs reasoning] return rows only with OWL2-RL inference enabled.
BASE <https://example.org/uiuc-course-advisor/resource/>
PREFIX uca:  <https://example.org/uiuc-course-advisor/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>


# Inference: property chain + inverse (scheduledInTerm, maySatisfyRequirement) [needs reasoning]
# Features: BGP over two inferred properties, OPTIONAL
SELECT ?courseCode ?title WHERE {
  ?course uca:maySatisfyRequirement <requirement/UIUC-BS-CS-2026/Elective-TeamProject> ;
          uca:scheduledInTerm <term/2026-fa> ;
          uca:courseCode ?courseCode .
  OPTIONAL { ?course uca:courseTitle ?title }
}
ORDER BY ?courseCode
```

| courseCode | title |
| --- | --- |
| CS 411 | Database Systems |
| CS 415 | Game Development |
| CS 417 | Introduction to Extended Reality |
| CS 425 | Distributed Systems |
| CS 427 | Software Engineering I |
| CS 437 | Topics in Internet of Things |
| CS 465 | User Interface Design |
| CS 497 | CS Team Project |


# Three verified symbolic inference examples


# inverse_department

inDepartment owl:inverseOf hasCourse

```
{
  "name": "inverse_department",
  "conclusion": {
    "s": "<https://example.org/uiuc-course-advisor/resource/department/CS>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasCourse>",
    "o": "<https://example.org/uiuc-course-advisor/resource/course/CS421>",
    "status": "inferred",
    "id": "Ea108fedc4fcc53b5"
  },
  "premises": [
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/course/CS421>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#inDepartment>",
      "o": "<https://example.org/uiuc-course-advisor/resource/department/CS>",
      "status": "explicit",
      "id": "Ef4e0d7aa0bb3047a"
    }
  ],
  "rule": "inDepartment owl:inverseOf hasCourse",
  "schema_axioms": [
    {
      "s": "<https://example.org/uiuc-course-advisor/ontology#inDepartment>",
      "p": "<http://www.w3.org/2002/07/owl#inverseOf>",
      "o": "<https://example.org/uiuc-course-advisor/ontology#hasCourse>",
      "status": "explicit",
      "id": "E50779dd0a2255c70"
    }
  ],
  "absent_from_explicit": true,
  "present_in_closure": true
}
```


# completion_chain

hasCompletion o completedCourse -> hasCompletedCourse

```
{
  "name": "completion_chain",
  "conclusion": {
    "s": "<https://example.org/uiuc-course-advisor/resource/student/S003>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasCompletedCourse>",
    "o": "<https://example.org/uiuc-course-advisor/resource/course/CS124>",
    "status": "inferred",
    "id": "E146b0e269c1d202f"
  },
  "premises": [
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/student/S003>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#hasCompletion>",
      "o": "<https://example.org/uiuc-course-advisor/resource/completion/S003/CS124>",
      "status": "explicit",
      "id": "E56dffea2c9c123fc"
    },
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/completion/S003/CS124>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#completedCourse>",
      "o": "<https://example.org/uiuc-course-advisor/resource/course/CS124>",
      "status": "explicit",
      "id": "E29313bf6239657f0"
    }
  ],
  "rule": "hasCompletion o completedCourse -> hasCompletedCourse",
  "schema_axioms": [
    {
      "s": "<https://example.org/uiuc-course-advisor/ontology#hasCompletedCourse>",
      "p": "<http://www.w3.org/2002/07/owl#propertyChainAxiom>",
      "o": "_:n09b8ccdb34534d42b14beca5eafa80b4b5",
      "status": "explicit",
      "id": "E8e9434c071001ff7"
    }
  ],
  "absent_from_explicit": true,
  "present_in_closure": true
}
```


# offering_chain

hasOffering o offeredInTerm -> scheduledInTerm

```
{
  "name": "offering_chain",
  "conclusion": {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/CS421>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#scheduledInTerm>",
    "o": "<https://example.org/uiuc-course-advisor/resource/term/2026-fa>",
    "status": "inferred",
    "id": "E0c17de53a889a68e"
  },
  "premises": [
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/course/CS421>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#hasOffering>",
      "o": "<https://example.org/uiuc-course-advisor/resource/offering/CS421/2026-fa>",
      "status": "explicit",
      "id": "Ed57e791826b2ab8c"
    },
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/offering/CS421/2026-fa>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#offeredInTerm>",
      "o": "<https://example.org/uiuc-course-advisor/resource/term/2026-fa>",
      "status": "explicit",
      "id": "Ef42b1a939fe7a663"
    }
  ],
  "rule": "hasOffering o offeredInTerm -> scheduledInTerm",
  "schema_axioms": [
    {
      "s": "<https://example.org/uiuc-course-advisor/ontology#scheduledInTerm>",
      "p": "<http://www.w3.org/2002/07/owl#propertyChainAxiom>",
      "o": "_:n09b8ccdb34534d42b14beca5eafa80b4b11",
      "status": "explicit",
      "id": "E78b18ae40c5f2f29"
    }
  ],
  "absent_from_explicit": true,
  "present_in_closure": true
}
```


# Preserved actual screenshots

![Archived Iteration 1 screenshot: GraphDB repository Project_uiuc configured with the OWL2-RL ruleset. Supplied in the original archive; not a current execution screenshot.](iteration1/Visualization/GraphDB_G01.png)

![Archived Iteration 1 screenshot: Protégé active ontology, version 1.3, header and ontology metrics. Supplied in the original archive; not a current execution screenshot.](iteration1/Visualization/Protege_P01.png)

![Archived Iteration 1 screenshot: GraphDB class-relationship chord visualization for the course KG. Supplied in the original archive; displayed link statistics belong to that archived run.](iteration1/Visualization/GraphDB_G05.png)

![Archived Iteration 1 screenshot: the inference-dependent Q11 department aggregate and displayed GraphDB results. The new local execution is preserved separately in the current query-results CSV.](iteration1/Visualization/GraphDB_G08.png)

![Actual Day 5 prerequisite-chain execution for CS421, showing the input, graph hash, path validation and a stored-edge excerpt. Full paths are in reasoning/outputs/day5/chain.json.](report/screenshots/afaan_day5_chain.png)

![Actual Day 5 eligibility execution for synthetic S003 and CS421 in Fall 2026, showing met and unmet AND/OR conditions. Full evidence is in reasoning/outputs/day5/eligibility.json.](report/screenshots/afaan_day5_eligibility.png)

![Actual Day 5 hypothetical reverse-unlock execution for synthetic S002 completing CS225, with concurrent-plan credit disabled to match the what-if protocol. Full assumptions and blockers are in reasoning/outputs/day5/unlock.json.](report/screenshots/afaan_day5_unlock.png)

![Actual Day 5 recorded degree-progress execution for synthetic S003, showing count/credit shortfalls and graph evidence. This is not a certified graduation audit. Full groups are in reasoning/outputs/day5/degree.json.](report/screenshots/afaan_day5_degree.png)

![Actual desktop comparison viewer showing the twenty recorded trial 3 grading decisions in ten paired rows, with generated A/B totals. Full questions, expected results and responses remain in comparison.csv.](report/screenshots/comparison.png)

![Actual laptop execution of the weather question for CS 421. The app returns insufficient_evidence with llm_called=false; no weather answer is invented.](report/screenshots/insufficient_evidence.png)

![Actual desktop viewer showing a fresh local Qwen3 4B answer to the MATH 241 eligibility question, retrieved condition rows and RDF evidence. The separate CPU readiness profile uses a smaller context/output budget than the recorded Kaggle experiment. Full response: report/live_grounded.json.](report/screenshots/grounded_app.png)


# Iteration 2 architecture

Architecture: see report/architecture.mmd.

Diagram source: report/architecture.mmd. Local RDF retrieval is the executable default; GraphDB is used separately for the live query/inference walkthrough.


# Iteration 2: knowledge-grounded course planning


# Objective and scope

The course_planning system answers prerequisite, eligibility and degree-allocation questions over the supplied UIUC Fall 2026 snapshot and the curated Grainger BS Computer Science requirements. It extends Iteration 1 through an executable multi-hop reasoning component and a natural-language application whose context comes from that graph at query time. The students are explicitly synthetic test personas, not records of actual UIUC students. The frozen snapshot is the project's evidence base; it does not establish current registration permission or an official graduation audit.

The consolidated report generator adds the original competency questions and mapping, the preserved ontology/URI design, reproduced graph statistics, original queries with re-executed outputs, and the supplied actual Iteration 1 screenshots. It then appends the Iteration 2 method, measured reasoning results, comparison protocol and explainability records. Results are loaded from execution artifacts; missing experimental outputs are printed as PENDING.


# Method: Option C multi-hop KG reasoning

A prerequisite-course hop is a sequence through an expression, an option, a condition and a referenced course. The reasoner follows these stored edges and records every intermediate entity. It retains a nested expression tree so that different options remain alternatives, conditions within an option remain conjunctions, and a CourseChoiceCondition requires only one of its candidates. Therefore a course appearing on a possible path is not automatically a compulsory prerequisite.

Path-based reasoning has a substantial research history. Lao and Cohen (2010) learn relational retrieval from edge-label sequences; DeepPath learns relational navigation policies (Xiong et al., 2017), and MINERVA conditions navigation on a query (Das et al., 2018). These sources motivated preserving typed paths and examining intermediate decisions. Our implementation is a deterministic symbolic traversal suitable for the supplied graph; it does not implement their trained policies, embeddings or link-prediction objectives. Hogan et al. (2021) informed the distinction between querying, deduction and induction. Option C here produces verified traversals and rule conclusions, with no predicted links.

Prerequisite-chain search uses a path-local ancestry set to stop cycles while allowing the same course to appear on different valid branches. A course-hop depth bound and terminal-path bound control enumeration; the trace explicitly marks cycle stops and truncation. A separate queue-based visited-set closure computes all reachable candidates for comparison with SPARQL. That closure includes the start entity only if a genuine nonzero cycle returns to it. The validation follows SPARQL property-path semantics (Harris and Seaborne, 2013).

Eligibility checks recorded completions, same-term concurrent plans only where allowsConcurrent is true, standing rank and explicit course permissions. Free-text and unknown conditions remain unverified. A single fully met option satisfies the encoded expression. Already completed status and observed offering status are separate from the prerequisite verdict. A stub with no source catalog text cannot be declared unrestricted. needs_review remains a visible warning even if an encoded option succeeds. These are conservative closed-world application rules, distinct from OWL's open-world schema semantics.

Reverse unlock search finds courses that can reach a proposed completion, evaluates each before and after the hypothetical addition, and identifies those whose encoded eligibility changes. Indirect reachability alone does not make a downstream course immediately available. The original what-if queries omit concurrent-plan credit, so that comparison uses the same policy. Hypothetical completions appear only as assumptions and are never inserted into the RDF evidence.

Degree-progress reasoning follows student → completion → allocated requirement → program, using a reverse traversal of the stored program → requirement edge. It reports allocated counts and credits, unmet encoded thresholds, invalid memberships and technical/advanced-elective double-counting conflicts. It inspects existing allocations rather than optimizing a new assignment. Focus-area alternatives and prose-only policies prevent a per-group numeric summary from constituting a graduation decision.


# Architecture and KG-grounded generation

The pipeline is question → entity/intent linking → parameterized SPARQL and Python reasoning → context construction → the configured LLM → generated answer and inspectable graph evidence. It runs locally from the supplied Turtle graph; GraphDB remains available for the required live ontology/inference walkthrough and optional endpoint checks. The app does not require a live GraphDB server to retrieve its graph evidence.

Entity linking recognizes course codes, synthetic student IDs and terms. Intent rules select generic query families without consulting the evaluation question file or stored answers. Unknown, ambiguous or unsupported requests receive an insufficient-evidence response. Valid unseen combinations of known entities run against the graph. The scope of natural-language coverage is the implemented templates; arbitrary questions and multi-turn reference resolution remain limitations.

The application uses KG-RAG with SPARQL-generated context, informed by external-memory grounding in Lewis et al. (2020). It preserves relationships as in graph-oriented retrieval, but does not implement the community-index construction or global summarization procedure in Edge et al. (2024). Retrieved records, original query text, reasoning traces, graph hash and evidence edge IDs remain inspectable. OWL-inferred triples are labelled separately by testing membership in the explicit graph and its computed closure.

The grounding prompt restricts the model to the supplied context and asks it to cite edge or result-row IDs, preserve alternative branches and state missing evidence. The LLM remains capable of unsupported prose: prompts and citation-ID checks do not establish semantic correctness. Invalid citations are retained for scoring. Every query row is included or the system abstains if the result table alone exceeds its context budget. Additional evidence and traces may be omitted from the prompt with explicit omitted counts; the full output artifact keeps them. Character budgets approximate model tokens, and length-truncated answers are flagged.

The selected free local configuration uses Qwen3 4B Instruct through Ollama's compatible chat API (Qwen Team; Ollama documentation). Both A and B use the same locally created model, temperature and output budget. The harness records and checks the actual Ollama model digest and runtime version across runs; actual settings and prompt hashes are retained with the experiment. Local inference has no paid API calls, but requires suitable RAM, downloaded model weights and execution time. The selected experiment now contains actual model outputs; suitability remains limited by the recorded errors.


# Reasoning evaluation protocol and interpretation

The reachable-prerequisite set for every course with a recorded expression is compared with an independently executed SPARQL property-path closure. Exact match is computed on sets, including cycle semantics. The Q01 eligible-course sets are re-instantiated for all synthetic students using the same offering/exclusion/concurrency scope. Q03 condition-level decisions are compared for CS421 and every synthetic student. Every returned edge in the evaluated traces is checked for explicit membership or genuine closure-only inferred membership.

The scripts also exercise an unknown course, a catalog course without recorded prerequisites, an unmet student case, a cycle and a deliberately shallow depth bound. They record runtime and path-depth statistics. Targets are not reported as results: the generated tables supply the observed metrics. Successful graph-edge validation establishes provenance integrity, not the correctness of a source statement, a prerequisite parse or an adviser policy. One local runtime is an execution measurement rather than a statistically robust benchmark.


# LLM-only versus KG-grounded experiment

Ten original competency questions are retained verbatim with explicit test instances supplied equally to both modes. The selection covers prerequisite chains, condition evaluation, downstream and hypothetical effects, degree allocations, a two-hop query, cross-listings, an OWL-dependent aggregate and recommendation evidence. Expected answers are re-executed against the frozen graph. The baseline receives neither the graph nor synthetic transcripts, expected outputs or retrieval tools. The grounded mode uses the real router and query-time retrieval, never a case-specific answer lookup.

Both conditions use the same LLM, temperature and maximum output tokens with fresh stateless calls. Their prompts differ to express grounding, so this compares complete systems rather than isolating retrieval as the sole causal variable. Paired runs can alternate order; the daily work plan also permits separately recorded A and B runs under the same immutable manifest. Changes in model, prompts, questions or graph require a new run ID. Provider failures remain errors, and missing calls or reviews block final scoring.

A human reviewer compares each response against the complete expected rows, checks requested-set completeness and substantive conclusions, counts atomic unsupported factual claims, and verifies relevant provenance. A refusal can avoid hallucination while failing to answer an answerable CQ. A second member reviews disagreements. Grades are tied to raw-file hashes. Only after review does the scorer generate the required comparison table, correctness totals out of ten, unsupported-claim totals and evidence counts. No automatic word-match score or fabricated placeholder is treated as a measured result.


# Comparative findings

The selected run is qwen3_trial3_kaggle. All twenty model calls completed without flagged truncation. The recorded grading entries give 0/10 for the baseline and 6/10 for the grounded application. CQ01, CQ03, CQ04, CQ08, CQ11 and CQ15 pass the strict completeness and correctness rule. CQ02 omits three prerequisite edges, CQ06 omits three completed requirement groups, CQ10 omits CS 581, and CQ13 adds an unsupported blanket statement about other prerequisites. The baseline mainly refuses because it lacks the frozen catalog and synthetic transcripts. This can avoid hallucination while failing to answer an answerable question. Grading explanations and unsupported-claim counts are retained per response. Reviewer assignments were supplied by the team, with ten entries each for Hassan Tariq and Diya Hurmat.

Trial 3 was revised after inspecting earlier failures. Runtime context includes query-field explanations, exact row counts and recorded student completion codes, while retaining all query rows and full evidence in the artifacts. The model, settings and expected-question snapshot are unchanged from trial 2. This is a development rerun rather than a held-out evaluation. The ten selected questions and synthetic transcripts limit generalization to real advising. The report reads every numeric total from generated execution or scoring artifacts.


# Explainability examples

The report builder includes three real retrieved-context records for eligibility, multi-hop prerequisites and the inference-dependent elective aggregate. Their generated-text fields now contain the supplied actual grounded CQ03, CQ08 and CQ11 responses, including any errors; the prose is not silently corrected. At final assembly it selects the corresponding live B records and prints the question, actual generated text, query rows, representative graph edges and rule traces. The complete paths remain in the machine-readable artifacts.

Explicit knowledge means an RDF triple directly in the submitted Turtle. Inferred knowledge means a triple absent there and present after OWL RL closure; separately saved symbolic examples include the actual stored premises and schema axiom. Eligibility verdicts and aggregate counts are computed application/query conclusions. Generated text means the actual LLM response. There is no Prediction in Option C; hypothetical completions are assumptions. An unrecorded completion is a closed-world absence check, not a stored negative fact.


# Limitations and integrity

The graph is a scoped historical catalog snapshot with missing-course stubs, ambiguous prerequisite prose and synthetic transcripts. Cross-listings do not establish interchangeability; no owl:sameAs substitution is introduced. The parser keeps difficult clauses for review, and numeric eligibility covers only encoded conditions. GPA, minimum grades, topic-specific approvals, credit caps and other prose policies require human interpretation. Degree allocation is not automatically optimized, and focus areas are alternatives rather than simultaneous graduation obligations.

The local OWL closure count may differ from a historical runtime; the report records the installed dependency versions and measured total. Query comparison normalizes URI display, unbound values and unspecified GROUP_CONCAT order, while preserving the raw outputs for inspection. SHACL validates the supplied structural shapes; conformity does not prove every degree policy, including the separately seeded double-count conflict. GraphDB and Protégé screenshots supplied with Iteration 1 are identified as archived images, not new Iteration 2 executions.

Grounded prose can omit rows, misuse a valid citation or add an unsupported inference. Routing is template-based, context is bounded, and output limits can truncate lists. A context budget is a character approximation, not an exact tokenizer guarantee. A failure to retrieve is reported as insufficient evidence instead of a real-world absence claim. Manual semantic scoring and the live unseen-question demonstration remain necessary.

ChatGPT was used to assist with code, documentation and prompts, and to cite external code, datasets, ontologies, prompts, libraries, tutorials and other resources. The team must review, modify, reproduce and explain the work. The contribution schedule is prospective: no commits were created, backdated or attributed to team members by this scaffold. The final contribution table must cite actual individual commits and the externally hosted demo. Repository creation, instructor access, clean-machine execution and recording are not claimed without evidence.


# References and resource attribution

Lao, N. and Cohen, W. W. (2010). Relational retrieval using a combination of path-constrained random walks. Machine Learning 81, 53–67. https://doi.org/10.1007/s10994-010-5205-8

Xiong, W., Hoang, T. and Wang, W. Y. (2017). DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning. EMNLP, 564–573. https://doi.org/10.18653/v1/D17-1060

Das, R. et al. (2018). Go for a Walk and Arrive at the Answer: Reasoning Over Paths in Knowledge Bases using Reinforcement Learning. ICLR. https://arxiv.org/abs/1711.05851

Hogan, A. et al. (2021). Knowledge Graphs. ACM Computing Surveys 54(4), Article 71. https://doi.org/10.1145/3447772

Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS. https://arxiv.org/abs/2005.11401

Edge, D. et al. (2024; revised 2025). From Local to Global: A Graph RAG Approach to Query-Focused Summarization. https://arxiv.org/abs/2404.16130

Harris, S. and Seaborne, A., eds. (2013). SPARQL 1.1 Query Language. W3C. https://www.w3.org/TR/sparql11-query/

W3C (2012). OWL 2 Web Ontology Language Profiles (Second Edition). https://www.w3.org/TR/owl2-profiles/

UIUC course-catalog dataset. https://discovery.cs.illinois.edu/dataset/course-catalog/ (supplied Fall 2026 CSV; source evidence, not a newly downloaded catalog).

Illinois prerequisites dataset. https://github.com/illinois/prerequisites-dataset (supplied QA-only CSV).

UIUC Grainger BS Computer Science catalog. https://catalog.illinois.edu/undergraduate/engineering/computer-science-bs/ (Iteration 1 curated requirement provenance; current web page is not substituted for the supplied snapshot).

Qwen Team. Qwen3 official repository and model releases. https://github.com/QwenLM/Qwen3

Ollama. OpenAI-compatible API and selected model entry. https://docs.ollama.com/api/openai-compatibility ; https://ollama.com/library/qwen3:4b-instruct

RDFLib and OWL-RL libraries. https://github.com/RDFLib/rdflib ; https://github.com/RDFLib/OWL-RL

pySHACL. https://github.com/RDFLib/pySHACL ; pandas. https://pandas.pydata.org/docs/ ; Requests. https://requests.readthedocs.io/ ; pytest. https://docs.pytest.org/ ; python-docx. https://python-docx.readthedocs.io/ ; ReportLab. https://www.reportlab.com/docs/reportlab-userguide.pdf

Ontotext GraphDB documentation. https://graphdb.ontotext.com/documentation/10.7/ ; Protégé. https://protege.stanford.edu/

Project code/prompt provenance: supplied Iteration 1 archive, this repository's `iteration1/Code`, `reasoning`, `app`, `evaluation`, and `prompts`; ChatGPT use is disclosed above. Exact package versions are recorded in the environment artifact. Research titles and links were checked against primary publication/release pages on 21 November 2026.


# Selected Kaggle experiment findings

The selected manifest records Linux, Python 3.12.15, Ollama 0.40.18 and Qwen3 4B Q4_K_M. Runtime evidence reports full GPU loading. The artifact audit checks all twenty actual responses, source and prompt hashes, request settings and graph evidence. Its recorded results are included alongside the scored comparison. It establishes artifact consistency and graph membership, not infallible prose.

Trial 1 and trial 2 remain historical runs. Their truncation and semantic problems are not silently replaced. Trial 3 has no flagged output truncation and no unknown citation IDs, but still has omissions and one unsupported grounded claim under the recorded rubric. No result was manually repaired. The manifest's missing Git commit is preserved because Kaggle ran outside a checkout; the final implementation commit must be recorded separately.



# Measured modern-reasoning results

| Observed metric | Result |
| --- | --- |
| generated_utc | "2026-11-21T12:12:36.077075+00:00" |
| graph_sha256 | "ac0352a0246d3e67fae34d3fd27f3847bb9a3d7897478f19e865478f2a1ea2a8" |
| python | "3.11.7" |
| courses_with_prerequisites | 339 |
| reachability_exact_matches | 339 |
| reachability_exact_match_rate | 1.0 |
| eligibility_student_set_matches | 4 |
| eligibility_student_sets_tested | 4 |
| condition_matches | 12 |
| conditions_tested | 12 |
| returned_edges_checked | 206635 |
| invalid_returned_edges | 0 |
| edge_validity_rate | 1.0 |
| invalid_or_disconnected_paths | 0 |
| maximum_returned_course_depth | 12 |
| mean_returned_course_depth | 5.486440053994355 |
| truncated_course_traces | 0 |
| max_depth | 32 |
| max_paths | 20000 |
| runtime_seconds | 12.406906367000374 |
| negative_cases | {"unknown_course": "no_path", "no_prerequisites": "satisfied", "failing_student": "unmet"} |

Reachable sets include the source only if an actual nonzero cycle returns to it.

Q01 comparison covers courses with recorded expressions; no-prerequisite courses are separate.

Q03 is checked for all four students on CS421; not every student-course pair.

100% edge validity does not establish parser or policy correctness.

Runtime is one local run, not a statistical benchmark.


# eligibility.csv

| student | query | expected_count | actual_count | exact_match | missing | extra |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | Q01 | 11 | 11 | True | [] | [] |
| S002 | Q01 | 15 | 15 | True | [] | [] |
| S003 | Q01 | 52 | 52 | True | [] | [] |
| S004 | Q01 | 71 | 71 | True | [] | [] |


# option_conditions.csv

| student | condition | query | expected_met | actual_met | exact_match |
| --- | --- | --- | --- | --- | --- |
| S001 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1 | Q03 | False | False | True |
| S001 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/2 | Q03 | False | False | True |
| S001 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/3 | Q03 | False | False | True |
| S002 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1 | Q03 | False | False | True |
| S002 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/2 | Q03 | False | False | True |
| S002 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/3 | Q03 | False | False | True |
| S003 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1 | Q03 | True | True | True |
| S003 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/2 | Q03 | False | False | True |
| S003 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/3 | Q03 | True | True | True |
| S004 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1 | Q03 | True | True | True |
| S004 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/2 | Q03 | True | True | True |
| S004 | https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/3 | Q03 | True | True | True |


# Natural-language retrieval validation (no model calls)

| CQ | Intent match | Expected-row match | Evidence edges | Invalid edges | Rows fit context | Omitted evidence / traces |
| --- | --- | --- | --- | --- | --- | --- |
| CQ01 | True | True | 569 | 0 | True | 502 / 0 |
| CQ02 | True | True | 1073 | 0 | True | 990 / 0 |
| CQ03 | True | True | 171 | 0 | True | 60 / 0 |
| CQ04 | True | True | 1552 | 0 | True | 1433 / 1 |
| CQ06 | True | True | 789 | 0 | True | 758 / 0 |
| CQ08 | True | True | 885 | 0 | True | 773 / 0 |
| CQ10 | True | True | 414 | 0 | True | 286 / 0 |
| CQ11 | True | True | 1819 | 0 | True | 1708 / 0 |
| CQ13 | True | True | 1219 | 0 | True | 1087 / 1 |
| CQ15 | True | True | 223 | 0 | True | 118 / 0 |

These are retrieval checks, not LLM accuracy measurements. Full evidence remains in the JSON; context omissions are counted.

Actual pytest run: {"name": "pytest", "errors": "0", "failures": "0", "skipped": "0", "tests": "39", "time": "7.601", "timestamp": "2026-11-26T20:11:23.307059", "hostname": "afaan-sohail-ThinkPad-T470s"}

Actual fresh isolated virtual-environment pytest run: {"name": "pytest", "errors": "0", "failures": "0", "skipped": "0", "tests": "39", "time": "12.648", "timestamp": "2026-11-26T20:24:38.146726", "hostname": "afaan-sohail-ThinkPad-T470s"}. This is not a separate-laptop certification.


# Observed review-laptop checks

Fresh laptop environment: fresh project .venv, Python 3.11.7; passing tests: 39

Protege: Version 1.3 ontology loaded successfully; see protege.log

| GraphDB query | Inference | Observed rows |
| --- | --- | --- |
| Q08 | True | 56 |
| INF1 | False | 0 |
| INF1 | True | 146 |
| INF3 | False | 0 |
| INF3 | True | 4 |
| INF6 | False | 0 |
| INF6 | True | 8 |

Local CPU readiness response: {"llm_called": true, "finish_reason": "stop", "runtime_seconds": 98.83085517099971, "model": "course-planning-qwen3-review", "context_max_chars": 3000, "output_tokens_limit": 512, "configured_context_tokens": 4096, "mode": "CPU", "failed_attempt": "report/laptop_checks/failed_CS421_grounded.json", "response_file": "report/live_grounded.json", "limitations": "Cold inference takes several minutes. Local demo settings differ from the scored Kaggle experiment."}

The first CS421 readiness answer was incorrectly formatted and truncated at its local output limit. It is preserved separately. The successful short MATH241 answer establishes basic execution, not correctness on all unseen questions. Neither local answer is part of the scored Kaggle experiment.

Current GraphDB state: Stopped after checks to restore original state and free RAM


# Ten-question A/B comparison

| CQ / question | Expected answer | LLM only | KG-grounded | Correct? A / B | Evidence available? A / B |
| --- | --- | --- | --- | --- | --- |
| CQ01 / Given a student's completed courses and a target term, which catalog courses are offered in that term and have a satisfied prerequisite alternative? Instance: synthetic student S002; target term Fall 2026. | [{"courseCode": "ASRM 210", "title": "Theory of Interest", "satisfiedOptions": "1"}, {"courseCode": "BIOE 210", "title": "Linear Algebra for Biomedical Data Science", "satisfiedOptions": "1"}, {"courseCode": "CS 101", "title": "Intro Computing: Engrg & Sci", "satisfiedOptions": "1"}, {"courseCode": "CS 225", "title": "Data Structures", "satisfiedOptions": "1"}, {"courseCode": "CS 233", "title": "Computer Architecture", "satisfiedOptions": "1"}, {"courseCode": "CS 361", "title": "Probability & Statistics for Computer Science", "satisfiedOptions": "1"}, {"courseCode": "CS 427", "title": "Software Engineering I", "satisfiedOptions": "1"}, {"courseCode": "IE 310", "title": "Deterministic Models in Optimization", "satisfiedOptions": "1"}, {"courseCode": "MATH 213", "title": "Basic Discrete Mathematics", "satisfiedOptions": "1"}, {"courseCode": "MATH 225", "title": "Introductory Matrix Theory", "satisfiedOptions": "1"}, {"courseCode": "MATH 241", "title": "Calculus III", "satisfiedOptions": "1"}, {"courseCode": "PHYS 100", "title": "Thinking About Physics", "satisfiedOptions": "1"}, {"courseCode": "PHYS 212", "title": "University Physics: Elec & Mag", "satisfiedOptions": "1"}, {"courseCode": "PHYS 213", "title": "Univ Physics: Thermal Physics", "satisfiedOptions": "1"}, {"courseCode": "STAT 400", "title": "Statistics and Probability I", "satisfiedOptions": "1"}] | No catalog data or student transcript information is provided. Therefore, it is impossible to determine which courses are offered in Fall 2026 or whether any prerequisites are satisfied for student S002.<br><br>To answer the question, the following information is required:<br><br>- The university course catalog (with course offerings by term)<br>- The student’s completed courses (to evaluate prerequisite satisfaction)<br>- Prerequisite rules (including alternative pathways) for each course<br><br>Without this data, no valid conclusion can be drawn.<br><br>**Conclusion**: Insufficient information to determine catalog courses offered in Fall 2026 with satisfied prerequisite alternatives for student S002. | \| courseCode \| title \| satisfiedOptions \| citation \|<br>\|-----------\|------\|------------------\|---------\|<br>\| ASRM 210 \| Theory of Interest \| 1 \| [R1] \|<br>\| BIOE 210 \| Linear Algebra for Biomedical Data Science \| 1 \| [R2] \|<br>\| CS 101 \| Intro Computing: Engrg & Sci \| 1 \| [R3] \|<br>\| CS 225 \| Data Structures \| 1 \| [R4] \|<br>\| CS 233 \| Computer Architecture \| 1 \| [R5] \|<br>\| CS 361 \| Probability & Statistics for Computer Science \| 1 \| [R6] \|<br>\| CS 427 \| Software Engineering I \| 1 \| [R7] \|<br>\| IE 310 \| Deterministic Models in Optimization \| 1 \| [R8] \|<br>\| MATH 213 \| Basic Discrete Mathematics \| 1 \| [R9] \|<br>\| MATH 225 \| Introductory Matrix Theory \| 1 \| [R10] \|<br>\| MATH 241 \| Calculus III \| 1 \| [R11] \|<br>\| PHYS 100 \| Thinking About Physics \| 1 \| [R12] \|<br>\| PHYS 212 \| University Physics: Elec & Mag \| 1 \| [R13] \|<br>\| PHYS 213 \| Univ Physics: Thermal Physics \| 1 \| [R14] \|<br>\| STAT 400 \| Statistics and Probability I \| 1 \| [R15] \| | No / Yes | No / Yes |
| CQ02 / For a selected course, what are its possible prerequisite chains back to courses with no recorded course prerequisites, preserving AND/OR branches? Instance: CS 421. | [{"fromCode": "ASRM 210", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 231", "toIsBaseCourse": "false"}, {"fromCode": "ASRM 406", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 241", "toIsBaseCourse": "false"}, {"fromCode": "ASRM 406", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ASRM 210", "toIsBaseCourse": "false"}, {"fromCode": "ASRM 406", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "FIN 221", "toIsBaseCourse": "false"}, {"fromCode": "ASRM 406", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 210", "toIsBaseCourse": "true"}, {"fromCode": "BIOE 210", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 231", "toIsBaseCourse": "false"}, {"fromCode": "BIOE 210", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 101", "toIsBaseCourse": "false"}, {"fromCode": "BIOE 210", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 124", "toIsBaseCourse": "false"}, {"fromCode": "CS 101", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 220", "toIsBaseCourse": "false"}, {"fromCode": "CS 101", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 221", "toIsBaseCourse": "false"}, {"fromCode": "CS 101", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 231", "toIsBaseCourse": "false"}, {"fromCode": "CS 101", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 241", "toIsBaseCourse": "false"}, {"fromCode": "CS 124", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 112", "toIsBaseCourse": "false"}, {"fromCode": "CS 128", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 124", "toIsBaseCourse": "false"}, {"fromCode": "CS 128", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 125", "toIsBaseCourse": "true"}, {"fromCode": "CS 173", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 124", "toIsBaseCourse": "false"}, {"fromCode": "CS 173", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 125", "toIsBaseCourse": "true"}, {"fromCode": "CS 173", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ECE 220", "toIsBaseCourse": "false"}, {"fromCode": "CS 173", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 220", "toIsBaseCourse": "false"}, {"fromCode": "CS 173", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 221", "toIsBaseCourse": "false"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 126", "toIsBaseCourse": "true"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 128", "toIsBaseCourse": "false"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 173", "toIsBaseCourse": "false"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 413", "toIsBaseCourse": "true"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ECE 220", "toIsBaseCourse": "false"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 213", "toIsBaseCourse": "false"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 314", "toIsBaseCourse": "false"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 347", "toIsBaseCourse": "true"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 412", "toIsBaseCourse": "false"}, {"fromCode": "CS 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 413", "toIsBaseCourse": "false"}, {"fromCode": "CS 233", "option": "option 1", "edgeType": "AND: required course", "toCode": "CS 225", "toIsBaseCourse": "false"}, {"fromCode": "CS 233", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 125", "toIsBaseCourse": "true"}, {"fromCode": "CS 233", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 128", "toIsBaseCourse": "false"}, {"fromCode": "CS 233", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 173", "toIsBaseCourse": "false"}, {"fromCode": "CS 233", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 213", "toIsBaseCourse": "false"}, {"fromCode": "CS 340", "option": "option 1", "edgeType": "AND: required course", "toCode": "CS 128", "toIsBaseCourse": "false"}, {"fromCode": "CS 340", "option": "option 1", "edgeType": "AND: required course", "toCode": "CS 225", "toIsBaseCourse": "false"}, {"fromCode": "CS 374", "option": "option 1", "edgeType": "AND: required course", "toCode": "CS 225", "toIsBaseCourse": "false"}, {"fromCode": "CS 374", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 173", "toIsBaseCourse": "false"}, {"fromCode": "CS 374", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 213", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ASRM 406", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "BIOE 210", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 233", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 240", "toIsBaseCourse": "true"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 340", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 374", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ECE 374", "toIsBaseCourse": "true"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ECE 391", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 225", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 257", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 415", "toIsBaseCourse": "false"}, {"fromCode": "CS 421", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 416", "toIsBaseCourse": "false"}, {"fromCode": "ECE 220", "option": "option 1", "edgeType": "AND: required course", "toCode": "ECE 120", "toIsBaseCourse": "false"}, {"fromCode": "ECE 391", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 233", "toIsBaseCourse": "false"}, {"fromCode": "ECE 391", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ECE 220", "toIsBaseCourse": "false"}, {"fromCode": "FIN 221", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ECON 102", "toIsBaseCourse": "true"}, {"fromCode": "FIN 221", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "ECON 103", "toIsBaseCourse": "true"}, {"fromCode": "MATH 115", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 112", "toIsBaseCourse": "false"}, {"fromCode": "MATH 213", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 220", "toIsBaseCourse": "false"}, {"fromCode": "MATH 213", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 221", "toIsBaseCourse": "false"}, {"fromCode": "MATH 220", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 115", "toIsBaseCourse": "false"}, {"fromCode": "MATH 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 220", "toIsBaseCourse": "false"}, {"fromCode": "MATH 225", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 221", "toIsBaseCourse": "false"}, {"fromCode": "MATH 231", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 220", "toIsBaseCourse": "false"}, {"fromCode": "MATH 231", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 221", "toIsBaseCourse": "false"}, {"fromCode": "MATH 241", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 231", "toIsBaseCourse": "false"}, {"fromCode": "MATH 257", "option": "option 1", "edgeType": "AND: required course", "toCode": "CS 101", "toIsBaseCourse": "false"}, {"fromCode": "MATH 257", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 220", "toIsBaseCourse": "false"}, {"fromCode": "MATH 257", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 221", "toIsBaseCourse": "false"}, {"fromCode": "MATH 314", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 241", "toIsBaseCourse": "false"}, {"fromCode": "MATH 412", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "CS 374", "toIsBaseCourse": "false"}, {"fromCode": "MATH 412", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 314", "toIsBaseCourse": "false"}, {"fromCode": "MATH 412", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 347", "toIsBaseCourse": "true"}, {"fromCode": "MATH 413", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 314", "toIsBaseCourse": "false"}, {"fromCode": "MATH 413", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 347", "toIsBaseCourse": "true"}, {"fromCode": "MATH 415", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 241", "toIsBaseCourse": "false"}, {"fromCode": "MATH 416", "option": "option 1", "edgeType": "AND: required course", "toCode": "MATH 241", "toIsBaseCourse": "false"}, {"fromCode": "MATH 416", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 314", "toIsBaseCourse": "false"}, {"fromCode": "MATH 416", "option": "option 1", "edgeType": "OR: one of a group", "toCode": "MATH 347", "toIsBaseCourse": "true"}] | None of the provided information allows for the determination of prerequisite chains for CS 421 or any course, as no course data, prerequisites, or structure is available. Without a course catalog or prerequisite graph, it is impossible to trace chains back to courses with no recorded prerequisites, nor to preserve AND/OR branches.<br><br>**Conclusion**:  <br>No possible prerequisite chains can be determined due to lack of course data.  <br><br>**Missing Information**:  <br>- Course catalog or prerequisite database  <br>- Prerequisite relationships for CS 421 or any course  <br>- Structure of course hierarchy (e.g., whether prerequisites are AND/OR)  <br><br>→ Response is not feasible with current input. | \| fromCode \| option \| edgeType \| toCode \| toIsBaseCourse \|<br>\|---------\|--------\|----------\|--------\|----------------\|<br>\| ASRM 406 \| option 1 \| OR: one of a group \| ASRM 210 \| false \|<br>\| ASRM 406 \| option 1 \| OR: one of a group \| FIN 221 \| false \|<br>\| ASRM 406 \| option 1 \| OR: one of a group \| MATH 210 \| true \|<br>\| BIOE 210 \| option 1 \| OR: one of a group \| CS 101 \| false \|<br>\| BIOE 210 \| option 1 \| OR: one of a group \| CS 124 \| false \|<br>\| CS 101 \| option 1 \| OR: one of a group \| MATH 220 \| false \|<br>\| CS 101 \| option 1 \| OR: one of a group \| MATH 221 \| false \|<br>\| CS 101 \| option 1 \| OR: one of a group \| MATH 231 \| false \|<br>\| CS 101 \| option 1 \| OR: one of a group \| MATH 241 \| false \|<br>\| CS 124 \| option 1 \| AND: required course \| MATH 112 \| false \|<br>\| CS 128 \| option 1 \| OR: one of a group \| CS 124 \| false \|<br>\| CS 128 \| option 1 \| OR: one of a group \| CS 125 \| true \|<br>\| CS 173 \| option 1 \| OR: one of a group \| CS 124 \| false \|<br>\| CS 173 \| option 1 \| OR: one of a group \| CS 125 \| true \|<br>\| CS 173 \| option 1 \| OR: one of a group \| ECE 220 \| false \|<br>\| CS 173 \| option 1 \| OR: one of a group \| MATH 220 \| false \|<br>\| CS 173 \| option 1 \| OR: one of a group \| MATH 221 \| false \|<br>\| CS 225 \| option 1 \| OR: one of a group \| CS 126 \| true \|<br>\| CS 225 \| option 1 \| OR: one of a group \| CS 128 \| false \|<br>\| CS 225 \| option 1 \| OR: one of a group \| CS 173 \| false \|<br>\| CS 225 \| option 1 \| OR: one of a group \| CS 413 \| true \|<br>\| CS 225 \| option 1 \| OR: one of a group \| ECE 220 \| false \|<br>\| CS 225 \| option 1 \| OR: one of a group \| MATH 213 \| false \|<br>\| CS 225 \| option 1 \| OR: one of a group \| MATH 314 \| false \|<br>\| CS 225 \| option 1 \| OR: one of a group \| MATH 347 \| true \|<br>\| CS 225 \| option 1 \| OR: one of a group \| MATH 412 \| false \|<br>\| CS 225 \| option 1 \| OR: one of a group \| MATH 413 \| false \|<br>\| CS 233 \| option 1 \| AND: required course \| CS 225 \| false \|<br>\| CS 233 \| option 1 \| OR: one of a group \| CS 125 \| true \|<br>\| CS 233 \| option 1 \| OR: one of a group \| CS 128 \| false \|<br>\| CS 233 \| option 1 \| OR: one of a group \| CS 173 \| false \|<br>\| CS 233 \| option 1 \| OR: one of a group \| MATH 213 \| false \|<br>\| CS 340 \| option 1 \| AND: required course \| CS 128 \| false \|<br>\| CS 340 \| option 1 \| AND: required course \| CS 225 \| false \|<br>\| CS 374 \| option 1 \| AND: required course \| CS 225 \| false \|<br>\| CS 374 \| option 1 \| OR: one of a group \| CS 173 \| false \|<br>\| CS 374 \| option 1 \| OR: one of a group \| MATH 213 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| ASRM 406 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| BIOE 210 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| CS 233 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| CS 240 \| true \|<br>\| CS 421 \| option 1 \| OR: one of a group \| CS 340 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| CS 374 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| ECE 374 \| true \|<br>\| CS 421 \| option 1 \| OR: one of a group \| ECE 391 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| MATH 225 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| MATH 257 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| MATH 415 \| false \|<br>\| CS 421 \| option 1 \| OR: one of a group \| MATH 416 \| false \|<br>\| ECE 220 \| option 1 \| AND: required course \| ECE 120 \| false \|<br>\| ECE 391 \| option 1 \| OR: one of a group \| CS 233 \| false \|<br>\| ECE 391 \| option 1 \| OR: one of a group \| ECE 220 \| false \|<br>\| FIN 221 \| option 1 \| OR: one of a group \| ECON 102 \| true \|<br>\| FIN 221 \| option 1 \| OR: one of a group \| ECON 103 \| true \|<br>\| MATH 115 \| option 1 \| AND: required course \| MATH 112 \| false \|<br>\| MATH 213 \| option 1 \| OR: one of a group \| MATH 220 \| false \|<br>\| MATH 213 \| option 1 \| OR: one of a group \| MATH 221 \| false \|<br>\| MATH 220 \| option 1 \| AND: required course \| MATH 115 \| false \|<br>\| MATH 225 \| option 1 \| OR: one of a group \| MATH 220 \| false \|<br>\| MATH 225 \| option 1 \| OR: one of a group \| MATH 221 \| false \|<br>\| MATH 231 \| option 1 \| OR: one of a group \| MATH 220 \| false \|<br>\| MATH 231 \| option 1 \| OR: one of a group \| MATH 221 \| false \|<br>\| MATH 241 \| option 1 \| AND: required course \| MATH 231 \| false \|<br>\| MATH 257 \| option 1 \| AND: required course \| CS 101 \| false \|<br>\| MATH 257 \| option 1 \| OR: one of a group \| MATH 220 \| false \|<br>\| MATH 257 \| option 1 \| OR: one of a group \| MATH 221 \| false \|<br>\| MATH 314 \| option 1 \| AND: required course \| MATH 241 \| false \|<br>\| MATH 412 \| option 1 \| OR: one of a group \| CS 374 \| false \|<br>\| MATH 412 \| option 1 \| OR: one of a group \| MATH 314 \| false \|<br>\| MATH 412 \| option 1 \| OR: one of a group \| MATH 347 \| true \|<br>\| MATH 413 \| option 1 \| OR: one of a group \| MATH 314 \| false \|<br>\| MATH 413 \| option 1 \| OR: one of a group \| MATH 347 \| true \|<br>\| MATH 415 \| option 1 \| AND: required course \| MATH 241 \| false \|<br>\| MATH 416 \| option 1 \| AND: required course \| MATH 241 \| false \|<br>\| MATH 416 \| option 1 \| OR: one of a group \| MATH 314 \| false \|<br>\| MATH 416 \| option 1 \| OR: one of a group \| MATH 347 \| true \| | No / No | No / Yes |
| CQ03 / Which prerequisite alternatives for a target course are fully met by a given student, and wh ich precise course, standing, or consent conditions remain unmet? Instance: synthetic student S003; target course CS 421; Fall 2026. | [{"option": "https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1", "optionStatus": "not met", "conditionType": "CourseChoiceCondition", "conditionText": "One of CS 233, CS 240, CS 340 or ECE 391", "conditionStatus": "met"}, {"option": "https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1", "optionStatus": "not met", "conditionType": "CourseChoiceCondition", "conditionText": "CS 374 or ECE 374", "conditionStatus": "UNMET / needs review"}, {"option": "https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1", "optionStatus": "not met", "conditionType": "CourseChoiceCondition", "conditionText": "one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210", "conditionStatus": "met"}] | No data is available regarding student S003, course CS 421, or any prerequisite conditions for Fall 2026. Without access to a student transcript, course catalog, or enrollment system, it is impossible to determine which prerequisites are met or unmet, or what specific standing or consent conditions remain.<br><br>Therefore, the query cannot be answered with certainty based on available information.<br><br>**Conclusion:**  <br>- Prerequisite alternatives fully met: Unknown (no data)  <br>- Unmet conditions: Unknown (no data)  <br><br>*Note: This response reflects the absence of retrieval tools or course graph data. No assumptions or inferences are made beyond the stated constraints.* | \| option \| conditionText \| conditionStatus \| optionStatus \| basis \| unmetCondition \| citation \|<br>\|--------\|--------------\|----------------\|-------------\|-------\|----------------\|----------\|<br>\| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 \| One of CS 233, CS 240, CS 340 or ECE 391 \| met \| not met \| completed \| — \| [R1] \|<br>\| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 \| CS 374 or ECE 374 \| UNMET / needs review \| not met \| unverified \| CS 374 or ECE 374 \| [R2] \|<br>\| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| met \| not met \| completed \| — \| [R3] \| | No / Yes | No / Yes |
| CQ04 / If a student completes one additional course, which downstream courses may become available and what other conditions would still have to hold? Instance: synthetic student S002 hypothetically completes CS 225; Fall 2026. | [{"courseCode": "CS 341", "option": "option 1", "status": "still blocked", "stillRequired": "CS 233"}, {"courseCode": "CS 418", "option": "option 1", "status": "still blocked", "stillRequired": "One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| MATH 241"}, {"courseCode": "CS 440", "option": "option 1", "status": "still blocked", "stillRequired": "one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310"}, {"courseCode": "CS 441", "option": "option 1", "status": "still blocked", "stillRequired": "one of CS 361, STAT 361, ECE 313, BIOE 310, MATH 362, MATH 461, MATH 463 or STAT 400"}, {"courseCode": "CS 444", "option": "option 1", "status": "still blocked", "stillRequired": "MATH 241 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400"}, {"courseCode": "CS 445", "option": "option 1", "status": "still blocked", "stillRequired": "CS 225, MATH 225"}, {"courseCode": "CS 446", "option": "option 1", "status": "still blocked", "stillRequired": "One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310"}, {"courseCode": "CS 447", "option": "option 1", "status": "still blocked", "stillRequired": "CS 374 or ECE 374 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210"}, {"courseCode": "CS 463", "option": "option 1", "status": "still blocked", "stillRequired": "one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400"}, {"courseCode": "CS 470", "option": "option 1", "status": "still blocked", "stillRequired": "one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210"}, {"courseCode": "CS 477", "option": "option 1", "status": "still blocked", "stillRequired": "one of CS 374, ECE 374 or MATH 414"}, {"courseCode": "ADV 492", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 210", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 211", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 233", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 340", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 374", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 409", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 410", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 411", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 412", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 415", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 452", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 464", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 465", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "CS 466", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "ECE 407", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}, {"courseCode": "ECE 549", "option": "option 1", "status": "would become satisfiable", "stillRequired": ""}] | No downstream courses become available, and no additional conditions are triggered.<br><br>Reasoning:  <br>The scenario specifies only that a student completes CS 225 in Fall 2026. However, no course prerequisites, downstream dependencies, or availability rules are provided in the query or context. Without explicit information about course prerequisites, co-requisites, or academic pathways (e.g., "CS 225 is required for CS 330"), it is impossible to determine which downstream courses may become available.<br><br>Additionally, even if CS 225 were a prerequisite for another course, the absence of a stated dependency or course structure means we cannot infer downstream availability.<br><br>Therefore, based on the given information:<br><br>- No downstream courses are known to become available.<br>- No conditions beyond the completion of CS 225 are specified or verifiable.<br>- The student’s academic pathway, degree requirements, or university policy are not provided.<br><br>Conclusion:  <br>Without explicit prerequisite or dependency rules, downstream course availability cannot be determined. The condition "a student completes one additional course" does not trigger any known downstream outcomes in this context.<br><br>> ⚠️ Uncertainty: Missing course dependency data.  <br>> ⚠️ Missing academic policy or curriculum structure.  <br>> ⚠️ No evidence of CS 225 being a prerequisite for any downstream course.  <br><br>Thus, no downstream courses are identified, and no additional conditions are known to hold. | \| courseCode \| status \| stillRequired \| citation \|<br>\|-----------\|--------\|--------------\|---------\|<br>\| CS 341 \| still blocked \| CS 233 \| [R1] \|<br>\| CS 418 \| still blocked \| One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \\| MATH 241 \| [R2] \|<br>\| CS 440 \| still blocked \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 \| [R3] \|<br>\| CS 441 \| still blocked \| one of CS 361, STAT 361, ECE 313, BIOE 310, MATH 362, MATH 461, MATH 463 or STAT 400 \| [R4] \|<br>\| CS 444 \| still blocked \| MATH 241 \\| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \\| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 \| [R5] \|<br>\| CS 445 \| still blocked \| CS 225, MATH 225 \| [R6] \|<br>\| CS 446 \| still blocked \| One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 \\| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 \| [R7] \|<br>\| CS 447 \| still blocked \| CS 374 or ECE 374 \\| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 \\| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 \| [R8] \|<br>\| CS 463 \| still blocked \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 \| [R9] \|<br>\| CS 470 \| still blocked \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 \\| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| [R10] \|<br>\| CS 477 \| still blocked \| one of CS 374, ECE 374 or MATH 414 \| [R11] \|<br>\| ADV 492 \| would become satisfiable \| \| [R12] \|<br>\| CS 210 \| would become satisfiable \| \| [R13] \|<br>\| CS 211 \| would become satisfiable \| \| [R14] \|<br>\| CS 233 \| would become satisfiable \| \| [R15] \|<br>\| CS 340 \| would become satisfiable \| \| [R16] \|<br>\| CS 374 \| would become satisfiable \| \| [R17] \|<br>\| CS 409 \| would become satisfiable \| \| [R18] \|<br>\| CS 410 \| would become satisfiable \| \| [R19] \|<br>\| CS 411 \| would become satisfiable \| \| [R20] \|<br>\| CS 412 \| would become satisfiable \| \| [R21] \|<br>\| CS 415 \| would become satisfiable \| \| [R22] \|<br>\| CS 452 \| would become satisfiable \| \| [R23] \|<br>\| CS 464 \| would become satisfiable \| \| [R24] \|<br>\| CS 465 \| would become satisfiable \| \| [R25] \|<br>\| CS 466 \| would become satisfiable \| \| [R26] \|<br>\| ECE 407 \| would become satisfiable \| \| [R27] \|<br>\| ECE 549 \| would become satisfiable \| \| [R28] \| | No / Yes | No / Yes |
| CQ06 / How many courses and credit hours are still needed in each core or elective group for a given student and degree-program catalog year? Instance: synthetic student S003; program UIUC BS CS, catalog year 2026. | [{"requirement": "Technical electives (min 6 courses, 18 hours)", "minCourses": "6", "allocatedCourses": "0", "remainingCourses": "6", "minCredits": "18.0", "allocatedCredits": "0"}, {"requirement": "CS technical core (11 courses, 35 hours)", "minCourses": "11", "allocatedCourses": "6", "remainingCourses": "5", "minCredits": "35.0", "allocatedCredits": "18.0"}, {"requirement": "Focus area: Algorithms and Models of Computation", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Focus area: Distributed Systems, Networking, and Security", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Focus area: Human and Social Impact", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Focus area: Intelligence and Big Data", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Focus area: Machines", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Focus area: Media", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Focus area: Scientific, Parallel, and High Performance Computing", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Focus area: Software Foundations", "minCourses": "3", "allocatedCourses": "0", "remainingCourses": "3", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Advanced electives (min 2 courses, 6 hours)", "minCourses": "2", "allocatedCourses": "0", "remainingCourses": "2", "minCredits": "6.0", "allocatedCredits": "0"}, {"requirement": "Ethical and professional issues: CS 210 or CS 211", "minCourses": "1", "allocatedCourses": "0", "remainingCourses": "1", "minCredits": "2.0", "allocatedCredits": "0"}, {"requirement": "Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212", "minCourses": "4", "allocatedCourses": "3", "remainingCourses": "1", "minCredits": "15.0", "allocatedCredits": "11.0"}, {"requirement": "Science elective (one Natural Science & Technology course)", "minCourses": "1", "allocatedCourses": "0", "remainingCourses": "1", "minCredits": "3.0", "allocatedCredits": "0"}, {"requirement": "Team project course (at least 1 of the technical electives)", "minCourses": "1", "allocatedCourses": "0", "remainingCourses": "1", "minCredits": null, "allocatedCredits": "0"}, {"requirement": "Calculus I: MATH 221 (MATH 220 may be substituted)", "minCourses": "1", "allocatedCourses": "1", "remainingCourses": "0", "minCredits": "4.0", "allocatedCredits": "4.0"}, {"requirement": "Linear algebra: MATH 257, MATH 415 or MATH 416", "minCourses": "1", "allocatedCourses": "1", "remainingCourses": "0", "minCredits": "3.0", "allocatedCredits": "3.0"}, {"requirement": "Orientation: ENG 100", "minCourses": "1", "allocatedCourses": "1", "remainingCourses": "0", "minCredits": "1.0", "allocatedCredits": "1.0"}] | I cannot provide the number of courses and credit hours still needed for student S003 in the UIUC BS CS program for catalog year 2026, as no student transcript, course enrollment data, or program-specific curriculum details have been provided. <br><br>To determine remaining course and credit requirements, I would need:<br><br>- The student’s current course enrollment or transcript (including completed and pending courses)<br>- The official degree program curriculum for UIUC BS CS in catalog year 2026<br>- The specific core and elective group breakdowns (e.g., math, CS core, electives)<br>- Prerequisites and graduation requirements for that catalog year<br><br>Without this information, any calculation is speculative.<br><br>**Conclusion**: Insufficient data to determine remaining courses and credit hours.  <br>→ **No answer possible with current information.** | \| Requirement \| Min Courses \| Allocated Courses \| Remaining Courses \| Min Credits \| Allocated Credits \| Remaining Credits \|<br>\|-----------\|-------------\|-------------------\|-------------------\|-------------\|-------------------\|-------------------\|<br>\| CS technical core (11 courses, 35 hours) \| 11 \| 6 \| 5 \| 35.0 \| 18.0 \| 17.0 \|<br>\| Ethical and professional issues: CS 210 or CS 211 \| 1 \| 0 \| 1 \| 2.0 \| 0.0 \| 2.0 \|<br>\| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 \| 4 \| 3 \| 1 \| 15.0 \| 11.0 \| 4.0 \|<br>\| Advanced electives (min 2 courses, 6 hours) \| 2 \| 0 \| 2 \| 6.0 \| 0.0 \| 6.0 \|<br>\| Focus area: Algorithms and Models of Computation \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Focus area: Distributed Systems, Networking, and Security \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Focus area: Human and Social Impact \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Focus area: Intelligence and Big Data \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Focus area: Machines \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Focus area: Media \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Focus area: Scientific, Parallel, and High Performance Computing \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Focus area: Software Foundations \| 3 \| 0 \| 3 \| null \| 0.0 \| null \|<br>\| Science elective (one Natural Science & Technology course) \| 1 \| 0 \| 1 \| 3.0 \| 0.0 \| 3.0 \|<br>\| Team project course (at least 1 of the technical electives) \| 1 \| 0 \| 1 \| null \| 0.0 \| null \|<br>\| Technical electives (min 6 courses, 18 hours) \| 6 \| 0 \| 6 \| 18.0 \| 0.0 \| 18.0 \| | No / No | No / Yes |
| CQ08 / Which courses are at least two prerequisite-course links upstream of a selected target course, and through which alternative branches are they reachable? Instance: CS 440. | [{"upstreamCode": "BIOE 210", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "CS 101", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "CS 101", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "CS 124", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "CS 124", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "CS 125", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "CS 126", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "CS 128", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "CS 173", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "CS 374", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "CS 413", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "ECE 120", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "ECE 220", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 112", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 112", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 112", "viaCode": "CS 361", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 112", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 112", "viaCode": "MATH 461", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 112", "viaCode": "STAT 400", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 115", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 115", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 115", "viaCode": "CS 361", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 115", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 115", "viaCode": "MATH 461", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 115", "viaCode": "STAT 400", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 213", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 220", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 220", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 220", "viaCode": "CS 361", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 220", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 220", "viaCode": "MATH 461", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 220", "viaCode": "STAT 400", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 221", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 221", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 221", "viaCode": "CS 361", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 221", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 221", "viaCode": "MATH 461", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 221", "viaCode": "STAT 400", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 231", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 231", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 231", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 231", "viaCode": "MATH 461", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 231", "viaCode": "STAT 400", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 241", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 241", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 241", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 241", "viaCode": "MATH 461", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 257", "viaCode": "BIOE 310", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 257", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 314", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 314", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 347", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 347", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}, {"upstreamCode": "MATH 412", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 413", "viaCode": "CS 225", "firstHop": "via required course"}, {"upstreamCode": "MATH 416", "viaCode": "ECE 313", "firstHop": "via one-of group (potential)"}] | None of the courses are known to be at least two prerequisite-course links upstream of CS 440, and no alternative branches are documented in the available course data.<br><br>Reasoning:  <br>- The query asks for courses that are at least two prerequisite links upstream of CS 440.  <br>- Without a course prerequisite graph or database, we cannot trace prerequisite chains or determine upstream dependencies.  <br>- No course graph or transcript data is provided to evaluate prerequisite relationships or alternative pathways.  <br>- Therefore, no courses can be identified as satisfying the "at least two prerequisite links upstream" condition.  <br>- Similarly, no alternative branches are reachable due to lack of structural or dependency information.<br><br>Conclusion:  <br>No such courses exist in the available data.  <br>Alternative branches cannot be determined due to missing prerequisite structure.<br><br>Note: This response is based solely on the absence of provided course data and cannot infer relationships without a course dependency graph. | \| upstreamCode \| viaCode  \| firstHop                     \|<br>\|-------------\|----------\|-----------------------------\|<br>\| BIOE 210    \| BIOE 310 \| via one-of group (potential)\|<br>\| CS 101      \| BIOE 310 \| via one-of group (potential)\|<br>\| CS 101      \| ECE 313  \| via one-of group (potential)\|<br>\| CS 124      \| BIOE 310 \| via one-of group (potential)\|<br>\| CS 124      \| CS 225   \| via required course        \|<br>\| CS 125      \| CS 225   \| via required course        \|<br>\| CS 126      \| CS 225   \| via required course        \|<br>\| CS 128      \| CS 225   \| via required course        \|<br>\| CS 173      \| CS 225   \| via required course        \|<br>\| CS 374      \| CS 225   \| via required course        \|<br>\| CS 413      \| CS 225   \| via required course        \|<br>\| ECE 120     \| CS 225   \| via required course        \|<br>\| ECE 220     \| CS 225   \| via required course        \|<br>\| MATH 112    \| BIOE 310 \| via one-of group (potential)\|<br>\| MATH 112    \| CS 225   \| via required course        \|<br>\| MATH 112    \| CS 361   \| via one-of group (potential)\|<br>\| MATH 112    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 112    \| MATH 461 \| via one-of group (potential)\|<br>\| MATH 112    \| STAT 400 \| via one-of group (potential)\|<br>\| MATH 115    \| BIOE 310 \| via one-of group (potential)\|<br>\| MATH 115    \| CS 225   \| via required course        \|<br>\| MATH 115    \| CS 361   \| via one-of group (potential)\|<br>\| MATH 115    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 115    \| MATH 461 \| via one-of group (potential)\|<br>\| MATH 115    \| STAT 400 \| via one-of group (potential)\|<br>\| MATH 213    \| CS 225   \| via required course        \|<br>\| MATH 220    \| BIOE 310 \| via one-of group (potential)\|<br>\| MATH 220    \| CS 225   \| via required course        \|<br>\| MATH 220    \| CS 361   \| via one-of group (potential)\|<br>\| MATH 220    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 220    \| MATH 461 \| via one-of group (potential)\|<br>\| MATH 220    \| STAT 400 \| via one-of group (potential)\|<br>\| MATH 221    \| BIOE 310 \| via one-of group (potential)\|<br>\| MATH 221    \| CS 225   \| via required course        \|<br>\| MATH 221    \| CS 361   \| via one-of group (potential)\|<br>\| MATH 221    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 221    \| MATH 461 \| via one-of group (potential)\|<br>\| MATH 221    \| STAT 400 \| via one-of group (potential)\|<br>\| MATH 231    \| BIOE 310 \| via one-of group (potential)\|<br>\| MATH 231    \| CS 225   \| via required course        \|<br>\| MATH 231    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 231    \| MATH 461 \| via one-of group (potential)\|<br>\| MATH 231    \| STAT 400 \| via one-of group (potential)\|<br>\| MATH 241    \| BIOE 310 \| via one-of group (potential)\|<br>\| MATH 241    \| CS 225   \| via required course        \|<br>\| MATH 241    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 241    \| MATH 461 \| via one-of group (potential)\|<br>\| MATH 257    \| BIOE 310 \| via one-of group (potential)\|<br>\| MATH 257    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 314    \| CS 225   \| via required course        \|<br>\| MATH 314    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 347    \| CS 225   \| via required course        \|<br>\| MATH 347    \| ECE 313  \| via one-of group (potential)\|<br>\| MATH 412    \| CS 225   \| via required course        \|<br>\| MATH 413    \| CS 225   \| via required course        \|<br>\| MATH 416    \| ECE 313  \| via one-of group (potential)\|<br>[R1], [R2], [R3], [R4], [R5], [R6], [R7], [R8], [R9], [R10], [R11], [R12], [R13], [R14], [R15], [R16], [R17], [R18], [R19], [R20], [R21], [R22], [R23], [R24], [R25], [R26], [R27], [R28], [R29], [R30], [R31], [R32], [R33], [R34], [R35], [R36], [R37], [R38], [R39], [R40], [R41], [R42], [R43], [R44], [R45], [R46], [R47], [R48], [R49], [R50], [R51], [R52], [R53], [R54], [R55], [R56] | No / Yes | No / Yes |
| CQ10 / For a selected course, which cross-listed course codes and downstream prerequisites reference its codes, and are any substitutions still subject to explicit policy? Instance: CS 374. | [{"alias": "ECE 374", "downstreamCode": "CS 421", "mentions": "CS 374, ECE 374", "acceptsBothCodes": "true"}, {"alias": "ECE 374", "downstreamCode": "CS 447", "mentions": "CS 374, ECE 374", "acceptsBothCodes": "true"}, {"alias": "ECE 374", "downstreamCode": "CS 473", "mentions": "CS 374, ECE 374", "acceptsBothCodes": "true"}, {"alias": "ECE 374", "downstreamCode": "CS 475", "mentions": "CS 374, ECE 374", "acceptsBothCodes": "true"}, {"alias": "ECE 374", "downstreamCode": "CS 477", "mentions": "CS 374, ECE 374", "acceptsBothCodes": "true"}, {"alias": "ECE 374", "downstreamCode": "CS 521", "mentions": "CS 374, ECE 374", "acceptsBothCodes": "true"}, {"alias": "ECE 374", "downstreamCode": "CS 581", "mentions": "CS 374, ECE 374", "acceptsBothCodes": "true"}, {"alias": "ECE 374", "downstreamCode": "MATH 412", "mentions": "CS 374", "acceptsBothCodes": "false"}, {"alias": "ECE 374", "downstreamCode": "MATH 417", "mentions": "CS 374", "acceptsBothCodes": "false"}] | No information is available regarding cross-listed course codes, downstream prerequisites, or substitution policies for CS 374 or any course in the absence of a course catalog, university database, or official academic policy document.<br><br>Therefore, I cannot provide:<br><br>- Cross-listed course codes that reference CS 374  <br>- Downstream prerequisites that depend on CS 374  <br>- Whether substitutions are subject to explicit policy  <br><br>This query requires access to a university’s official course catalog or academic policy repository, which is not available here.<br><br>**Conclusion**: Uncertain. No data provided. Requested information cannot be retrieved or verified without official course records. | \| cross-listed_code \| downstream_prerequisite \| substitution_policy_status \|<br>\|------------------\|------------------------\|----------------------------\|<br>\| ECE 374          \| CS 421                \| acceptsBothCodes=true     \|<br>\| ECE 374          \| CS 447                \| acceptsBothCodes=true     \|<br>\| ECE 374          \| CS 473                \| acceptsBothCodes=true     \|<br>\| ECE 374          \| CS 475                \| acceptsBothCodes=true     \|<br>\| ECE 374          \| CS 477                \| acceptsBothCodes=true     \|<br>\| ECE 374          \| CS 521                \| acceptsBothCodes=true     \|<br>\| ECE 374          \| MATH 412              \| acceptsBothCodes=false    \|<br>\| ECE 374          \| MATH 417              \| acceptsBothCodes=false    \|<br><br>*Result Guide: "acceptsBothCodes=true" means both codes are explicitly mentioned in the downstream prerequisite. "false" means explicit acceptance of both was NOT established; it does NOT mean substitution is forbidden. Cross-listing alone does not establish general substitution policy.* | No / No | No / Yes |
| CQ11 / For each department, how many available courses could fulfill a particular  elective group in a selected term? Instance: advanced elective group; Fall 2026. | [{"department": "CS", "advancedElectivesOfferedFall2026": "50"}, {"department": "ECE", "advancedElectivesOfferedFall2026": "46"}, {"department": "MATH", "advancedElectivesOfferedFall2026": "30"}, {"department": "STAT", "advancedElectivesOfferedFall2026": "19"}, {"department": "PHYS", "advancedElectivesOfferedFall2026": "17"}, {"department": "CSE", "advancedElectivesOfferedFall2026": "12"}, {"department": "ASRM", "advancedElectivesOfferedFall2026": "5"}, {"department": "PHIL", "advancedElectivesOfferedFall2026": "3"}, {"department": "BIOE", "advancedElectivesOfferedFall2026": "2"}, {"department": "MSE", "advancedElectivesOfferedFall2026": "2"}, {"department": "ADV", "advancedElectivesOfferedFall2026": "1"}, {"department": "AE", "advancedElectivesOfferedFall2026": "1"}, {"department": "IE", "advancedElectivesOfferedFall2026": "1"}, {"department": "ME", "advancedElectivesOfferedFall2026": "1"}, {"department": "NE", "advancedElectivesOfferedFall2026": "1"}, {"department": "TAM", "advancedElectivesOfferedFall2026": "1"}] | I cannot provide a specific answer to your question because:<br><br>- There is no available course data or departmental course catalog provided.<br>- No term (e.g., Fall 2026) or elective group (e.g., advanced elective group) is defined in the context of a university curriculum.<br>- No departmental course offerings or prerequisites are specified.<br><br>Therefore, I cannot determine how many available courses in each department could fulfill a particular elective group in a selected term.<br><br>To answer this question accurately, I would need:<br>- A list of departments and their offered courses.<br>- A defined set of elective groups (e.g., advanced, humanities, science).<br>- A schedule of course availability by term (e.g., Fall 2026).<br>- Prerequisite or enrollment constraints.<br><br>Without such data, the query cannot be resolved.<br><br>**Conclusion**: Insufficient information to determine available courses per department for a specific elective group in a term. | \| department \| available_courses_for_advanced_elective_group_fall_2026 \|<br>\|---\|---\|<br>\| CS \| 50 \|<br>\| ECE \| 46 \|<br>\| MATH \| 30 \|<br>\| STAT \| 19 \|<br>\| PHYS \| 17 \|<br>\| CSE \| 12 \|<br>\| ASRM \| 5 \|<br>\| PHIL \| 3 \|<br>\| BIOE \| 2 \|<br>\| MSE \| 2 \|<br>\| ADV \| 1 \|<br>\| AE \| 1 \|<br>\| IE \| 1 \|<br>\| ME \| 1 \|<br>\| NE \| 1 \|<br>\| TAM \| 1 \| | No / Yes | No / Yes |
| CQ13 / How does the set of satisfiable prerequisite options and course recommendations change when one planned completion is hypothetically added to a student's transcript? Instance: synthetic student S002 hypothetically adds CS 225; Fall 2026. | [{"courseCode": "ADV 492", "title": "Tech and Advertising Campaigns", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 210", "title": "Ethical & Professional Issues", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 211", "title": "Ethical and Professional Conduct", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 233", "title": "Computer Architecture", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 340", "title": "Introduction to Computer Systems", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 374", "title": "Introduction to Algorithms & Models of Computation", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 409", "title": "The Art of Web Programming", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 410", "title": "Text Information Systems", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 411", "title": "Database Systems", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 412", "title": "Introduction to Data Mining", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 415", "title": "Game Development", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 452", "title": "Topics in Robotics", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 464", "title": "Topics in Societal and Ethical Impacts of Computer Technology", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 465", "title": "User Interface Design", "eligibleIn": "plus CS 225"}, {"courseCode": "CS 466", "title": "Introduction to Bioinformatics", "eligibleIn": "plus CS 225"}, {"courseCode": "ECE 407", "title": "Cryptography", "eligibleIn": "plus CS 225"}, {"courseCode": "ECE 549", "title": "Computer Vision", "eligibleIn": "plus CS 225"}] | No retrievable data or course graph is available to assess how the set of satisfiable prerequisite options or course recommendations changes when a hypothetical course completion (e.g., CS 225, Fall 2026) is added to a student's transcript.<br><br>Therefore, based on the provided information:<br><br>- There is no access to a student transcript or course prerequisite graph.<br>- No prior course history or academic plan for student S002 is available.<br>- No rules or logic for evaluating prerequisite satisfaction or course recommendations are provided.<br><br>**Conclusion:**  <br>The impact of adding CS 225 (Fall 2026) to student S002’s transcript cannot be determined without access to the course prerequisite structure, current transcript, or recommendation logic.<br><br>**Uncertainty:**  <br>- The prerequisite relationships for CS 225 are unknown.  <br>- Whether CS 225 is a prerequisite for other courses or a result of prior course work is not specified.  <br>- No data exists to evaluate how this addition affects satisfiable options or recommendations.<br><br>Thus, **no change** can be assessed — **no information is available to compute or infer any change**. | \| courseCode \| title \| eligibleIn \| citation \|<br>\|-----------\|------\|-----------\|---------\|<br>\| ADV 492 \| Tech and Advertising Campaigns \| plus CS 225 \| [R1] \|<br>\| CS 210 \| Ethical & Professional Issues \| plus CS 225 \| [R2] \|<br>\| CS 211 \| Ethical and Professional Conduct \| plus CS 225 \| [R3] \|<br>\| CS 233 \| Computer Architecture \| plus CS 225 \| [R4] \|<br>\| CS 340 \| Introduction to Computer Systems \| plus CS 225 \| [R5] \|<br>\| CS 374 \| Introduction to Algorithms & Models of Computation \| plus CS 225 \| [R6] \|<br>\| CS 409 \| The Art of Web Programming \| plus CS 225 \| [R7] \|<br>\| CS 410 \| Text Information Systems \| plus CS 225 \| [R8] \|<br>\| CS 411 \| Database Systems \| plus CS 225 \| [R9] \|<br>\| CS 412 \| Introduction to Data Mining \| plus CS 225 \| [R10] \|<br>\| CS 415 \| Game Development \| plus CS 225 \| [R11] \|<br>\| CS 452 \| Topics in Robotics \| plus CS 225 \| [R12] \|<br>\| CS 464 \| Topics in Societal and Ethical Impacts of Computer Technology \| plus CS 225 \| [R13] \|<br>\| CS 465 \| User Interface Design \| plus CS 225 \| [R14] \|<br>\| CS 466 \| Introduction to Bioinformatics \| plus CS 225 \| [R15] \|<br>\| ECE 407 \| Cryptography \| plus CS 225 \| [R16] \|<br>\| ECE 549 \| Computer Vision \| plus CS 225 \| [R17] \|<br><br>**Change Summary under Hypothetical Completion of CS 225 (Fall 2026):**  <br>All 17 courses listed above become *eligible* due to the prerequisite condition "plus CS 225". This hypothetical completion satisfies the prerequisite for each of these courses, enabling their inclusion in the student’s course recommendations.  <br>- **Newly satisfied prerequisites**: 17 courses (as per `newly_satisfied` in reasoning).  <br>- **Downstream candidates**: 71 (as per `downstream_course_count` in reasoning).  <br>- **Note**: The stored KG remains unchanged; this evaluation is a memory-based what-if.  <br>- **Unverified**: No course has a prerequisite that does not depend on CS 225; all listed prerequisites are explicitly tied to CS 225.  <br>- **Missing evidence**: 1130 RDF edges omitted; no impact on this query result.  <br><br>*All entries are derived from the `eligibleIn` field and verified via explicit prerequisite conditions in the context.* | No / No | No / No |
| CQ15 / What catalog wording, degree requirement and prerequisite-option evidence s upports each recommendation, and which conditions remain unverified? Instance: synthetic student S002's planned courses; Fall 2026. | [{"courseCode": "CS 225", "prerequisiteText": "CS 126 or CS 128 or ECE 220; One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413.", "parseStatus": "parsed", "satisfiedOptions": "1", "requirement": "CS technical core (11 courses, 35 hours)", "requirementNote": "Technical GPA of 2.0 is required for CS and Math courses.", "source": "https://discovery.cs.illinois.edu/dataset/course-catalog/", "unverified": "none"}, {"courseCode": "MATH 241", "prerequisiteText": "MATH 231.", "parseStatus": "parsed", "satisfiedOptions": "1", "requirement": "Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212", "requirementNote": null, "source": "https://discovery.cs.illinois.edu/dataset/course-catalog/", "unverified": "none"}, {"courseCode": "MATH 257", "prerequisiteText": "MATH 220 or MATH 221; CS 101 or equivalent programming experience.", "parseStatus": "needs_review", "satisfiedOptions": "0", "requirement": "Linear algebra: MATH 257, MATH 415 or MATH 416", "requirementNote": null, "source": "https://discovery.cs.illinois.edu/dataset/course-catalog/", "unverified": "yes: wording such as 'or equivalent' needs manual check"}] | No catalog wording, degree requirement, or prerequisite-option evidence is available for student S002's planned courses in Fall 2026. No course data, transcripts, or institutional records have been provided to support any recommendations, verify prerequisites, or confirm degree requirements.<br><br>Therefore, all claims—regarding catalog wording, degree requirements, or prerequisite options—remain unverified. No instance of a student (e.g., S002) or course schedule has been presented or accessible for analysis.<br><br>**Unverified conditions:**<br>- Catalog wording for any course or requirement<br>- Degree requirement alignment (e.g., major, minor, graduation criteria)<br>- Prerequisite options for specific courses<br>- Course sequencing or academic plan validity<br><br>**Conclusion:**  <br>No evidence is available to support any recommendation for student S002 in Fall 2026. All conditions remain unverified due to lack of input data. | \| Course Code \| Catalog Wording \| Degree Requirement \| Prerequisite Option Evidence \| Unverified Conditions \| R-number \|<br>\|------------\|----------------\|--------------------\|-------------------------------\|------------------------\|---------\|<br>\| CS 225 \| Prerequisites: CS 126 or CS 128 or ECE 220; One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413. \| CS technical core (11 courses, 35 hours); Technical GPA of 2.0 required for CS and Math courses. \| Satisfied: CS 128 (completed), CS 173 (completed). \| none \| [R1] \|<br>\| MATH 241 \| Prerequisite: MATH 231. \| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212. \| Satisfied: MATH 231 (completed). \| none \| [R2] \|<br>\| MATH 257 \| Prerequisite: MATH 220 or MATH 221; CS 101 or equivalent programming experience. \| Linear algebra: MATH 257, MATH 415 or MATH 416. \| Partially satisfied: MATH 221 (completed); CS 101 programming experience unverified. \| CS 101 or equivalent programming experience (unverified) \| [R3] \| | No / Yes | No / Yes |

Scored totals: {"status": "human_review_complete", "questions": 10, "conditions": {"A": {"correct": 0, "evidence": 0, "unsupported_claims": 6, "llm_called": 10}, "B": {"correct": 6, "evidence": 9, "unsupported_claims": 1, "llm_called": 10}}}

Grounding helped: CQ01, CQ03, CQ04, CQ08, CQ11, CQ15.

Grounding worsened: none in this run.

Both correct: none in this run.

Both incorrect: CQ02, CQ06, CQ10, CQ13.


# Recorded error and unsupported-claim analysis

CQ01 A — Hassan Tariq: The answer explains that the transcript and catalog are unavailable. It does not invent course choices, but it does not answer which courses S002 can take.

CQ01 B — Hassan Tariq: All 15 expected courses, titles and satisfied-option counts are present. The earlier incorrect total is gone. The row citations and saved graph evidence support the list.

CQ02 A — Diya Hurmat: The model cannot identify prerequisite chains without the catalog. This is a reasonable refusal, but it does not provide the requested chains or alternatives.

CQ02 B — Diya Hurmat: The 76 returned direct edges match the expected rows, but three of 79 edges are missing: ASRM 210 to MATH 231, ASRM 406 to MATH 241, and BIOE 210 to MATH 231. The answer is incomplete. These omissions are not invented claims. Full graph paths and group structure remain available in the saved retrieval artifact.

CQ03 A — Hassan Tariq: The answer identifies the missing transcript and prerequisite data without guessing. It does not establish which CS 421 conditions are met or unmet for S003.

CQ03 B — Hassan Tariq: All three prerequisite conditions have the expected status. The CS 374 or ECE 374 condition remains unmet, so option 1 is not met. The response does not turn that result into an official registration decision. Its row citations and completion evidence support the assessment.

CQ04 A — Diya Hurmat: The answer eventually acknowledges missing dependency data, but its opening makes two unsupported negative claims: (1) no downstream courses become available, and (2) no additional conditions are triggered. The expected results contain satisfiable downstream courses and remaining conditions. A lack of access cannot establish either negative conclusion.

CQ04 B — Diya Hurmat: All 28 expected rows are included. The answer separates the 11 still-blocked rows from the 17 rows that would become satisfiable and preserves the remaining conditions. The citations support the rows. The hypothetical scenario comes from the question. This checks agreement with the frozen expected rows rather than independently validating the catalog parser.

CQ06 A — Hassan Tariq: The model correctly avoids calculating progress without a transcript and degree structure. It provides no requirement-group results, so it does not answer the question.

CQ06 B — Hassan Tariq: The 15 displayed requirement groups agree with the expected figures, but the answer omits the completed Calculus I, Linear algebra and Orientation groups. The question asks for each group, including groups with zero remaining courses. The saved evidence supports the displayed figures, but the set is incomplete.

CQ08 A — Diya Hurmat: Most of the response describes missing prerequisite data. However, the statement that no alternative branches are reachable because structural information is missing is an unsupported negative reachability claim. The absence of access cannot establish that no path exists. The answer provides none of the expected upstream results.

CQ08 B — Diya Hurmat: All 56 expected upstream-course, intermediate-course and branch-type rows are reproduced exactly. This fixes the previous false empty-result answer. The row citations and saved graph evidence support the traversal results.

CQ10 A — Hassan Tariq: The model states that it lacks the catalog and substitution policy. It does not invent a cross-listing or policy, but it provides none of the requested downstream references.

CQ10 B — Hassan Tariq: The answer correctly explains that failure to establish acceptance of both codes is not a substitution ban. However, CS 581 is missing, leaving eight of nine expected downstream rows. The answer is incomplete. Its displayed references have supporting provenance in the saved artifact.

CQ11 A — Diya Hurmat: The answer refuses to provide counts without course data. It also incorrectly says that (1) no term and (2) no elective group are defined in the supplied context. The question explicitly identifies Fall 2026 and the advanced elective group. Their definitions and membership may be unavailable, but their identities are provided. No departmental counts are returned.

CQ11 B — Diya Hurmat: All 16 departments and their expected counts are present. The response does not add an unsupported total or policy. The saved derived rows and inferred graph evidence support the aggregate, although the answer itself omits inline row citations.

CQ13 A — Hassan Tariq: The answer explains that it cannot calculate a hypothetical change without the transcript and prerequisite graph. It avoids inventing recommendations but does not provide the requested change.

CQ13 B — Hassan Tariq: All 17 expected course rows are correct, and the answer distinguishes these from 71 downstream candidates. However, it adds one unsupported blanket claim: no course has a prerequisite independent of CS 225. Becoming eligible after adding CS 225 does not establish that all other prerequisites depend on CS 225. The table has supporting evidence, but that added conclusion does not, so the complete answer fails the correctness and supporting-evidence checks.

CQ15 A — Diya Hurmat: The model has no transcript or catalog evidence and does not answer the requested question. It also incorrectly says that no student instance or course schedule has been presented. The question identifies S002 and Fall 2026. The detailed planned courses are unavailable to the baseline, but the student instance is provided.

CQ15 B — Diya Hurmat: All three planned courses are covered. The answer gives the catalog wording, degree requirement and supporting prerequisite completions. It keeps the CS 101 or equivalent programming-experience condition for MATH 257 unverified. The row citations and recorded completion codes support the answer, and it does not invent an official registration decision.


# CQ01 — verified expected rows

Given a student's completed courses and a target term, which catalog courses are offered in that term and have a satisfied prerequisite alternative? Instance: synthetic student S002; target term Fall 2026.

| courseCode | title | satisfiedOptions |
| --- | --- | --- |
| ASRM 210 | Theory of Interest | 1 |
| BIOE 210 | Linear Algebra for Biomedical Data Science | 1 |
| CS 101 | Intro Computing: Engrg & Sci | 1 |
| CS 225 | Data Structures | 1 |
| CS 233 | Computer Architecture | 1 |
| CS 361 | Probability & Statistics for Computer Science | 1 |
| CS 427 | Software Engineering I | 1 |
| IE 310 | Deterministic Models in Optimization | 1 |
| MATH 213 | Basic Discrete Mathematics | 1 |
| MATH 225 | Introductory Matrix Theory | 1 |
| MATH 241 | Calculus III | 1 |
| PHYS 100 | Thinking About Physics | 1 |
| PHYS 212 | University Physics: Elec & Mag | 1 |
| PHYS 213 | Univ Physics: Thermal Physics | 1 |
| STAT 400 | Statistics and Probability I | 1 |


# CQ01 condition A — full supplied model answer

No catalog data or student transcript information is provided. Therefore, it is impossible to determine which courses are offered in Fall 2026 or whether any prerequisites are satisfied for student S002.

To answer the question, the following information is required:

- The university course catalog (with course offerings by term)
- The student’s completed courses (to evaluate prerequisite satisfaction)
- Prerequisite rules (including alternative pathways) for each course

Without this data, no valid conclusion can be drawn.

**Conclusion**: Insufficient information to determine catalog courses offered in Fall 2026 with satisfied prerequisite alternatives for student S002.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ01 condition B — full supplied model answer

| courseCode | title | satisfiedOptions | citation |
|-----------|------|------------------|---------|
| ASRM 210 | Theory of Interest | 1 | [R1] |
| BIOE 210 | Linear Algebra for Biomedical Data Science | 1 | [R2] |
| CS 101 | Intro Computing: Engrg & Sci | 1 | [R3] |
| CS 225 | Data Structures | 1 | [R4] |
| CS 233 | Computer Architecture | 1 | [R5] |
| CS 361 | Probability & Statistics for Computer Science | 1 | [R6] |
| CS 427 | Software Engineering I | 1 | [R7] |
| IE 310 | Deterministic Models in Optimization | 1 | [R8] |
| MATH 213 | Basic Discrete Mathematics | 1 | [R9] |
| MATH 225 | Introductory Matrix Theory | 1 | [R10] |
| MATH 241 | Calculus III | 1 | [R11] |
| PHYS 100 | Thinking About Physics | 1 | [R12] |
| PHYS 212 | University Physics: Elec & Mag | 1 | [R13] |
| PHYS 213 | Univ Physics: Thermal Physics | 1 | [R14] |
| STAT 400 | Statistics and Probability I | 1 | [R15] |

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ02 — verified expected rows

For a selected course, what are its possible prerequisite chains back to courses with no recorded course prerequisites, preserving AND/OR branches? Instance: CS 421.

| fromCode | option | edgeType | toCode | toIsBaseCourse |
| --- | --- | --- | --- | --- |
| ASRM 210 | option 1 | AND: required course | MATH 231 | false |
| ASRM 406 | option 1 | AND: required course | MATH 241 | false |
| ASRM 406 | option 1 | OR: one of a group | ASRM 210 | false |
| ASRM 406 | option 1 | OR: one of a group | FIN 221 | false |
| ASRM 406 | option 1 | OR: one of a group | MATH 210 | true |
| BIOE 210 | option 1 | AND: required course | MATH 231 | false |
| BIOE 210 | option 1 | OR: one of a group | CS 101 | false |
| BIOE 210 | option 1 | OR: one of a group | CS 124 | false |
| CS 101 | option 1 | OR: one of a group | MATH 220 | false |
| CS 101 | option 1 | OR: one of a group | MATH 221 | false |
| CS 101 | option 1 | OR: one of a group | MATH 231 | false |
| CS 101 | option 1 | OR: one of a group | MATH 241 | false |
| CS 124 | option 1 | AND: required course | MATH 112 | false |
| CS 128 | option 1 | OR: one of a group | CS 124 | false |
| CS 128 | option 1 | OR: one of a group | CS 125 | true |
| CS 173 | option 1 | OR: one of a group | CS 124 | false |
| CS 173 | option 1 | OR: one of a group | CS 125 | true |
| CS 173 | option 1 | OR: one of a group | ECE 220 | false |
| CS 173 | option 1 | OR: one of a group | MATH 220 | false |
| CS 173 | option 1 | OR: one of a group | MATH 221 | false |
| CS 225 | option 1 | OR: one of a group | CS 126 | true |
| CS 225 | option 1 | OR: one of a group | CS 128 | false |
| CS 225 | option 1 | OR: one of a group | CS 173 | false |
| CS 225 | option 1 | OR: one of a group | CS 413 | true |
| CS 225 | option 1 | OR: one of a group | ECE 220 | false |
| CS 225 | option 1 | OR: one of a group | MATH 213 | false |
| CS 225 | option 1 | OR: one of a group | MATH 314 | false |
| CS 225 | option 1 | OR: one of a group | MATH 347 | true |
| CS 225 | option 1 | OR: one of a group | MATH 412 | false |
| CS 225 | option 1 | OR: one of a group | MATH 413 | false |
| CS 233 | option 1 | AND: required course | CS 225 | false |
| CS 233 | option 1 | OR: one of a group | CS 125 | true |
| CS 233 | option 1 | OR: one of a group | CS 128 | false |
| CS 233 | option 1 | OR: one of a group | CS 173 | false |
| CS 233 | option 1 | OR: one of a group | MATH 213 | false |
| CS 340 | option 1 | AND: required course | CS 128 | false |
| CS 340 | option 1 | AND: required course | CS 225 | false |
| CS 374 | option 1 | AND: required course | CS 225 | false |
| CS 374 | option 1 | OR: one of a group | CS 173 | false |
| CS 374 | option 1 | OR: one of a group | MATH 213 | false |
| CS 421 | option 1 | OR: one of a group | ASRM 406 | false |
| CS 421 | option 1 | OR: one of a group | BIOE 210 | false |
| CS 421 | option 1 | OR: one of a group | CS 233 | false |
| CS 421 | option 1 | OR: one of a group | CS 240 | true |
| CS 421 | option 1 | OR: one of a group | CS 340 | false |
| CS 421 | option 1 | OR: one of a group | CS 374 | false |
| CS 421 | option 1 | OR: one of a group | ECE 374 | true |
| CS 421 | option 1 | OR: one of a group | ECE 391 | false |
| CS 421 | option 1 | OR: one of a group | MATH 225 | false |
| CS 421 | option 1 | OR: one of a group | MATH 257 | false |
| CS 421 | option 1 | OR: one of a group | MATH 415 | false |
| CS 421 | option 1 | OR: one of a group | MATH 416 | false |
| ECE 220 | option 1 | AND: required course | ECE 120 | false |
| ECE 391 | option 1 | OR: one of a group | CS 233 | false |
| ECE 391 | option 1 | OR: one of a group | ECE 220 | false |
| FIN 221 | option 1 | OR: one of a group | ECON 102 | true |
| FIN 221 | option 1 | OR: one of a group | ECON 103 | true |
| MATH 115 | option 1 | AND: required course | MATH 112 | false |
| MATH 213 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 213 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 220 | option 1 | AND: required course | MATH 115 | false |
| MATH 225 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 225 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 231 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 231 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 241 | option 1 | AND: required course | MATH 231 | false |
| MATH 257 | option 1 | AND: required course | CS 101 | false |
| MATH 257 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 257 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 314 | option 1 | AND: required course | MATH 241 | false |
| MATH 412 | option 1 | OR: one of a group | CS 374 | false |
| MATH 412 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 412 | option 1 | OR: one of a group | MATH 347 | true |
| MATH 413 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 413 | option 1 | OR: one of a group | MATH 347 | true |
| MATH 415 | option 1 | AND: required course | MATH 241 | false |
| MATH 416 | option 1 | AND: required course | MATH 241 | false |
| MATH 416 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 416 | option 1 | OR: one of a group | MATH 347 | true |


# CQ02 condition A — full supplied model answer

None of the provided information allows for the determination of prerequisite chains for CS 421 or any course, as no course data, prerequisites, or structure is available. Without a course catalog or prerequisite graph, it is impossible to trace chains back to courses with no recorded prerequisites, nor to preserve AND/OR branches.

**Conclusion**:  
No possible prerequisite chains can be determined due to lack of course data.  

**Missing Information**:  
- Course catalog or prerequisite database  
- Prerequisite relationships for CS 421 or any course  
- Structure of course hierarchy (e.g., whether prerequisites are AND/OR)  

→ Response is not feasible with current input.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ02 condition B — full supplied model answer

| fromCode | option | edgeType | toCode | toIsBaseCourse |
|---------|--------|----------|--------|----------------|
| ASRM 406 | option 1 | OR: one of a group | ASRM 210 | false |
| ASRM 406 | option 1 | OR: one of a group | FIN 221 | false |
| ASRM 406 | option 1 | OR: one of a group | MATH 210 | true |
| BIOE 210 | option 1 | OR: one of a group | CS 101 | false |
| BIOE 210 | option 1 | OR: one of a group | CS 124 | false |
| CS 101 | option 1 | OR: one of a group | MATH 220 | false |
| CS 101 | option 1 | OR: one of a group | MATH 221 | false |
| CS 101 | option 1 | OR: one of a group | MATH 231 | false |
| CS 101 | option 1 | OR: one of a group | MATH 241 | false |
| CS 124 | option 1 | AND: required course | MATH 112 | false |
| CS 128 | option 1 | OR: one of a group | CS 124 | false |
| CS 128 | option 1 | OR: one of a group | CS 125 | true |
| CS 173 | option 1 | OR: one of a group | CS 124 | false |
| CS 173 | option 1 | OR: one of a group | CS 125 | true |
| CS 173 | option 1 | OR: one of a group | ECE 220 | false |
| CS 173 | option 1 | OR: one of a group | MATH 220 | false |
| CS 173 | option 1 | OR: one of a group | MATH 221 | false |
| CS 225 | option 1 | OR: one of a group | CS 126 | true |
| CS 225 | option 1 | OR: one of a group | CS 128 | false |
| CS 225 | option 1 | OR: one of a group | CS 173 | false |
| CS 225 | option 1 | OR: one of a group | CS 413 | true |
| CS 225 | option 1 | OR: one of a group | ECE 220 | false |
| CS 225 | option 1 | OR: one of a group | MATH 213 | false |
| CS 225 | option 1 | OR: one of a group | MATH 314 | false |
| CS 225 | option 1 | OR: one of a group | MATH 347 | true |
| CS 225 | option 1 | OR: one of a group | MATH 412 | false |
| CS 225 | option 1 | OR: one of a group | MATH 413 | false |
| CS 233 | option 1 | AND: required course | CS 225 | false |
| CS 233 | option 1 | OR: one of a group | CS 125 | true |
| CS 233 | option 1 | OR: one of a group | CS 128 | false |
| CS 233 | option 1 | OR: one of a group | CS 173 | false |
| CS 233 | option 1 | OR: one of a group | MATH 213 | false |
| CS 340 | option 1 | AND: required course | CS 128 | false |
| CS 340 | option 1 | AND: required course | CS 225 | false |
| CS 374 | option 1 | AND: required course | CS 225 | false |
| CS 374 | option 1 | OR: one of a group | CS 173 | false |
| CS 374 | option 1 | OR: one of a group | MATH 213 | false |
| CS 421 | option 1 | OR: one of a group | ASRM 406 | false |
| CS 421 | option 1 | OR: one of a group | BIOE 210 | false |
| CS 421 | option 1 | OR: one of a group | CS 233 | false |
| CS 421 | option 1 | OR: one of a group | CS 240 | true |
| CS 421 | option 1 | OR: one of a group | CS 340 | false |
| CS 421 | option 1 | OR: one of a group | CS 374 | false |
| CS 421 | option 1 | OR: one of a group | ECE 374 | true |
| CS 421 | option 1 | OR: one of a group | ECE 391 | false |
| CS 421 | option 1 | OR: one of a group | MATH 225 | false |
| CS 421 | option 1 | OR: one of a group | MATH 257 | false |
| CS 421 | option 1 | OR: one of a group | MATH 415 | false |
| CS 421 | option 1 | OR: one of a group | MATH 416 | false |
| ECE 220 | option 1 | AND: required course | ECE 120 | false |
| ECE 391 | option 1 | OR: one of a group | CS 233 | false |
| ECE 391 | option 1 | OR: one of a group | ECE 220 | false |
| FIN 221 | option 1 | OR: one of a group | ECON 102 | true |
| FIN 221 | option 1 | OR: one of a group | ECON 103 | true |
| MATH 115 | option 1 | AND: required course | MATH 112 | false |
| MATH 213 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 213 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 220 | option 1 | AND: required course | MATH 115 | false |
| MATH 225 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 225 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 231 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 231 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 241 | option 1 | AND: required course | MATH 231 | false |
| MATH 257 | option 1 | AND: required course | CS 101 | false |
| MATH 257 | option 1 | OR: one of a group | MATH 220 | false |
| MATH 257 | option 1 | OR: one of a group | MATH 221 | false |
| MATH 314 | option 1 | AND: required course | MATH 241 | false |
| MATH 412 | option 1 | OR: one of a group | CS 374 | false |
| MATH 412 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 412 | option 1 | OR: one of a group | MATH 347 | true |
| MATH 413 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 413 | option 1 | OR: one of a group | MATH 347 | true |
| MATH 415 | option 1 | AND: required course | MATH 241 | false |
| MATH 416 | option 1 | AND: required course | MATH 241 | false |
| MATH 416 | option 1 | OR: one of a group | MATH 314 | false |
| MATH 416 | option 1 | OR: one of a group | MATH 347 | true |

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ03 — verified expected rows

Which prerequisite alternatives for a target course are fully met by a given student, and wh ich precise course, standing, or consent conditions remain unmet? Instance: synthetic student S003; target course CS 421; Fall 2026.

| option | optionStatus | conditionType | conditionText | conditionStatus |
| --- | --- | --- | --- | --- |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | not met | CourseChoiceCondition | One of CS 233, CS 240, CS 340 or ECE 391 | met |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | not met | CourseChoiceCondition | CS 374 or ECE 374 | UNMET / needs review |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | not met | CourseChoiceCondition | one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 | met |


# CQ03 condition A — full supplied model answer

No data is available regarding student S003, course CS 421, or any prerequisite conditions for Fall 2026. Without access to a student transcript, course catalog, or enrollment system, it is impossible to determine which prerequisites are met or unmet, or what specific standing or consent conditions remain.

Therefore, the query cannot be answered with certainty based on available information.

**Conclusion:**  
- Prerequisite alternatives fully met: Unknown (no data)  
- Unmet conditions: Unknown (no data)  

*Note: This response reflects the absence of retrieval tools or course graph data. No assumptions or inferences are made beyond the stated constraints.*

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ03 condition B — full supplied model answer

| option | conditionText | conditionStatus | optionStatus | basis | unmetCondition | citation |
|--------|--------------|----------------|-------------|-------|----------------|----------|
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | One of CS 233, CS 240, CS 340 or ECE 391 | met | not met | completed | — | [R1] |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | CS 374 or ECE 374 | UNMET / needs review | not met | unverified | CS 374 or ECE 374 | [R2] |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 | met | not met | completed | — | [R3] |

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ04 — verified expected rows

If a student completes one additional course, which downstream courses may become available and what other conditions would still have to hold? Instance: synthetic student S002 hypothetically completes CS 225; Fall 2026.

| courseCode | option | status | stillRequired |
| --- | --- | --- | --- |
| CS 341 | option 1 | still blocked | CS 233 |
| CS 418 | option 1 | still blocked | One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| MATH 241 |
| CS 440 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 |
| CS 441 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, BIOE 310, MATH 362, MATH 461, MATH 463 or STAT 400 |
| CS 444 | option 1 | still blocked | MATH 241 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 |
| CS 445 | option 1 | still blocked | CS 225, MATH 225 |
| CS 446 | option 1 | still blocked | One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 |
| CS 447 | option 1 | still blocked | CS 374 or ECE 374 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 |
| CS 463 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 |
| CS 470 | option 1 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 |
| CS 477 | option 1 | still blocked | one of CS 374, ECE 374 or MATH 414 |
| ADV 492 | option 1 | would become satisfiable |  |
| CS 210 | option 1 | would become satisfiable |  |
| CS 211 | option 1 | would become satisfiable |  |
| CS 233 | option 1 | would become satisfiable |  |
| CS 340 | option 1 | would become satisfiable |  |
| CS 374 | option 1 | would become satisfiable |  |
| CS 409 | option 1 | would become satisfiable |  |
| CS 410 | option 1 | would become satisfiable |  |
| CS 411 | option 1 | would become satisfiable |  |
| CS 412 | option 1 | would become satisfiable |  |
| CS 415 | option 1 | would become satisfiable |  |
| CS 452 | option 1 | would become satisfiable |  |
| CS 464 | option 1 | would become satisfiable |  |
| CS 465 | option 1 | would become satisfiable |  |
| CS 466 | option 1 | would become satisfiable |  |
| ECE 407 | option 1 | would become satisfiable |  |
| ECE 549 | option 1 | would become satisfiable |  |


# CQ04 condition A — full supplied model answer

No downstream courses become available, and no additional conditions are triggered.

Reasoning:  
The scenario specifies only that a student completes CS 225 in Fall 2026. However, no course prerequisites, downstream dependencies, or availability rules are provided in the query or context. Without explicit information about course prerequisites, co-requisites, or academic pathways (e.g., "CS 225 is required for CS 330"), it is impossible to determine which downstream courses may become available.

Additionally, even if CS 225 were a prerequisite for another course, the absence of a stated dependency or course structure means we cannot infer downstream availability.

Therefore, based on the given information:

- No downstream courses are known to become available.
- No conditions beyond the completion of CS 225 are specified or verifiable.
- The student’s academic pathway, degree requirements, or university policy are not provided.

Conclusion:  
Without explicit prerequisite or dependency rules, downstream course availability cannot be determined. The condition "a student completes one additional course" does not trigger any known downstream outcomes in this context.

> ⚠️ Uncertainty: Missing course dependency data.  
> ⚠️ Missing academic policy or curriculum structure.  
> ⚠️ No evidence of CS 225 being a prerequisite for any downstream course.  

Thus, no downstream courses are identified, and no additional conditions are known to hold.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ04 condition B — full supplied model answer

| courseCode | status | stillRequired | citation |
|-----------|--------|--------------|---------|
| CS 341 | still blocked | CS 233 | [R1] |
| CS 418 | still blocked | One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| MATH 241 | [R2] |
| CS 440 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 | [R3] |
| CS 441 | still blocked | one of CS 361, STAT 361, ECE 313, BIOE 310, MATH 362, MATH 461, MATH 463 or STAT 400 | [R4] |
| CS 444 | still blocked | MATH 241 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 | [R5] |
| CS 445 | still blocked | CS 225, MATH 225 | [R6] |
| CS 446 | still blocked | One of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 | [R7] |
| CS 447 | still blocked | CS 374 or ECE 374 \| one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463, STAT 400 or BIOE 310 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406 or BIOE 210 | [R8] |
| CS 463 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 | [R9] |
| CS 470 | still blocked | one of CS 361, STAT 361, ECE 313, MATH 362, MATH 461, MATH 463 or STAT 400 \| one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 | [R10] |
| CS 477 | still blocked | one of CS 374, ECE 374 or MATH 414 | [R11] |
| ADV 492 | would become satisfiable | | [R12] |
| CS 210 | would become satisfiable | | [R13] |
| CS 211 | would become satisfiable | | [R14] |
| CS 233 | would become satisfiable | | [R15] |
| CS 340 | would become satisfiable | | [R16] |
| CS 374 | would become satisfiable | | [R17] |
| CS 409 | would become satisfiable | | [R18] |
| CS 410 | would become satisfiable | | [R19] |
| CS 411 | would become satisfiable | | [R20] |
| CS 412 | would become satisfiable | | [R21] |
| CS 415 | would become satisfiable | | [R22] |
| CS 452 | would become satisfiable | | [R23] |
| CS 464 | would become satisfiable | | [R24] |
| CS 465 | would become satisfiable | | [R25] |
| CS 466 | would become satisfiable | | [R26] |
| ECE 407 | would become satisfiable | | [R27] |
| ECE 549 | would become satisfiable | | [R28] |

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ06 — verified expected rows

How many courses and credit hours are still needed in each core or elective group for a given student and degree-program catalog year? Instance: synthetic student S003; program UIUC BS CS, catalog year 2026.

| requirement | minCourses | allocatedCourses | remainingCourses | minCredits | allocatedCredits |
| --- | --- | --- | --- | --- | --- |
| Technical electives (min 6 courses, 18 hours) | 6 | 0 | 6 | 18.0 | 0 |
| CS technical core (11 courses, 35 hours) | 11 | 6 | 5 | 35.0 | 18.0 |
| Focus area: Algorithms and Models of Computation | 3 | 0 | 3 |  | 0 |
| Focus area: Distributed Systems, Networking, and Security | 3 | 0 | 3 |  | 0 |
| Focus area: Human and Social Impact | 3 | 0 | 3 |  | 0 |
| Focus area: Intelligence and Big Data | 3 | 0 | 3 |  | 0 |
| Focus area: Machines | 3 | 0 | 3 |  | 0 |
| Focus area: Media | 3 | 0 | 3 |  | 0 |
| Focus area: Scientific, Parallel, and High Performance Computing | 3 | 0 | 3 |  | 0 |
| Focus area: Software Foundations | 3 | 0 | 3 |  | 0 |
| Advanced electives (min 2 courses, 6 hours) | 2 | 0 | 2 | 6.0 | 0 |
| Ethical and professional issues: CS 210 or CS 211 | 1 | 0 | 1 | 2.0 | 0 |
| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | 4 | 3 | 1 | 15.0 | 11.0 |
| Science elective (one Natural Science & Technology course) | 1 | 0 | 1 | 3.0 | 0 |
| Team project course (at least 1 of the technical electives) | 1 | 0 | 1 |  | 0 |
| Calculus I: MATH 221 (MATH 220 may be substituted) | 1 | 1 | 0 | 4.0 | 4.0 |
| Linear algebra: MATH 257, MATH 415 or MATH 416 | 1 | 1 | 0 | 3.0 | 3.0 |
| Orientation: ENG 100 | 1 | 1 | 0 | 1.0 | 1.0 |


# CQ06 condition A — full supplied model answer

I cannot provide the number of courses and credit hours still needed for student S003 in the UIUC BS CS program for catalog year 2026, as no student transcript, course enrollment data, or program-specific curriculum details have been provided. 

To determine remaining course and credit requirements, I would need:

- The student’s current course enrollment or transcript (including completed and pending courses)
- The official degree program curriculum for UIUC BS CS in catalog year 2026
- The specific core and elective group breakdowns (e.g., math, CS core, electives)
- Prerequisites and graduation requirements for that catalog year

Without this information, any calculation is speculative.

**Conclusion**: Insufficient data to determine remaining courses and credit hours.  
→ **No answer possible with current information.**

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ06 condition B — full supplied model answer

| Requirement | Min Courses | Allocated Courses | Remaining Courses | Min Credits | Allocated Credits | Remaining Credits |
|-----------|-------------|-------------------|-------------------|-------------|-------------------|-------------------|
| CS technical core (11 courses, 35 hours) | 11 | 6 | 5 | 35.0 | 18.0 | 17.0 |
| Ethical and professional issues: CS 210 or CS 211 | 1 | 0 | 1 | 2.0 | 0.0 | 2.0 |
| Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 | 4 | 3 | 1 | 15.0 | 11.0 | 4.0 |
| Advanced electives (min 2 courses, 6 hours) | 2 | 0 | 2 | 6.0 | 0.0 | 6.0 |
| Focus area: Algorithms and Models of Computation | 3 | 0 | 3 | null | 0.0 | null |
| Focus area: Distributed Systems, Networking, and Security | 3 | 0 | 3 | null | 0.0 | null |
| Focus area: Human and Social Impact | 3 | 0 | 3 | null | 0.0 | null |
| Focus area: Intelligence and Big Data | 3 | 0 | 3 | null | 0.0 | null |
| Focus area: Machines | 3 | 0 | 3 | null | 0.0 | null |
| Focus area: Media | 3 | 0 | 3 | null | 0.0 | null |
| Focus area: Scientific, Parallel, and High Performance Computing | 3 | 0 | 3 | null | 0.0 | null |
| Focus area: Software Foundations | 3 | 0 | 3 | null | 0.0 | null |
| Science elective (one Natural Science & Technology course) | 1 | 0 | 1 | 3.0 | 0.0 | 3.0 |
| Team project course (at least 1 of the technical electives) | 1 | 0 | 1 | null | 0.0 | null |
| Technical electives (min 6 courses, 18 hours) | 6 | 0 | 6 | 18.0 | 0.0 | 18.0 |

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ08 — verified expected rows

Which courses are at least two prerequisite-course links upstream of a selected target course, and through which alternative branches are they reachable? Instance: CS 440.

| upstreamCode | viaCode | firstHop |
| --- | --- | --- |
| BIOE 210 | BIOE 310 | via one-of group (potential) |
| CS 101 | BIOE 310 | via one-of group (potential) |
| CS 101 | ECE 313 | via one-of group (potential) |
| CS 124 | BIOE 310 | via one-of group (potential) |
| CS 124 | CS 225 | via required course |
| CS 125 | CS 225 | via required course |
| CS 126 | CS 225 | via required course |
| CS 128 | CS 225 | via required course |
| CS 173 | CS 225 | via required course |
| CS 374 | CS 225 | via required course |
| CS 413 | CS 225 | via required course |
| ECE 120 | CS 225 | via required course |
| ECE 220 | CS 225 | via required course |
| MATH 112 | BIOE 310 | via one-of group (potential) |
| MATH 112 | CS 225 | via required course |
| MATH 112 | CS 361 | via one-of group (potential) |
| MATH 112 | ECE 313 | via one-of group (potential) |
| MATH 112 | MATH 461 | via one-of group (potential) |
| MATH 112 | STAT 400 | via one-of group (potential) |
| MATH 115 | BIOE 310 | via one-of group (potential) |
| MATH 115 | CS 225 | via required course |
| MATH 115 | CS 361 | via one-of group (potential) |
| MATH 115 | ECE 313 | via one-of group (potential) |
| MATH 115 | MATH 461 | via one-of group (potential) |
| MATH 115 | STAT 400 | via one-of group (potential) |
| MATH 213 | CS 225 | via required course |
| MATH 220 | BIOE 310 | via one-of group (potential) |
| MATH 220 | CS 225 | via required course |
| MATH 220 | CS 361 | via one-of group (potential) |
| MATH 220 | ECE 313 | via one-of group (potential) |
| MATH 220 | MATH 461 | via one-of group (potential) |
| MATH 220 | STAT 400 | via one-of group (potential) |
| MATH 221 | BIOE 310 | via one-of group (potential) |
| MATH 221 | CS 225 | via required course |
| MATH 221 | CS 361 | via one-of group (potential) |
| MATH 221 | ECE 313 | via one-of group (potential) |
| MATH 221 | MATH 461 | via one-of group (potential) |
| MATH 221 | STAT 400 | via one-of group (potential) |
| MATH 231 | BIOE 310 | via one-of group (potential) |
| MATH 231 | CS 225 | via required course |
| MATH 231 | ECE 313 | via one-of group (potential) |
| MATH 231 | MATH 461 | via one-of group (potential) |
| MATH 231 | STAT 400 | via one-of group (potential) |
| MATH 241 | BIOE 310 | via one-of group (potential) |
| MATH 241 | CS 225 | via required course |
| MATH 241 | ECE 313 | via one-of group (potential) |
| MATH 241 | MATH 461 | via one-of group (potential) |
| MATH 257 | BIOE 310 | via one-of group (potential) |
| MATH 257 | ECE 313 | via one-of group (potential) |
| MATH 314 | CS 225 | via required course |
| MATH 314 | ECE 313 | via one-of group (potential) |
| MATH 347 | CS 225 | via required course |
| MATH 347 | ECE 313 | via one-of group (potential) |
| MATH 412 | CS 225 | via required course |
| MATH 413 | CS 225 | via required course |
| MATH 416 | ECE 313 | via one-of group (potential) |


# CQ08 condition A — full supplied model answer

None of the courses are known to be at least two prerequisite-course links upstream of CS 440, and no alternative branches are documented in the available course data.

Reasoning:  
- The query asks for courses that are at least two prerequisite links upstream of CS 440.  
- Without a course prerequisite graph or database, we cannot trace prerequisite chains or determine upstream dependencies.  
- No course graph or transcript data is provided to evaluate prerequisite relationships or alternative pathways.  
- Therefore, no courses can be identified as satisfying the "at least two prerequisite links upstream" condition.  
- Similarly, no alternative branches are reachable due to lack of structural or dependency information.

Conclusion:  
No such courses exist in the available data.  
Alternative branches cannot be determined due to missing prerequisite structure.

Note: This response is based solely on the absence of provided course data and cannot infer relationships without a course dependency graph.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ08 condition B — full supplied model answer

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

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ10 — verified expected rows

For a selected course, which cross-listed course codes and downstream prerequisites reference its codes, and are any substitutions still subject to explicit policy? Instance: CS 374.

| alias | downstreamCode | mentions | acceptsBothCodes |
| --- | --- | --- | --- |
| ECE 374 | CS 421 | CS 374, ECE 374 | true |
| ECE 374 | CS 447 | CS 374, ECE 374 | true |
| ECE 374 | CS 473 | CS 374, ECE 374 | true |
| ECE 374 | CS 475 | CS 374, ECE 374 | true |
| ECE 374 | CS 477 | CS 374, ECE 374 | true |
| ECE 374 | CS 521 | CS 374, ECE 374 | true |
| ECE 374 | CS 581 | CS 374, ECE 374 | true |
| ECE 374 | MATH 412 | CS 374 | false |
| ECE 374 | MATH 417 | CS 374 | false |


# CQ10 condition A — full supplied model answer

No information is available regarding cross-listed course codes, downstream prerequisites, or substitution policies for CS 374 or any course in the absence of a course catalog, university database, or official academic policy document.

Therefore, I cannot provide:

- Cross-listed course codes that reference CS 374  
- Downstream prerequisites that depend on CS 374  
- Whether substitutions are subject to explicit policy  

This query requires access to a university’s official course catalog or academic policy repository, which is not available here.

**Conclusion**: Uncertain. No data provided. Requested information cannot be retrieved or verified without official course records.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ10 condition B — full supplied model answer

| cross-listed_code | downstream_prerequisite | substitution_policy_status |
|------------------|------------------------|----------------------------|
| ECE 374          | CS 421                | acceptsBothCodes=true     |
| ECE 374          | CS 447                | acceptsBothCodes=true     |
| ECE 374          | CS 473                | acceptsBothCodes=true     |
| ECE 374          | CS 475                | acceptsBothCodes=true     |
| ECE 374          | CS 477                | acceptsBothCodes=true     |
| ECE 374          | CS 521                | acceptsBothCodes=true     |
| ECE 374          | MATH 412              | acceptsBothCodes=false    |
| ECE 374          | MATH 417              | acceptsBothCodes=false    |

*Result Guide: "acceptsBothCodes=true" means both codes are explicitly mentioned in the downstream prerequisite. "false" means explicit acceptance of both was NOT established; it does NOT mean substitution is forbidden. Cross-listing alone does not establish general substitution policy.*

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ11 — verified expected rows

For each department, how many available courses could fulfill a particular  elective group in a selected term? Instance: advanced elective group; Fall 2026.

| department | advancedElectivesOfferedFall2026 |
| --- | --- |
| CS | 50 |
| ECE | 46 |
| MATH | 30 |
| STAT | 19 |
| PHYS | 17 |
| CSE | 12 |
| ASRM | 5 |
| PHIL | 3 |
| BIOE | 2 |
| MSE | 2 |
| ADV | 1 |
| AE | 1 |
| IE | 1 |
| ME | 1 |
| NE | 1 |
| TAM | 1 |


# CQ11 condition A — full supplied model answer

I cannot provide a specific answer to your question because:

- There is no available course data or departmental course catalog provided.
- No term (e.g., Fall 2026) or elective group (e.g., advanced elective group) is defined in the context of a university curriculum.
- No departmental course offerings or prerequisites are specified.

Therefore, I cannot determine how many available courses in each department could fulfill a particular elective group in a selected term.

To answer this question accurately, I would need:
- A list of departments and their offered courses.
- A defined set of elective groups (e.g., advanced, humanities, science).
- A schedule of course availability by term (e.g., Fall 2026).
- Prerequisite or enrollment constraints.

Without such data, the query cannot be resolved.

**Conclusion**: Insufficient information to determine available courses per department for a specific elective group in a term.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ11 condition B — full supplied model answer

| department | available_courses_for_advanced_elective_group_fall_2026 |
|---|---|
| CS | 50 |
| ECE | 46 |
| MATH | 30 |
| STAT | 19 |
| PHYS | 17 |
| CSE | 12 |
| ASRM | 5 |
| PHIL | 3 |
| BIOE | 2 |
| MSE | 2 |
| ADV | 1 |
| AE | 1 |
| IE | 1 |
| ME | 1 |
| NE | 1 |
| TAM | 1 |

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ13 — verified expected rows

How does the set of satisfiable prerequisite options and course recommendations change when one planned completion is hypothetically added to a student's transcript? Instance: synthetic student S002 hypothetically adds CS 225; Fall 2026.

| courseCode | title | eligibleIn |
| --- | --- | --- |
| ADV 492 | Tech and Advertising Campaigns | plus CS 225 |
| CS 210 | Ethical & Professional Issues | plus CS 225 |
| CS 211 | Ethical and Professional Conduct | plus CS 225 |
| CS 233 | Computer Architecture | plus CS 225 |
| CS 340 | Introduction to Computer Systems | plus CS 225 |
| CS 374 | Introduction to Algorithms & Models of Computation | plus CS 225 |
| CS 409 | The Art of Web Programming | plus CS 225 |
| CS 410 | Text Information Systems | plus CS 225 |
| CS 411 | Database Systems | plus CS 225 |
| CS 412 | Introduction to Data Mining | plus CS 225 |
| CS 415 | Game Development | plus CS 225 |
| CS 452 | Topics in Robotics | plus CS 225 |
| CS 464 | Topics in Societal and Ethical Impacts of Computer Technology | plus CS 225 |
| CS 465 | User Interface Design | plus CS 225 |
| CS 466 | Introduction to Bioinformatics | plus CS 225 |
| ECE 407 | Cryptography | plus CS 225 |
| ECE 549 | Computer Vision | plus CS 225 |


# CQ13 condition A — full supplied model answer

No retrievable data or course graph is available to assess how the set of satisfiable prerequisite options or course recommendations changes when a hypothetical course completion (e.g., CS 225, Fall 2026) is added to a student's transcript.

Therefore, based on the provided information:

- There is no access to a student transcript or course prerequisite graph.
- No prior course history or academic plan for student S002 is available.
- No rules or logic for evaluating prerequisite satisfaction or course recommendations are provided.

**Conclusion:**  
The impact of adding CS 225 (Fall 2026) to student S002’s transcript cannot be determined without access to the course prerequisite structure, current transcript, or recommendation logic.

**Uncertainty:**  
- The prerequisite relationships for CS 225 are unknown.  
- Whether CS 225 is a prerequisite for other courses or a result of prior course work is not specified.  
- No data exists to evaluate how this addition affects satisfiable options or recommendations.

Thus, **no change** can be assessed — **no information is available to compute or infer any change**.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ13 condition B — full supplied model answer

| courseCode | title | eligibleIn | citation |
|-----------|------|-----------|---------|
| ADV 492 | Tech and Advertising Campaigns | plus CS 225 | [R1] |
| CS 210 | Ethical & Professional Issues | plus CS 225 | [R2] |
| CS 211 | Ethical and Professional Conduct | plus CS 225 | [R3] |
| CS 233 | Computer Architecture | plus CS 225 | [R4] |
| CS 340 | Introduction to Computer Systems | plus CS 225 | [R5] |
| CS 374 | Introduction to Algorithms & Models of Computation | plus CS 225 | [R6] |
| CS 409 | The Art of Web Programming | plus CS 225 | [R7] |
| CS 410 | Text Information Systems | plus CS 225 | [R8] |
| CS 411 | Database Systems | plus CS 225 | [R9] |
| CS 412 | Introduction to Data Mining | plus CS 225 | [R10] |
| CS 415 | Game Development | plus CS 225 | [R11] |
| CS 452 | Topics in Robotics | plus CS 225 | [R12] |
| CS 464 | Topics in Societal and Ethical Impacts of Computer Technology | plus CS 225 | [R13] |
| CS 465 | User Interface Design | plus CS 225 | [R14] |
| CS 466 | Introduction to Bioinformatics | plus CS 225 | [R15] |
| ECE 407 | Cryptography | plus CS 225 | [R16] |
| ECE 549 | Computer Vision | plus CS 225 | [R17] |

**Change Summary under Hypothetical Completion of CS 225 (Fall 2026):**  
All 17 courses listed above become *eligible* due to the prerequisite condition "plus CS 225". This hypothetical completion satisfies the prerequisite for each of these courses, enabling their inclusion in the student’s course recommendations.  
- **Newly satisfied prerequisites**: 17 courses (as per `newly_satisfied` in reasoning).  
- **Downstream candidates**: 71 (as per `downstream_course_count` in reasoning).  
- **Note**: The stored KG remains unchanged; this evaluation is a memory-based what-if.  
- **Unverified**: No course has a prerequisite that does not depend on CS 225; all listed prerequisites are explicitly tied to CS 225.  
- **Missing evidence**: 1130 RDF edges omitted; no impact on this query result.  

*All entries are derived from the `eligibleIn` field and verified via explicit prerequisite conditions in the context.*

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ15 — verified expected rows

What catalog wording, degree requirement and prerequisite-option evidence s upports each recommendation, and which conditions remain unverified? Instance: synthetic student S002's planned courses; Fall 2026.

| courseCode | prerequisiteText | parseStatus | satisfiedOptions | requirement | requirementNote | source | unverified |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CS 225 | CS 126 or CS 128 or ECE 220; One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413. | parsed | 1 | CS technical core (11 courses, 35 hours) | Technical GPA of 2.0 is required for CS and Math courses. | https://discovery.cs.illinois.edu/dataset/course-catalog/ | none |
| MATH 241 | MATH 231. | parsed | 1 | Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212 |  | https://discovery.cs.illinois.edu/dataset/course-catalog/ | none |
| MATH 257 | MATH 220 or MATH 221; CS 101 or equivalent programming experience. | needs_review | 0 | Linear algebra: MATH 257, MATH 415 or MATH 416 |  | https://discovery.cs.illinois.edu/dataset/course-catalog/ | yes: wording such as 'or equivalent' needs manual check |


# CQ15 condition A — full supplied model answer

No catalog wording, degree requirement, or prerequisite-option evidence is available for student S002's planned courses in Fall 2026. No course data, transcripts, or institutional records have been provided to support any recommendations, verify prerequisites, or confirm degree requirements.

Therefore, all claims—regarding catalog wording, degree requirements, or prerequisite options—remain unverified. No instance of a student (e.g., S002) or course schedule has been presented or accessible for analysis.

**Unverified conditions:**
- Catalog wording for any course or requirement
- Degree requirement alignment (e.g., major, minor, graduation criteria)
- Prerequisite options for specific courses
- Course sequencing or academic plan validity

**Conclusion:**  
No evidence is available to support any recommendation for student S002 in Fall 2026. All conditions remain unverified due to lack of input data.

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# CQ15 condition B — full supplied model answer

| Course Code | Catalog Wording | Degree Requirement | Prerequisite Option Evidence | Unverified Conditions | R-number |
|------------|----------------|--------------------|-------------------------------|------------------------|---------|
| CS 225 | Prerequisites: CS 126 or CS 128 or ECE 220; One of CS 173, CS 413, MATH 213, MATH 314, MATH 347, MATH 412, or MATH 413. | CS technical core (11 courses, 35 hours); Technical GPA of 2.0 required for CS and Math courses. | Satisfied: CS 128 (completed), CS 173 (completed). | none | [R1] |
| MATH 241 | Prerequisite: MATH 231. | Required calculus and physics: MATH 231, MATH 241, PHYS 211, PHYS 212. | Satisfied: MATH 231 (completed). | none | [R2] |
| MATH 257 | Prerequisite: MATH 220 or MATH 221; CS 101 or equivalent programming experience. | Linear algebra: MATH 257, MATH 415 or MATH 416. | Partially satisfied: MATH 221 (completed); CS 101 programming experience unverified. | CS 101 or equivalent programming experience (unverified) | [R3] |

finish_reason: stop; truncated: False; human correctness/evidence review pending unless scored above.


# Three explainability records


# CQ03 — Which prerequisite alternatives for a target course are fully met by a given student, and wh ich precise course, standing, or consent conditions remain unmet? Instance: synthetic student S003; target course CS 421; Fall 2026.

Generated text (LLM): | option | conditionText | conditionStatus | optionStatus | basis | unmetCondition | citation |
|--------|--------------|----------------|-------------|-------|----------------|----------|
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | One of CS 233, CS 240, CS 340 or ECE 391 | met | not met | completed | — | [R1] |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | CS 374 or ECE 374 | UNMET / needs review | not met | unverified | CS 374 or ECE 374 | [R2] |
| https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1 | one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210 | met | not met | completed | — | [R3] |

Explicit knowledge (stored) — representative retrieved triples (full evidence in JSON):

```
[
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/CS421>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression>",
    "o": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421>",
    "status": "explicit",
    "id": "E94388d011e2a20d7"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasOption>",
    "o": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1>",
    "status": "explicit",
    "id": "E353f1aa2f2d74648"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasCondition>",
    "o": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1>",
    "status": "explicit",
    "id": "E8e3ce88b17c81bae"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#alternativeCourse>",
    "o": "<https://example.org/uiuc-course-advisor/resource/course/CS233>",
    "status": "explicit",
    "id": "E693025f47b57b4e3"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/student/S003>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasCompletion>",
    "o": "<https://example.org/uiuc-course-advisor/resource/completion/S003/CS233>",
    "status": "explicit",
    "id": "E6d20782aa3436399"
  }
]
```

Inferred knowledge (OWL schema closure) — representative retrieved triples (full evidence in JSON):

No retrieved triples of this kind in this answer.

```
{
  "one_complete_returned_path": [
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/course/CS421>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#hasPrerequisiteExpression>",
      "o": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421>",
      "status": "explicit",
      "id": "E94388d011e2a20d7"
    },
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#hasOption>",
      "o": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1>",
      "status": "explicit",
      "id": "E353f1aa2f2d74648"
    },
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#hasCondition>",
      "o": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1>",
      "status": "explicit",
      "id": "E8e3ce88b17c81bae"
    },
    {
      "s": "<https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1/condition/1>",
      "p": "<https://example.org/uiuc-course-advisor/ontology#alternativeCourse>",
      "o": "<https://example.org/uiuc-course-advisor/resource/course/CS233>",
      "status": "explicit",
      "id": "E693025f47b57b4e3"
    }
  ]
}
```

Query/application conclusions (computed, not asserted RDF):

```
{
  "rows": [
    {
      "option": "https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1",
      "optionStatus": "not met",
      "conditionType": "CourseChoiceCondition",
      "conditionText": "One of CS 233, CS 240, CS 340 or ECE 391",
      "conditionStatus": "met"
    },
    {
      "option": "https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1",
      "optionStatus": "not met",
      "conditionType": "CourseChoiceCondition",
      "conditionText": "CS 374 or ECE 374",
      "conditionStatus": "UNMET / needs review"
    },
    {
      "option": "https://example.org/uiuc-course-advisor/resource/prereq/CS421/option/1",
      "optionStatus": "not met",
      "conditionType": "CourseChoiceCondition",
      "conditionText": "one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210",
      "conditionStatus": "met"
    }
  ],
  "limitations": []
}
```

Prediction: none. Hypothetical completions, where used, are assumptions. Full query, paths and graph hash remain in the raw JSON.


# CQ08 — Which courses are at least two prerequisite-course links upstream of a selected target course, and through which alternative branches are they reachable? Instance: CS 440.

Generated text (LLM): | upstreamCode | viaCode  | firstHop                     |
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

Explicit knowledge (stored) — representative retrieved triples (full evidence in JSON):

```
[
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/BIOE210>",
    "p": "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>",
    "o": "<https://example.org/uiuc-course-advisor/ontology#Course>",
    "status": "explicit",
    "id": "Ebac390cd31212005"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/BIOE210>",
    "p": "<http://www.w3.org/2000/01/rdf-schema#label>",
    "o": "\"BIOE 210 Linear Algebra for Biomedical Data Science\"",
    "status": "explicit",
    "id": "Ec92778016a6d84e5"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/BIOE210>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#courseCode>",
    "o": "\"BIOE 210\"",
    "status": "explicit",
    "id": "E8d291110ac67bf92"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/BIOE210>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#courseCreditsMax>",
    "o": "\"3.0\"^^<http://www.w3.org/2001/XMLSchema#decimal>",
    "status": "explicit",
    "id": "E4e48060676adad89"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/BIOE210>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#courseCreditsMin>",
    "o": "\"3.0\"^^<http://www.w3.org/2001/XMLSchema#decimal>",
    "status": "explicit",
    "id": "E4decf53ef3700b48"
  }
]
```

Inferred knowledge (OWL schema closure) — representative retrieved triples (full evidence in JSON):

No retrieved triples of this kind in this answer.

Query/application conclusions (computed, not asserted RDF):

```
{
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
  "limitations": []
}
```

Prediction: none. Hypothetical completions, where used, are assumptions. Full query, paths and graph hash remain in the raw JSON.


# CQ11 — For each department, how many available courses could fulfill a particular  elective group in a selected term? Instance: advanced elective group; Fall 2026.

Generated text (LLM): | department | available_courses_for_advanced_elective_group_fall_2026 |
|---|---|
| CS | 50 |
| ECE | 46 |
| MATH | 30 |
| STAT | 19 |
| PHYS | 17 |
| CSE | 12 |
| ASRM | 5 |
| PHIL | 3 |
| BIOE | 2 |
| MSE | 2 |
| ADV | 1 |
| AE | 1 |
| IE | 1 |
| ME | 1 |
| NE | 1 |
| TAM | 1 |

Explicit knowledge (stored) — representative retrieved triples (full evidence in JSON):

```
[
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/program/UIUC-BS-CS-2026>",
    "p": "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>",
    "o": "<https://example.org/uiuc-course-advisor/ontology#DegreeProgram>",
    "status": "explicit",
    "id": "E405857d92f36d076"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/program/UIUC-BS-CS-2026>",
    "p": "<http://www.w3.org/2000/01/rdf-schema#comment>",
    "o": "\"Collected from the official catalog page (retrieved 2026-11-14). The page does not print its catalog-year label; treated as the current 2026-27 catalog. General education and free electives are intentionally not modelled as requirement groups.\"",
    "status": "explicit",
    "id": "Eb448c5a460f82974"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/program/UIUC-BS-CS-2026>",
    "p": "<http://www.w3.org/2000/01/rdf-schema#label>",
    "o": "\"Computer Science, BS (UIUC, Grainger College of Engineering)\"",
    "status": "explicit",
    "id": "E6f6bfcf84fd49499"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/program/UIUC-BS-CS-2026>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasRequirement>",
    "o": "<https://example.org/uiuc-course-advisor/resource/requirement/UIUC-BS-CS-2026/Core-CSTechnical>",
    "status": "explicit",
    "id": "E7f88e8e4ecbba150"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/program/UIUC-BS-CS-2026>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasRequirement>",
    "o": "<https://example.org/uiuc-course-advisor/resource/requirement/UIUC-BS-CS-2026/Core-CalculusI>",
    "status": "explicit",
    "id": "E30ad2b1266063264"
  }
]
```

Inferred knowledge (OWL schema closure) — representative retrieved triples (full evidence in JSON):

```
[
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/department/ADV>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasCourse>",
    "o": "<https://example.org/uiuc-course-advisor/resource/course/ADV492>",
    "status": "inferred",
    "id": "E762b6dffcf900bb8"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/ADV492>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#maySatisfyRequirement>",
    "o": "<https://example.org/uiuc-course-advisor/resource/requirement/UIUC-BS-CS-2026/Elective-Advanced>",
    "status": "inferred",
    "id": "Edcd9028bfce214b3"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/ADV492>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#scheduledInTerm>",
    "o": "<https://example.org/uiuc-course-advisor/resource/term/2026-fa>",
    "status": "inferred",
    "id": "E108879828cae3def"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/department/AE>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#hasCourse>",
    "o": "<https://example.org/uiuc-course-advisor/resource/course/AE482>",
    "status": "inferred",
    "id": "Ee538b8a14c12aeb7"
  },
  {
    "s": "<https://example.org/uiuc-course-advisor/resource/course/AE482>",
    "p": "<https://example.org/uiuc-course-advisor/ontology#maySatisfyRequirement>",
    "o": "<https://example.org/uiuc-course-advisor/resource/requirement/UIUC-BS-CS-2026/Elective-Advanced>",
    "status": "inferred",
    "id": "E212fb4c64cfb3f2f"
  }
]
```

Query/application conclusions (computed, not asserted RDF):

```
{
  "rows": [
    {
      "department": "CS",
      "advancedElectivesOfferedFall2026": "50"
    },
    {
      "department": "ECE",
      "advancedElectivesOfferedFall2026": "46"
    },
    {
      "department": "MATH",
      "advancedElectivesOfferedFall2026": "30"
    },
    {
      "department": "STAT",
      "advancedElectivesOfferedFall2026": "19"
    },
    {
      "department": "PHYS",
      "advancedElectivesOfferedFall2026": "17"
    },
    {
      "department": "CSE",
      "advancedElectivesOfferedFall2026": "12"
    },
    {
      "department": "ASRM",
      "advancedElectivesOfferedFall2026": "5"
    },
    {
      "department": "PHIL",
      "advancedElectivesOfferedFall2026": "3"
    },
    {
      "department": "BIOE",
      "advancedElectivesOfferedFall2026": "2"
    },
    {
      "department": "MSE",
      "advancedElectivesOfferedFall2026": "2"
    },
    {
      "department": "ADV",
      "advancedElectivesOfferedFall2026": "1"
    },
    {
      "department": "AE",
      "advancedElectivesOfferedFall2026": "1"
    },
    {
      "department": "IE",
      "advancedElectivesOfferedFall2026": "1"
    },
    {
      "department": "ME",
      "advancedElectivesOfferedFall2026": "1"
    },
    {
      "department": "NE",
      "advancedElectivesOfferedFall2026": "1"
    },
    {
      "department": "TAM",
      "advancedElectivesOfferedFall2026": "1"
    }
  ],
  "limitations": []
}
```

Prediction: none. Hypothetical completions, where used, are assumptions. Full query, paths and graph hash remain in the raw JSON.


# Contribution and submission evidence

Representative commits were inspected on GitHub main. Planned scopes remain distinct from individually verified work; the final source commit and video are pending. ChatGPT was used to assist with code, documentation and prompts, and to cite external code, datasets, ontologies, prompts, libraries, tutorials and other resources. Trial 3 grading entries were prepared with tool assistance. Reviewer names and equal assignments were supplied by the team. Source commits establish development contributions separately from grading assignments.

| Member / GitHub | Planned scope | Verified representative commits |
| --- | --- | --- |
| Afaan Sohail / AfaanSohail | reasoning | https://github.com/AfaanSohail/course_planning/commit/0aa8217bce33e7e5eef186ea98e027a566dd02b9<br>https://github.com/AfaanSohail/course_planning/commit/cbc7fdd3741d5034e8357eaed801cdae85a0fe1e<br>https://github.com/AfaanSohail/course_planning/commit/734e226671d6f71b22433115af831b82e2eb2bcb |
| Hassan Tariq / hassan-cpp | app and prompts | https://github.com/AfaanSohail/course_planning/commit/5697732e26f19400970422e2909425c12eb590ea<br>https://github.com/AfaanSohail/course_planning/commit/1831b6393403628a33a80285663cbf07cbc06f1f<br>https://github.com/AfaanSohail/course_planning/commit/27706929cf4b5cf83a4cd9a267689045f83c721d |
| Diya Hurmat / Diya22466 | evaluation, explainability and report | https://github.com/AfaanSohail/course_planning/commit/6379dfc8f7f6fe403a1f9720758d124c1734083e<br>https://github.com/AfaanSohail/course_planning/commit/ff143e2643d6090f91a2dbd6bb168050e5bba850<br>https://github.com/AfaanSohail/course_planning/commit/c3e3cc04a1713bdf0fa57e546d7524d78d2e3f75 |


# Recorded execution environment

```
Python: 3.11.7
Platform: Linux-7.0.0-43-generic-x86_64-with-glibc2.39
rdflib==7.6.0
owlrl==7.6.2
pyparsing==3.3.3
pandas==2.2.2
requests==2.31.0
pytest==7.4.0
pyshacl==0.40.2
reportlab==5.1.0
python-docx==1.2.0

```
