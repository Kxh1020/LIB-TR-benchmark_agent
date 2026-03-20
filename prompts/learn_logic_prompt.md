Task definition:
You are analyzing a collection of human-written multiple-choice questions (MCQs) from a scientific reasoning benchmark.
Your goal is to reverse the question design strategies used by human experts.
Do not summarize the questions.
Instead, extract generalizable rules that an AI system could follow to generate high-quality MCQs with similar reasoning characteristics.
The goal is to identify design patterns that make the questions scientifically valid, reasoning-oriented, and resistant to superficial guessing.
Analysis dimensions
Analyze the MCQs along the following dimensions.
Focus on extracting repeatable design patterns.
1. Question Stem Construction
Identify how human authors construct the question scenario.
Look for patterns such as:
presenting experimental observations without revealing interpretation
describing system conditions but omitting key conclusions
including partial evidence that requires reasoning to interpret
Focus on rules that guide how to frame the scientific situation.
2. Evidence-to-Question Transformation
Identify how factual evidence is converted into reasoning questions.
Examples of patterns to detect:
turning experimental observations into causal reasoning tasks
combining multiple facts into a constraint-based question
asking what is supported rather than what is true
Extract rules describing how evidence becomes a reasoning challenge.
3. Distractor Design Archetypes
Identify common patterns used to construct plausible but incorrect options.
Typical distractor archetypes may include:
Overgeneralization
using absolute claims such as "always", "inevitably", "completely"
Mechanism confusion
mixing correct processes with incorrect mechanisms
Condition violation
statements that are true in general but not under the given conditions
Scope expansion
extending a local result into a universal rule
Numerical exaggeration
inflating magnitude relationships or thresholds
Extract rules explaining how distractors are designed to be plausible but incorrect.
4. Reasoning Requirements
Identify what type of reasoning the questions require.
Look for patterns such as:
causal reasoning
constraint-based reasoning
thermodynamic reasoning
system interaction reasoning
elimination via contradiction
Extract rules that force solvers to reason rather than recall facts.
5. Difficulty Control
Identify how human authors control question difficulty.
Look for mechanisms such as:
providing partial information
avoiding obvious keyword cues
mixing multiple interacting factors
including distractors that are partially correct
Extract rules describing how difficulty is calibrated.
Output requirements
Produce concise and actionable design rules that can guide an AI system to generate similar questions.
Rules must describe how to construct questions, not describe the dataset.
Each rule should be specific enough to be directly implemented in a question generator.
Output quality constraints
Prefer numbered rules.
Use short bullet points if helpful.
Use short sentences.
Avoid long paragraphs.
Avoid vague advice.
Each rule should describe a clear design pattern.
Good rule example:
"Describe experimental observations but omit the author's interpretation."
Bad rule example:
"Make the question challenging."
Formatting rules
Use numbered rules.
Bullet points are allowed.
Markdown formatting is allowed.
Code fences are allowed if useful.
Hard constraint:
Do NOT output JSON.
