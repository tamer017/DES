# Sentiment Analysis with BERT on the SST Dataset

> **BERT fine-tuning pipeline for sentiment classification on the Stanford Sentiment Treebank (SST-5) — 6 experiments comparing regularization, loss functions, and architectural modifications.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)](https://pytorch.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/)

---

## Overview

This project focuses on sentiment analysis using the **BERT model** on the Stanford Sentiment Treebank (SST) dataset. Sentiment analysis is a fundamental NLP task involving determining the sentiment expressed in text. The SST dataset provides labeled sentences with sentiment scores across 5 classes.

The primary objective is to **enhance BERT-based sentiment classification beyond the 52.2% baseline** by exploring regularization methods, loss functions, and architectural modifications.

---

## Key Takeaways

- **BERT Fine-Tuned**: High accuracy on IMDB (93.8%) but maintained baseline on SST and Tweets.
- **Multi-Task Fine-Tuning (SMART + Mnrl)**: Improved STS (Pearson 0.812) but did not enhance SST accuracy.
- **Residual MLP (RIMLP)**: Performance on par with baseline.
- **L2 Regularization**: Best improvement in SST accuracy (52.9%).
- **Autoencoder Backbone**: Significant drop in performance (18.3%).
- **Focal Loss**: Best loss function — 53% accuracy on SST.

---

## Experiments Summary

| **Experiment** | **Best Model/Technique** | **Dataset/Task** | **Metric** | **Result** |
|---|---|---|---|---|
| Exp 1 | BERT Fine-Tuned | IMDB/SST | Accuracy | 93.8%/52.6% |
| Exp 1 | BERT Fine-Tuned | Tweets/SST | Accuracy | 61.6%/52.6% |
| Exp 2 | Multi-Task (SMART + Mnrl) | SST | Accuracy | 51% |
| Exp 2 | Multi-Task (SMART + Mnrl) | STS | Pearson's r | 0.812 |
| Exp 3 | Residual MLP (RIMLP) | SST | Accuracy | 52.2% |
| Exp 4 | L2 Regularization (λ=0.05) | SST | Accuracy | 52.9% |
| Exp 5 | Autoencoder Backbone | SST | Accuracy | 18.3% |
| Exp 6 | Focal Loss | SST | Accuracy | **53%** |

---

## Experiment 6: Loss Functions (Best Result)

In **Experiment 6**, Focal Loss achieved **53% accuracy** over 10 epochs.

![Training and Validation Accuracy](https://github.com/user-attachments/assets/49227cf1-eb2f-49cc-8c18-3d177d130ea2)

### Comparison with State-of-the-Art

![State-of-the-Art Models](https://github.com/user-attachments/assets/8a2b2056-a47f-4780-8c81-1047e90adbb2)

| **Loss Function** | **Accuracy** |
|---|---|
| CrossEntropyLoss (Baseline) | 52.2% |
| Mean Squared Error (MSE) | 52.6% |
| Hinge Loss | 52.4% |
| Dice Loss | 46.6% |
| **Focal Loss** | **53%** |

---

## Experiment 4: Regularization Techniques

| **Technique** | **Accuracy** |
|---|---|
| Dropout (rate: 0.4) | 52.7% |
| **L2 Regularization (λ=0.05)** | **52.9%** |
| Batch Normalization | 52% |
| L1 Regularization (λ=1e-5) | 52.1% |
| Gradient Clipping (value: 1) | 52.1% |
| Label Smoothing (factor: 0.1) | 52.3% |

---

## Experiment 5: Autoencoder Backbone

#### Auto Encoder Training
![autoencoder_diagram](https://github.com/user-attachments/assets/afa860bc-bc2f-4eb5-b2cc-dc72a896ca74)

#### Sentiment Training
![classifier_diagram](https://github.com/user-attachments/assets/4a3b3f13-893a-4f91-a232-29d1fae58d53)

| **Training Dataset** | **Metric** | **Result** |
|---|---|---|
| Quora Paraphrase | Reconstruction Loss | 0.00001 |
| SST | Accuracy | 18.3% |

---

## How to Run the Best Model

Edit `run_train.py`:

```bash
python -u multitask_classifier.py --use_gpu --epochs 10 --local_files_only --option finetune --task sst --hidden_dropout_prob 0.1 --lr 1e-5 --batch_size 64
```

Run:
```bash
./run_train.py
```

---

## Experiment Branches

| Branch | Experiment |
|---|---|
| [sentiment-imdb-binary](https://github.com/thisHermit/nlp_project/tree/sentiment-imdb-binary) | Exp 1 — IMDB fine-tuning |
| [sentiment-tweets](https://github.com/thisHermit/nlp_project/tree/sentiment-tweets) | Exp 1 — Tweets fine-tuning |
| [sentiment-semantic](https://github.com/thisHermit/nlp_project/tree/sentiment-semantic) | Exp 2 — Multi-task SMART+Mnrl |
| [sentiment-architectures](https://github.com/thisHermit/nlp_project/tree/sentiment-architectures) | Exp 3 — RIMLP + bLSTM |
| [sentiment-regularization](https://github.com/thisHermit/nlp_project/tree/sentiment-regularization) | Exp 4 — Regularization |
| [sentiment-autoencoder](https://github.com/thisHermit/nlp_project/tree/sentiment-autoencoder) | Exp 5 — Autoencoder backbone |
| [sentiment-loss-function](https://github.com/thisHermit/nlp_project/tree/sentiment-loss-function) | Exp 6 — Loss functions |

---

## Skills & Concepts

`BERT` `Sentiment Analysis` `Transfer Learning` `Fine-Tuning` `Focal Loss` `L2 Regularization` `Multi-Task Learning` `Autoencoder` `PyTorch` `HuggingFace Transformers` `NLP` `SST-5`

---

## Author

**Ahmed Tamer Assy** — [GitHub](https://github.com/tamer017) | Machine Learning Researcher @ Volkswagen AG
