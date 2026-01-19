\# Future experiments and open questions



This case study focused on improving controllability and tone stability through prompt iteration and explicit evaluation criteria, using a single model to reduce variability.



After publishing it, I received a valuable suggestion that highlights two natural extensions of the work: cross-model comparison and context/memory effects. I’m documenting them here as planned follow-ups.



\## 1) Cross-model comparison



A next step would be to repeat the same workflow (baseline → iterations → scoring) on multiple LLMs, keeping the rubric constant.



The goal is to understand what changes are driven by:

\- the prompt structure and constraints

vs

\- the model’s linguistic sensitivity and instruction-following behavior



What I would measure:

\- tone alignment score (same rubric)

\- stability across runs (same prompt, multiple generations)

\- failure modes (what breaks first, and how)



Why it matters in governance contexts:

\- it avoids overfitting a “good prompt” to a single model

\- it helps choose the right model for brand-sensitive language, not just the cheapest or fastest



\## 2) Context and memory effects (does the conversation help?)



Another open question is whether later improvements are:

\- intrinsic to the final prompt design

or

\- partially dependent on the context accumulated during previous iterations



A simple controlled test:

1\. Reset model memory (fresh session)

2\. Run the final prompt in isolation (iteration\_03\_prompt)

3\. Score the output with the same rubric

4\. Compare it to the output produced when the model has full context



What this tells us:

\- If quality drops, part of the improvement may come from “context priming”

\- If quality holds, the prompt is more robust and portable



This distinction matters in production, where prompts are often executed in isolation.



\## Notes



These experiments intentionally come after the rubric and iteration log are in place. Without stable evaluation criteria, cross-model comparisons risk becoming subjective.



