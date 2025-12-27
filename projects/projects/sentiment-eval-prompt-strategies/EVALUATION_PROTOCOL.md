# Evaluation protocol

I define the evaluation protocol before running any experiments to ensure that prompt strategies are compared in a consistent and defensible way.

The goal is not only to measure performance, but to understand *how* and *why* different strategies fail or succeed on real customer reviews.

## Experimental setup

- Dataset: `luxury_reviews_100.csv` (100 reviews, balanced 50/50)
- Model: ChatGPT (same model and version across all runs)
- Variable under test: prompt strategy only
- Input reviews are identical across strategies

## Automatic metrics

### Accuracy
Accuracy is calculated as the percentage of correctly classified reviews over the full dataset.

This metric provides a clear and interpretable baseline for comparing prompt strategies.

### Confusion matrix
I compute a confusion matrix for each strategy to analyze:
- false positives (negative reviews classified as positive)
- false negatives (positive reviews classified as negative)

This helps identify asymmetric failure patterns.

## Qualitative error analysis

In addition to numeric metrics, I manually inspect misclassified reviews and assign error categories such as:
- implicit dissatisfaction
- sarcastic or ironic language
- mixed or ambivalent sentiment
- expectation mismatch typical of luxury contexts

This analysis helps explain *why* accuracy differs across strategies.

## Evaluation consistency

To reduce variability:
- I run each strategy on the full dataset using the same prompt structure
- I avoid prompt tweaks between runs
- I document any anomalies or unexpected outputs
