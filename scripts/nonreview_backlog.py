#!/usr/bin/env python3
"""Separate executable work from external closure evidence without rewriting the ledger."""
from collections import Counter
import json
from nonreview_common import roots,receipt,cli,digest,safe
# Explicit item-level judgments, not keyword-based classifications.
ACTIONS={
1:('SOURCE_AND_SPECIALIST','Trace each queued alternative to two page-level assertions; preserve dependence and shared-locus uncertainty.','Inspect both actual editions and obtain an attributable disposition before admitting a pair.'),
5:('EVALUATION','Freeze new task/source commitments and preserve untouched outputs, failures and exposure logs.','Unexposed cases and an independently checked confirmatory design.'),
6:('EVALUATION','Serialize exposure histories for all 24 labels and replay eligibility decisions.','Authenticated cohort history and independent verification of scoring eligibility.'),
7:('METHOD','Execute declared competing/control models and explicitly retain structural-only claims in the absence of discrimination.','Evidence supporting any stronger linguistic inference; software success alone is insufficient.'),
8:('SOURCE_AND_SPECIALIST','Run separately labelled cluster sensitivity scenarios; never overwrite identity with heuristic joins.','Authority-backed physical-unit crosswalk.'),
9:('METHOD','Enumerate inclusion strata, missingness and sensitivity analyses within evidenced populations.','Source coverage sufficient for the proposed generalization.'),
10:('SOURCE_AND_EVALUATION','Freeze aligned prediction/gold schema and leakage checks; test rejection of absent gold.','Lawfully accessible aligned linguistic gold and source-qualified scoring.'),
11:('SOURCE_ACCESS','Build reproducible degradation code using explicitly labelled synthetic controls.','Source-bound graphical controls with applicable permission and a frozen experimental design.'),
12:('SOURCE_ACCESS','Give each of the eight records a source/locus and occurrence-coverage disposition.','Actual source access for occurrence encoding or evidence supporting exclusion.'),
13:('DEPENDENCE','Enumerate source-specific assertions, units and known dependence; retain unknowns.','Evidence sufficient to assert independence for any selected witnesses.'),
14:('SOURCE_ACCESS','Publish per-entry reading coverage and exact unavailable-source exclusions.','Accessible source-bound readings for any additional transcription claim.'),
16:('SOURCE_AND_SPECIALIST','Bind sequence, layout and uncertainty to precise inspected source loci.','Source-supported complete sequences and review required by the admission policy.'),
18:('SOURCE_AND_SPECIALIST','Expose parallel source-specific directions, layouts and counts without pooling incompatible conventions.','Actual source assertions for every conflict; adjudication only if a resolved value is claimed.'),
19:('SOURCE_AND_SPECIALIST','Implement explicit included/excluded/unknown source-class filters and bounded denominators.','Authenticated source classification for whole-population linguistic claims.'),
20:('SPECIALIST','Package Greek parallels and uncertain component assignments without promoting them to gold.','Attributable component-level linguistic decisions with inspected loci.'),
22:('SOURCE_AND_SPECIALIST','Trace historical reading versions to exact loci and list nonadmitted rows.','Review and source evidence required by native admission.'),
23:('SOURCE_AND_SPECIALIST','Preserve digital entries and candidate object relations as different units.','Authority-backed object relations for any physical-population claim.'),
24:('SOURCE_AND_SPECIALIST','Trace apparatus alternatives to both real loci and document shared upstream editions.','Source-supported pair and reviewer decision before scholarly admission.'),
26:('SOURCE_AND_SPECIALIST','Resolve or explicitly exclude each of the 159 missing edition-lineage groups.','Inspected exact source joins and required review for admitted records.'),
27:('SOURCE_ACCESS','Expand bounded edition comparisons, recording restorations and line-fold transformations.','Actual consulted pages for each expanded claim; generic parallels remain contextual.'),
28:('SOURCE_ACCESS','Build text/object/bibliography crosswalks only where exact source evidence exists.','Missing text/object sources and component permissions.'),
29:('SOURCE_ACCESS','Represent each face as covered, unavailable or excluded, preserving source geometry.','Accessible source-bound face geometry and object relations.'),
30:('SPECIALIST','Prepare attributable sign/membership dossiers with conflicts and uncertainty.','Case-specific expert decisions; engineering parity is insufficient.'),
31:('SOURCE_ACCESS','Keep historical segmentations and counts separate; record source-access outcomes.','Authoritative inspectable geometry for asserted boundaries.'),
32:('SOURCE_AND_SPECIALIST','Apply Lydian row-level source-admission checks and preserve reference-only exclusions.','Inspected source evidence meeting the native admission policy.'),
33:('SOURCE_AND_SPECIALIST','Apply Sidetic row-level source-admission checks and preserve reference-only exclusions.','Inspected source evidence meeting the native admission policy.'),
34:('SOURCE_AND_SPECIALIST','Apply Pisidian row-level source-admission checks and preserve reference-only exclusions.','Inspected source evidence meeting the native admission policy.'),
35:('SPECIALIST','Validate packet completeness, exact slot/group targets and absence of fabricated assessments.','Attributable supported assessments for required Phaistos slots and groups.'),
36:('SPECIALIST','Exercise release rejection when external acceptance is absent.','Verified external-review receipt satisfying native acceptance conditions.'),
37:('EVALUATION','Run harder full-record retrieval development tasks, preserving source hashes and exposure limits.','Unexposed representative academic task selection for an academic-accuracy claim.'),
38:('SPECIALIST','Publish transparent field-level scoring and preserve raw model outputs.','Independent source-qualified grades and expertise/conflict disclosures.'),
39:('EVALUATION','Record all observable build/platform metadata and explicitly mark unknown builds.','Additional actually available model families/platforms; historical unknowns cannot be reconstructed.'),
40:('PARTICIPANTS','Implement timing/error collection and equal-evidence baseline tooling.','Actual consenting researcher participants and measured outcomes.'),
41:('DEPENDENCE','Screen short fields and source lineage; assign source-specific or unknown dependence without automatic object merges.','Evidence needed for semantic identity beyond the inspected source families.'),
42:('RIGHTS','Audit every concrete package member; exclude unresolved components from public redistribution.','Attributable component terms or permission for any newly included protected source.'),
43:('SOURCE_AND_SPECIALIST','Retain null combined counts and require explicit unit/dependence crosswalks.','Authenticated common denominator before any aggregate physical/sign claim.'),
49:('SOURCE_ACCESS','Attempt lawful access for the five missing primary sides; preserve individual failure receipts.','Actual inspected primary-page comparisons for all five sides.'),
50:('SOURCE_AND_SPECIALIST','Preserve both 09/10 assertions and exclude them from single-label gold.','Attributable correction only if resolving the source discrepancy.')}
FOLLOWUPS={
'FUP-003':('SOURCE_ACCESS','Search the 23 exact entry identifiers against inspectable edition routes; retain exclusions.','Actual verified edition locators, not search-result suggestions.'),
'FUP-015':('SPECIALIST','Preserve both material assertions and their independent provenance.','Attributable material/object adjudication for CHIC-202/252.'),
'FUP-017':('SOURCE_AND_SPECIALIST','Keep ordinal 32 and eight unassigned positions excluded from unambiguous lookup.','Inspect source/erratum evidence before resolving membership.'),
'FUP-021':('DEPENDENCE','Keep the source-entry union bounded and preserve per-view components.','Additional object/independence evidence for broader claims.'),
'FUP-025':('DEPENDENCE','Keep the exact-cache source-row union bounded and preserve access paths.','Reading/object/witness evidence beyond cache identity.')}
def build(parent):
    r=roots(parent)['Linear-A'];rp='corpus-factory/academic-defect-register-2026-10-23.json';sp='corpus-factory/academic-remediation-status.json'
    register=json.loads(safe(r,rp).read_bytes());status=json.loads(safe(r,sp).read_bytes());by={i['id']:i for i in register['items']};items=[]
    for s in status['items']:
        if s['current_status'] not in ('OPEN','MITIGATED_OPEN'):continue
        i=by[s['id']];kind,action,external=ACTIONS[int(i['id'][4:])]
        items.append({'id':i['id'],'title':i['title'],'scope':i['affected_scope'],'ledger_status':s['current_status'],'dependency_class':kind,'executable_without_academic_review':action,'remaining_closure_evidence':external,'original_closure_criteria':i['closure_criteria'],'criteria_changed':False})
    followups=[]
    for f in status['scientific_followups']:
        kind,action,external=FOLLOWUPS[f['id']];followups.append({**f,'dependency_class':kind,'executable_without_academic_review':action,'remaining_closure_evidence':external})
    if len(items)!=38 or len(followups)!=5 or {int(i['id'][4:]) for i in items}!=set(ACTIONS):raise ValueError('item-level classification scope drift')
    return {'format':'nonreview-backlog-disposition-v1','date':'2026-10-27','inputs':'inputs.json','register':{'path':rp,'sha256':digest(safe(r,rp).read_bytes())},'ledger':{'path':sp,'sha256':digest(safe(r,sp).read_bytes())},'totals':{'original_open':len(items),'scientific_followups':len(followups),'new_scholarly_closures':0},'classification_method':'Explicit desk classification of each unchanged closure criterion; executable subtasks do not imply that the whole item can close without new evidence.','items':items,'followups':followups,'by_dependency_class':dict(sorted(Counter(i['dependency_class'] for i in items).items()))}
if __name__=='__main__':
    a=cli(__doc__);r=receipt('backlog.json',build(a.checkouts),a.write);print(r['totals'])
