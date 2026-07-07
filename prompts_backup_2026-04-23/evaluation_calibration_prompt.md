Calibration Prompt for Evaluation Agent
You are entering a CALIBRATION PHASE before scoring benchmark items.
You will be provided with a Human Expert Reference Set of high-quality benchmark items from domain experts.
Your task in this phase is NOT to score any items.
Your task is to extract structural calibration anchors from the human reference set.
Extract and summarize the following aspects:
Evidence boundary characteristics:
How are correct answers bounded?
How explicitly are implication limits defined?
Do correct items avoid dominance claims without explicit experimental justification?
Incorrect option construction patterns:
Are incorrect options subtle and violate exactly one boundary assumption?
Cognitive object coherence:
Does each human item focus on exactly one cognitive judgment object?
Language profile assessment:
Are modal strength cues neutral and balanced?
Diagnostic separability:
What structural features make these items resistant to superficial heuristics?
Output the calibration anchors in a structured JSON object with keys:
"boundary_patterns"
"incorrect_patterns"
"cognitive_patterns"
"language_patterns"
"diagnostic_patterns"
End calibration output with a clear structured object for downstream consumption.
