# Prompt strategies

Before writing individual prompts, I define the prompt strategies I want to compare.

My goal is not to find a single “best” prompt, but to understand how different prompting approaches behave in terms of accuracy, stability, and cost when applied to real customer reviews.

## Strategy 1: Zero-shot baseline
This strategy uses a minimal instruction with no examples or domain context.

Rationale:
- establishes a low-cost baseline
- helps quantify task difficulty
- highlights variance and common failure modes

Expected trade-offs:
- lower stability
- higher sensitivity to ambiguous language and sarcasm

## Strategy 2: Few-shot generic
This strategy provides a small set of labeled examples (positive and negative) without domain-specific framing.

Rationale:
- reduces ambiguity by grounding the task with examples
- often improves consistency over zero-shot approaches

Expected trade-offs:
- higher token cost
- potential bias toward the provided examples

## Strategy 3: Domain-aware (luxury beauty)
This strategy explicitly frames sentiment classification within a luxury beauty context.

Rationale:
- aligns the model with domain-specific language and expectations
- helps interpret implicit sentiment common in luxury reviews

Expected trade-offs:
- increased prompt length
- risk of over-constraining the model
