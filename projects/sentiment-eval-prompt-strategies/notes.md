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



