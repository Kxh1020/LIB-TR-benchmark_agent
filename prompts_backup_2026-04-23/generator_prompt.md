
BENCHMARK ALIGNMENT (MANDATORY)
First, study the benchmark MCQs written by human experts.
All generated items should match their reasoning depth, cognitive style, admissibility framing, and engineering judgment level.
The benchmark examples are provided only to learn latent design logic:
scenario-first engineering framing
explicit local conditions
admissibility / justification judgment
boundary-sensitive reasoning
plausible expert misinterpretations
conditional conclusions
engineering mechanism chaining
These examples define reasoning style and question construction patterns only.
They are stylistic references, not factual sources or templates.
Do NOT imitate surface wording, topic-specific facts, or option phrasing.


EVIDENCE-DRIVEN CONSTRUCTION PRINCIPLE

All questions must be constructed based on the provided evidence bundles.
Evidence bundles are the only correctness anchors and define:
admissible conclusions
boundaries
limitations
condition-dependent behavior
mechanism relationships
comparisons
safety implications

Rules:
Do NOT invent facts not supported by evidence.
Do NOT introduce new thresholds, values, or mechanisms.
Do NOT generalize beyond the evidence scope unless required by a minimal engineering implication.
Do NOT assume system-level behavior from component-level evidence unless supported.
Do NOT convert conditional statements into universal conclusions.
If evidence is insufficient, prefer conservative interpretation.

Each question must be evidence-driven but reasoning-based.
Evidence should be transformed into:
scenario conditions
constraints
mechanism hints
boundary conditions
admissibility judgments

Questions must NOT be answerable by directly restating evidence.


EVIDENCE TRANSFORMATION AND TERMINOLOGY CONTROL (NEW – CRITICAL)

When transforming evidence into stems and options:

1. Do NOT copy evidence sentences verbatim into the stem or options.
2. Do NOT invent new technical terminology, regime names, mechanism labels, or conceptual categories that do not appear in the evidence.
3. Prefer using terminology that already exists in the evidence when referring to mechanisms, phenomena, materials, or behaviors.
4. If a new descriptive phrase must be introduced, it must describe observable behavior, conditions, or mechanisms clearly, not create a new abstract concept.
5. The transformation from evidence to question should be structural, not terminological:
   - change experimental descriptions into engineering scenarios
   - convert observations into constraints or conditions
   - convert conclusions into admissibility judgments
   - convert trends into boundary reasoning situations
6. Difficulty must come from reasoning, boundary judgment, mechanism interaction, or trade-offs,
   NOT from unfamiliar wording or invented terminology.
7. The solver should struggle because of reasoning complexity, not because of vocabulary interpretation.
8. If a concept can be described using conditions, mechanisms, or behavior, do NOT replace it with a newly invented term.
9. Prefer concrete descriptions over abstract labels.
10. The wording in stems and options must remain evidence-grounded even after transformation.


CORE GENERATION OBJECTIVE
Your goal is to generate high-difficulty closed-book engineering reasoning questions.
Each question must test engineering admissibility judgment, not factual recall.
The solver will have access only to:
the question stem
the answer options
general engineering / physical reasoning
The solver will NOT have access to:
papers
figures
tables
citations
experimental data
hidden evidence
Questions must be solvable using:
stem conditions
fundamental engineering principles
mechanism reasoning
boundary reasoning
scale reasoning
safety engineering judgment


QUESTION CONSTRUCTION PROCESS (MANDATORY INTERNAL LOGIC)
Before writing each item, internally perform the following steps:
Identify the target cognitive object.
Select relevant evidence claim units.
Identify the primary boundary.
Identify a tempting but invalid overclaim.
Determine the reasoning type.
Construct the mechanism or reasoning chain.
Transform evidence into scenario conditions.
Write the stem without revealing the conclusion.
Construct options:
correct options = admissible conclusions
incorrect options = boundary violations
If a question does not involve a clear admissibility boundary or reasoning chain, discard the item.


MULTI-HOP ENGINEERING REASONING
Each question MUST require multi-step engineering reasoning.
A valid item must involve at least two of the following reasoning steps:
mechanism → consequence
condition → regime change
parameter → system behavior
component behavior → system implication
thermal → electrochemical coupling
safety measure → risk change
material property → failure mode
scaling (cell → module → pack)
boundary reasoning (valid / not valid)
trade-off reasoning (safety vs performance)
A question that can be solved by a single fact recall is NOT allowed.
Each correct option must require at least one reasoning step, not direct recall.


REASONING TYPE TAXONOMY
Each generated question must belong to one of the following reasoning categories:
Causal Mechanism Reasoning
Boundary / Admissibility Reasoning
Regime Transfer Reasoning
Scale Transfer Reasoning
Safety Engineering Trade-off Reasoning
Failure Mode Reasoning
Signal / Diagnostic Reasoning
Design Strategy Reasoning
Multi-factor Interaction Reasoning
The generator should maintain balanced distribution across reasoning types across the dataset.


EVIDENCE AND BOUNDARY RULES
Use the provided evidence bundles only as hidden correctness anchors.
Additional rules:
Evidence must be transformed into reasoning scenarios, not copied directly.
Prefer combining multiple evidence claims to create multi-hop reasoning.
Questions should test whether conclusions are admissible under evidence constraints.
Evidence defines both:
what can be concluded
what cannot be concluded
Boundary violations should be used to construct distractors.
Correct options must stay within evidence-supported boundaries.
Incorrect options should violate one primary boundary.
Every correct option must be:
an evidence-supported statement, or
a minimal engineering implication from stem conditions plus stable engineering principles.
Correct options must NOT depend on hidden paper-specific details.


STEM CONSTRUCTION RULES
The stem must be:
closed-book solvable
self-contained
scenario-driven
condition-explicit
judgment-oriented
The stem should include:
engineering scenario
relevant local conditions
constraints
known relationships
judgment task
The stem must NOT include:
papers
experiments
citations
figures
tables
data references
hidden assumptions
If an option depends on a condition, that condition must appear in the stem.
The stem should transform evidence into engineering scenario conditions rather than restating experimental observations.


DISTRACTOR DESIGN RULES
Incorrect options must be technically plausible and fail for a specific engineering reason.
Common distractor failure modes:
scale transfer beyond evidence
regime transfer beyond stated conditions
causal overclaim
unjustified monotonicity
system-level recommendation from local observation
mechanism substitution
ignoring thermal-electrochemical coupling
ignoring confinement effects
ignoring SOC dependence
confusing trigger vs propagation
Avoid:
strawman distractors
wording tricks
obviously wrong options
options that fail only because of absolute wording
At least one distractor must be:
engineering-common-sense but unsupported


COUNTERINTUITIVE AND NON-HEURISTIC DESIGN (NEW – CRITICAL)
To prevent heuristic solving based on “conservative vs aggressive reasoning”, enforce the following:
Counterintuitive but correct options
At least one correct option per MCQ should:
appear counterintuitive or violate a common engineering heuristic
require mechanism-based or multi-step reasoning
not be trivially aligned with “safe” or “conservative” reasoning
Conservative but incorrect options
At least one incorrect option must:
appear cautious, conditional, or epistemically modest
still be incorrect due to boundary violation or mechanism inconsistency
Heuristic-breaking requirement
The following heuristic must be broken:
“Conservative statements are likely correct; strong claims are likely incorrect.”
Therefore:
Some correct options may contain strong conclusions
Some incorrect options may appear cautious
INTER-OPTION DEPENDENCY DESIGN (NEW – HIGH PRIORITY)
Options should NOT be fully independent.
At least one MCQ must include logical relationships between options:
mutual exclusivity
conditional dependency
shared boundary condition
competing interpretations
mechanism conflict
The solver should need to compare options rather than judge each independently.


ABSOLUTE-LANGUAGE AND CUE-LEAK CONTROL
Incorrect options must not be trivially rejectable due to absolute or categorical wording alone.
Rules:
Do not make an option incorrect mainly because it uses words like always, never, necessarily, must, guarantees, completely, eliminates, proves, or only.
Prefer distractors that remain incorrect even after softening extreme wording.
Correct and incorrect options should have comparable rhetorical strength.
The item must not be solvable mainly by detecting linguistic exaggeration or hedging asymmetry.
INTERNAL ITEM PLANNING
Before writing each item, internally identify:
target cognitive object
main admissible conclusion
tempting but invalid overclaim
boundary separating them
reasoning type
mechanism chain involved
If the boundary tension is weak, discard the item.


HEURISTIC-RESISTANCE CHECK (MANDATORY INTERNAL CHECK)
Before finalizing each item, internally check:
Can the question be solved by selecting only cautious or non-committal statements?
Can the solver ignore engineering content and still achieve high accuracy?
Does at least one correct option appear initially questionable or counterintuitive?
Does at least one incorrect option appear reasonable even after careful reading?
Are options interdependent rather than independent?
If yes, revise the item.


DIFFICULTY REQUIREMENTS (ENHANCED)
A high-difficulty item must satisfy at least TWO of:
multi-step mechanism reasoning
admissibility / non-implicability judgment
regime-dependent conclusion
scale inference boundary
safety trade-off reasoning
multi-factor interaction reasoning
plausible expert distractor
counterintuitive but correct conclusion
conservative but incorrect distractor
inter-option dependency
Difficulty must arise from:
reasoning conflict
boundary tension
competing interpretations
mechanism interactions


Length limits:
stem ≤ 90 words
option ≤ 50 words
justification ≤ 28 words
short answer ≤ 120 words

OUTPUT FORMAT
Output JSON-only schema (no extra text): { "mcqs":[ { "qid":"Q1", "type":"MCQ", "solver_view":{"stem":"...","options":["A ...","B ...","C ...","D ...","E ..."]}, "ground_truth":{ "correct_options":["A","C"], "option_judgments":[ {"option_id":"A","label":"Correct","justification":"...","error_type":null,"evidence_refs":["C1"]} ] }, "analysis":{ "target_cognitive_object":"...", "primary_boundary":"...", "intended_error_modes":["..."], "disallowed_extrapolations":["..."] } } ], "short_answers":[ { "qid":"S1", "type":"SHORT_ANSWER", "solver_view":{"prompt":"..."}, "ground_truth":{ "gold_answer":"...", "must_include":["..."], "disallowed_extrapolations":["..."] }, "analysis":{ "target_cognitive_object":"...", "primary_boundary":"...", "intended_error_modes":["..."] } } ] }


HARD CONSTRAINTS
Per bundle:
generate 2–3 MCQs
generate 1 short-answer
MCQ:
5–7 options
1–4 correct options
prefer 2–3 correct options

Evidence:
each question must cite at least one claim_id
do NOT invent evidence ids
Solver-view:
no hints
no references to paper or evidence
Output:
JSON only
no markdown
no extra text
Additional hard constraints:
At least one correct option must be counterintuitive.
At least one incorrect option must be conservative but wrong.
At least one pair of options must be logically dependent.
The question must not be solvable by selecting all cautious statements.
Correctness must not correlate with rhetorical strength or hedging level.