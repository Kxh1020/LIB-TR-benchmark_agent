Task Definition
Analyze human-written multiple-choice questions (MCQs) from a scientific reasoning benchmark.
Your core goal:
Reverse-engineer expert question design logic and extract reusable rules that can guide an AI system to generate high-quality engineering reasoning MCQs.
You are NOT analyzing the questions themselves.
You are extracting question construction rules.
The output rules must be:
generalizable
implementable
reusable
applicable to new domains
focused on reasoning, not factual recall
focused on engineering admissibility judgment
Do NOT summarize the input questions.
Do NOT discuss specific question content.
Extract only repeatable design patterns.
Analysis Dimensions (Expanded)
Extract ONLY repeatable, implementable design rules across the following dimensions:
1. Question Stem Construction Rules
Extract rules describing how experts construct stems.
Focus on patterns such as:
scenario-first framing
presenting observations without interpretation
providing partial conditions
defining constraints
including interacting factors
omitting key conclusions
forcing solver-side reasoning
defining system boundaries
including relevant but incomplete evidence
embedding mechanism clues without stating conclusions
defining local conditions but asking system-level judgment
presenting cause but not outcome
presenting outcome but not cause
including competing mechanisms
including regime-dependent behavior
Goal: Extract stem construction templates, not descriptions.
2. Evidence-to-Question Transformation Rules
Extract rules describing how experts transform factual evidence into reasoning questions.
Focus on patterns such as:
turning experimental observations into causal reasoning tasks
converting parameter relationships into admissibility judgments
combining multiple facts into constraint-based reasoning
converting trends into boundary reasoning questions
asking what is supported, not what is true
testing non-implication instead of implication
forcing solver to evaluate whether a conclusion is justified
distinguishing component behavior vs system behavior
converting condition-dependent behavior into regime reasoning
combining thermal, electrical, mechanical interactions
using partial evidence to constrain conclusions
forcing solver to reject overgeneralized conclusions
forcing solver to identify unsupported extrapolations
Goal: Extract evidence → reasoning task transformation rules.
3. Distractor Design Archetypes
Extract rules for designing plausible but incorrect options.
Focus on these core archetypes:
Overgeneralization
Extending local results to universal rules
Mechanism Confusion
Correct phenomenon but incorrect cause
Condition Violation
Statement true in general but invalid under given conditions
Scope Expansion
Component-level result → system-level conclusion
Numerical Exaggeration
Overstated magnitude or threshold
Ignoring Boundary Conditions
Conclusion valid only under specific regime
Regime Transfer Error
Behavior transferred across SOC, temperature, confinement, etc.
Causal Overclaim
Correlation interpreted as causation
Ignoring Multi-factor Interaction
Assuming single-variable behavior in multi-variable system
Engineering Recommendation from Limited Evidence
Local observation → design recommendation
Extract rules describing how to construct these distractors, not descriptions of them.
4. Reasoning Requirements
Extract rules that ensure questions require reasoning rather than fact recall.
Focus on reasoning structures such as:
causal chain reasoning
constraint-based reasoning
boundary / admissibility reasoning
regime-dependent reasoning
scale transfer reasoning
system interaction reasoning
trade-off reasoning
elimination via contradiction
multi-factor reasoning
mechanism competition reasoning
failure mode reasoning
safety engineering reasoning
diagnostic signal reasoning
propagation reasoning
parameter sensitivity reasoning
Extract rules describing how to force these reasoning processes through question design.
5. Difficulty Control Rules
Extract rules describing how experts control difficulty.
Focus on mechanisms such as:
providing incomplete but sufficient information
avoiding keyword matching
mixing multiple interacting variables
including partially correct distractors
forcing boundary judgments
requiring elimination instead of recognition
including counterintuitive but correct options
requiring multi-step reasoning
requiring distinguishing admissible vs plausible conclusions
including realistic engineering trade-offs
avoiding obvious incorrect options
including options that are correct in general but not under given conditions
requiring solver to identify unsupported extrapolation
limiting numerical cues
using qualitative reasoning instead of numerical calculation
presenting competing mechanisms
requiring solver to reason about system behavior rather than component behavior
Extract rules describing how difficulty is engineered.
Output Requirements
Output concise, actionable design rules.
Rules must:
be implementable
be generalizable
guide question generation
be phrased as construction rules
be specific
be short
be numbered
be grouped by category
not refer to the input questions
not include examples from the input
not include long explanations
not include vague advice
Good rule example:
"Describe system conditions and observations but omit the causal explanation."
"Include two interacting variables so that single-variable reasoning fails."
"Construct one distractor by extending a local observation to a system-level recommendation."
Bad rule example:
"Make the question challenging."
"Use good distractors."
"Ask about mechanisms."
Output Structure
Organize rules into the following sections:
Stem Construction Rules
Evidence Transformation Rules
Distractor Design Rules
Reasoning Enforcement Rules
Difficulty Control Rules
Each section should contain numbered rules.
Use short bullet points or short sentences.
Do NOT output JSON.
Do NOT summarize the dataset.
Do NOT describe specific questions.
Output only the rules.
