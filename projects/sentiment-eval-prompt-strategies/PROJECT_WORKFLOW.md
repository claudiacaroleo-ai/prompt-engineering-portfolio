# Project workflow and methodology

This document describes the end-to-end workflow used to build and evaluate prompt strategies for sentiment classification on real luxury beauty reviews.

It documents not only the final results, but also the reasoning process, tooling decisions, and iteration steps that guided the project.

---

## 1. Repository structure and version control

This project is developed using Git and GitHub, following a clear separation between:

- **local development** (Git Bash on the author’s machine)
- **remote repository** (GitHub web interface)

All experiments are first created and tested locally, then explicitly tracked and published to GitHub through Git commits.

### Key concepts

- **Local**: the working copy of the repository on my computer  
- **Remote**: the version hosted on GitHub  
- **git add**: select which files should be tracked  
- **git commit**: save a snapshot of selected changes with a message  
- **git push**: upload committed changes to GitHub  
- **git pull**: download updates from GitHub before continuing local work  

This workflow ensures full control over what is published and avoids accidental data leakage or inconsistencies.

---

## 2. Dataset selection and handling

### Data source

The project uses real customer reviews from the **Sephora Products and Skincare Reviews** dataset (Kaggle, CC BY 4.0).

Only a small, curated subset is used for evaluation.

### Data separation

To maintain reproducibility and cleanliness:

- `data/raw/` contains raw CSV files (ignored by Git)
- `data/curated/` contains the final curated dataset used for experiments

Raw data is never modified directly.

---

## 3. Curated dataset generation

A Python script (`extract_and_sample.py`) is used to generate a balanced evaluation dataset with the following rules:

- 100 English reviews total  
- 50 positive (rating ≥ 4)  
- 50 negative (rating ≤ 2)  
- rating == 3 excluded  
- deduplication by review text  
- max 3 reviews per product per class (to reduce product dominance)  
- fixed random seed for reproducibility  

The output is:

luxury_reviews_100.csv

yaml
Copy code

This file is versioned and used consistently across all prompt strategies.

---

## 4. Zero-shot baseline evaluation

### Goal

Establish a baseline for sentiment classification without examples.

### Process

- A zero-shot prompt is defined and documented  
- Predictions are generated manually using ChatGPT (web interface)  
- The model only sees `review_text`  
- Ground truth labels are applied **after** inference  

### Logging

Results are recorded in:

results/predictions_zero_shot.csv

yaml
Copy code

Each row logs:

- review ID  
- true label  
- predicted label  
- strategy  
- model  
- qualitative notes  

---

## 5. Initial error analysis (mini-analysis)

Before scaling the experiment, a first batch of 10 reviews is analyzed to validate the setup.

Observed failure modes include:

- implicit dissatisfaction  
- mixed sentiment  
- expectation mismatch  
- over-weighting of positive language  

This analysis is documented in:

notes.md

yaml
Copy code

The goal is not statistical significance, but early signal detection.

---

## 6. Few-shot prompt design

Based on the observed failure modes, two few-shot strategies are designed:

### 6.1 Generic few-shot prompt

Purpose:

- improve performance on nuanced sentiment  
- without explicit domain assumptions  

File:

prompts/few_shot_generic.md

makefile
Copy code

### 6.2 Failure-aware few-shot prompt

Purpose:

- explicitly address known failure modes  
- guide the model toward expectation-aware classification  

File:

prompts/few_shot_failure_aware.md

yaml
Copy code

Both prompts share the same classification task and output constraints, differing only in example design.

---

## 7. Few-shot evaluation

Predictions for each strategy are logged separately:

results/predictions_few_shots_generic.csv
results/predictions_few_shots_failure_aware.csv

yaml
Copy code

This separation enables direct comparison between strategies without ambiguity.

---

## 8. Iterative, controlled experimentation

The project follows an iterative evaluation approach:

1. Small batch testing  
2. Error inspection  
3. Prompt refinement  
4. Controlled expansion  

At no point are prompts changed mid-batch or results overwritten.

This mirrors real-world prompt engineering workflows used in production and consulting environments.

---

## 9. Scope and limitations

- Manual inference is used to prioritize reasoning transparency over automation  
- Statistical testing is out of scope for this iteration  
- The focus is on methodology, not leaderboard performance  

---

## 10. Next steps

Potential future extensions include:

- accuracy and confusion matrix computation  
- cross-model comparison  
- token cost vs performance analysis  
- semi-automated inference via API  
---

This project is intentionally designed to demonstrate **systematic thinking, evaluation rigor, and prompt iteration**, rather than one-off prompt crafting.
