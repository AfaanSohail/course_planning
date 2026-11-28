# Evaluation notes

These assessments compare the actual responses with the frozen expected rows and saved evidence. Reviewer names were supplied by the team. Hassan Tariq and Diya Hurmat are assigned ten entries each, covering five questions per person in both conditions. Assignments do not independently establish that each review has been completed. The original grading sheet and all raw responses are preserved.

Counts of unsupported claims depend on interpreting qualified and repeated statements. The notes explain each counted claim so that the team can confirm or revise the judgment. This is especially relevant to the baseline refusals.

## CQ01 condition A

Correct: No. Evidence available: No. Unsupported claims: 0.

The answer explains that the transcript and catalog are unavailable. It does not invent course choices, but it does not answer which courses S002 can take.

## CQ01 condition B

Correct: Yes. Evidence available: Yes. Unsupported claims: 0.

All 15 expected courses, titles and satisfied-option counts are present. The earlier incorrect total is gone. The row citations and saved graph evidence support the list.

## CQ02 condition A

Correct: No. Evidence available: No. Unsupported claims: 0.

The model cannot identify prerequisite chains without the catalog. This is a reasonable refusal, but it does not provide the requested chains or alternatives.

## CQ02 condition B

Correct: No. Evidence available: Yes. Unsupported claims: 0.

The 76 returned direct edges match the expected rows, but three of 79 edges are missing: ASRM 210 to MATH 231, ASRM 406 to MATH 241, and BIOE 210 to MATH 231. The answer is incomplete. These omissions are not invented claims. Full graph paths and group structure remain available in the saved retrieval artifact.

## CQ03 condition A

Correct: No. Evidence available: No. Unsupported claims: 0.

The answer identifies the missing transcript and prerequisite data without guessing. It does not establish which CS 421 conditions are met or unmet for S003.

## CQ03 condition B

Correct: Yes. Evidence available: Yes. Unsupported claims: 0.

All three prerequisite conditions have the expected status. The CS 374 or ECE 374 condition remains unmet, so option 1 is not met. The response does not turn that result into an official registration decision. Its row citations and completion evidence support the assessment.

## CQ04 condition A

Correct: No. Evidence available: No. Unsupported claims: 2.

The answer eventually acknowledges missing dependency data, but its opening makes two unsupported negative claims: (1) no downstream courses become available, and (2) no additional conditions are triggered. The expected results contain satisfiable downstream courses and remaining conditions. A lack of access cannot establish either negative conclusion.

## CQ04 condition B

Correct: Yes. Evidence available: Yes. Unsupported claims: 0.

All 28 expected rows are included. The answer separates the 11 still-blocked rows from the 17 rows that would become satisfiable and preserves the remaining conditions. The citations support the rows. The hypothetical scenario comes from the question. This checks agreement with the frozen expected rows rather than independently validating the catalog parser.

## CQ06 condition A

Correct: No. Evidence available: No. Unsupported claims: 0.

The model correctly avoids calculating progress without a transcript and degree structure. It provides no requirement-group results, so it does not answer the question.

## CQ06 condition B

Correct: No. Evidence available: Yes. Unsupported claims: 0.

The 15 displayed requirement groups agree with the expected figures, but the answer omits the completed Calculus I, Linear algebra and Orientation groups. The question asks for each group, including groups with zero remaining courses. The saved evidence supports the displayed figures, but the set is incomplete.

## CQ08 condition A

Correct: No. Evidence available: No. Unsupported claims: 1.

Most of the response describes missing prerequisite data. However, the statement that no alternative branches are reachable because structural information is missing is an unsupported negative reachability claim. The absence of access cannot establish that no path exists. The answer provides none of the expected upstream results.

## CQ08 condition B

Correct: Yes. Evidence available: Yes. Unsupported claims: 0.

All 56 expected upstream-course, intermediate-course and branch-type rows are reproduced exactly. This fixes the previous false empty-result answer. The row citations and saved graph evidence support the traversal results.

## CQ10 condition A

Correct: No. Evidence available: No. Unsupported claims: 0.

The model states that it lacks the catalog and substitution policy. It does not invent a cross-listing or policy, but it provides none of the requested downstream references.

## CQ10 condition B

Correct: No. Evidence available: Yes. Unsupported claims: 0.

The answer correctly explains that failure to establish acceptance of both codes is not a substitution ban. However, CS 581 is missing, leaving eight of nine expected downstream rows. The answer is incomplete. Its displayed references have supporting provenance in the saved artifact.

## CQ11 condition A

Correct: No. Evidence available: No. Unsupported claims: 2.

The answer refuses to provide counts without course data. It also incorrectly says that (1) no term and (2) no elective group are defined in the supplied context. The question explicitly identifies Fall 2026 and the advanced elective group. Their definitions and membership may be unavailable, but their identities are provided. No departmental counts are returned.

## CQ11 condition B

Correct: Yes. Evidence available: Yes. Unsupported claims: 0.

All 16 departments and their expected counts are present. The response does not add an unsupported total or policy. The saved derived rows and inferred graph evidence support the aggregate, although the answer itself omits inline row citations.

## CQ13 condition A

Correct: No. Evidence available: No. Unsupported claims: 0.

The answer explains that it cannot calculate a hypothetical change without the transcript and prerequisite graph. It avoids inventing recommendations but does not provide the requested change.

## CQ13 condition B

Correct: No. Evidence available: No. Unsupported claims: 1.

All 17 expected course rows are correct, and the answer distinguishes these from 71 downstream candidates. However, it adds one unsupported blanket claim: no course has a prerequisite independent of CS 225. Becoming eligible after adding CS 225 does not establish that all other prerequisites depend on CS 225. The table has supporting evidence, but that added conclusion does not, so the complete answer fails the correctness and supporting-evidence checks.

## CQ15 condition A

Correct: No. Evidence available: No. Unsupported claims: 1.

The model has no transcript or catalog evidence and does not answer the requested question. It also incorrectly says that no student instance or course schedule has been presented. The question identifies S002 and Fall 2026. The detailed planned courses are unavailable to the baseline, but the student instance is provided.

## CQ15 condition B

Correct: Yes. Evidence available: Yes. Unsupported claims: 0.

All three planned courses are covered. The answer gives the catalog wording, degree requirement and supporting prerequisite completions. It keeps the CS 101 or equivalent programming-experience condition for MATH 257 unverified. The row citations and recorded completion codes support the answer, and it does not invent an official registration decision.
