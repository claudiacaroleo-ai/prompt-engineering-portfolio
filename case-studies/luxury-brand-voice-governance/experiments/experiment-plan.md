\# Experiment plan – cross-model and context effects



\## Why this experiment exists



This experiment extends the original case study by testing two open questions:



1\. Do different LLMs respond differently to the same prompt and evaluation criteria?

2\. Does the final prompt remain effective when used in isolation, without conversational memory?



The goal is not to rank models, but to understand differences in behavior and failure modes.



\## What stays fixed



\- Same prompts:

&nbsp; - baseline\_prompt.md

&nbsp; - iteration\_03\_prompt.md

\- Same evaluation rubric:

&nbsp; - evaluation\_criteria.md

\- Same input scenario(s)



\## Variables under test



\### A. Cross-model comparison

The same prompts are tested across multiple LLMs to observe:

\- tone alignment

\- linguistic stability

\- instruction-following behavior

\- recurring failure modes



\### B. Context / memory effect

The final prompt is tested in two conditions:

\- fresh session (no prior context)

\- with an explicit context pack summarizing prior constraints



\## How results are evaluated



Each output is scored using the same qualitative rubric.

Scores and observations are logged explicitly.



\## Expected outcome



The experiment should clarify:

\- whether prompt improvements are model-dependent

\- whether conversational memory materially affects output quality

\- which risks emerge in production-like conditions



