"""Query-result semantics computed at runtime, never CQ answers or predictions."""
from collections import Counter

SEMANTICS = {
    'Q02': ('Each row is a DIRECT prerequisite edge from fromCode to toCode; option identifies an OR alternative; '
            'conditions in an option are AND, and a one-of group is OR. Render ALL edges in a compact table, '
            'preserving edgeType and option. Do not invent flattened end-to-end paths or combine different branches. '
            'toIsBaseCourse means no recorded course prerequisite, not guaranteed permission.'),
    'Q08': ('Every row ALREADY establishes upstreamCode reachable from the question target via viaCode '
            'in at least two prerequisite-course links. Render ALL rows; do not reject this executed query result '
            'because individual RDF edges were omitted from the prompt. firstHop distinguishes required and possible alternatives.'),
    'Q06': ('Render EVERY requirement row, INCLUDING zero remainingCourses. Remaining credits are '
            'max(0,minCredits-allocatedCredits) when minCredits is known, otherwise unknown. '
            'Focus areas are alternatives, not eight compulsory requirements. Do not add overlapping group totals.'),
    'Q04': ('Rows separate would become satisfiable from still blocked. Render BOTH groups and each '
            'stillRequired condition verbatim; do not describe blocked candidates as unlocked.'),
    'Q13': ('Rows describe the query-level change under the hypothetical assumption. The number of '
            'downstream candidates in the trace is NOT the number newly eligible. Report row membership '
            'without claiming every prerequisite was previously unsatisfied.'),
    'Q10': ('acceptsBothCodes=true means both codes are explicitly mentioned in that downstream prerequisite. '
            'false means explicit acceptance of both was NOT established; it does NOT mean substitution is forbidden. '
            'Cross-listing alone does not establish general substitution policy.'),
    'Q15': ('Render all course rows with catalog wording, requirement, parseStatus and unverified fields. '
            'satisfiedOptions is a COUNT of alternatives, not a list of separate conditions. '
            'Do not invent grades, credits, completed degrees or official registration decisions.'),
}


def guidance_for(retrieval):
    rows = retrieval['rows']
    result = {'row_count': len(rows), 'semantics': SEMANTICS.get(retrieval['intent'],
              'Render every result row. Preserve the scope and limitations of this executed query.')}
    if rows and 'courseCode' in rows[0]:
        result['distinct_course_count'] = len({r['courseCode'] for r in rows})
    for field in ('status', 'eligibleIn'):
        if rows and field in rows[0]:
            result[field + '_row_counts'] = dict(Counter(r[field] for r in rows))
    return result
