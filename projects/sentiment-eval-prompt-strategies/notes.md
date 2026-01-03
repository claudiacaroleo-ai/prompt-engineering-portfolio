\## Zero-shot baseline – initial observations (n=10)



I ran an initial zero-shot evaluation on a small batch of 10 curated luxury beauty reviews to validate the experimental setup before scaling to the full dataset.



\### Overall behavior

The zero-shot prompt produces concise and confident outputs. However, predictions often rely on surface-level sentiment cues rather than deeper intent or expectation alignment.



\### Error patterns observed

From this initial batch, misclassifications tend to cluster around:

\- implicit dissatisfaction expressed through polite or neutral language

\- mixed sentiment reviews combining positive tone with unmet expectations

\- over-weighting of positive adjectives despite negative outcomes



These patterns are consistent with known challenges in interpreting beauty and luxury product feedback.



\### Strengths

\- low prompt complexity

\- fast and consistent predictions

\- solid performance on clearly polarized reviews



\### Limitations

\- limited sensitivity to implicit negative signals

\- no domain grounding for expectations vs outcomes



\### Decision

I will keep the zero-shot results as a baseline and proceed with more structured prompt strategies (few-shot and domain-aware) to address the observed failure modes.



\## Comparative observations (n=10)



Across the initial batch of 10 reviews, zero-shot, generic few-shot, and failure-aware few-shot strategies produced identical sentiment classifications.



This suggests that, for this dataset and task, the base model already handles binary sentiment classification reliably, even without examples.



The absence of differences is itself informative:

\- the zero-shot prompt was sufficiently clear and well-scoped

\- few-shot prompting did not add measurable value at this scale

\- more complex prompt engineering may be unnecessary for this use case



This result highlights an important practical insight: prompt complexity should be justified by observed failure modes and task difficulty, not assumed by default.

