# DES Cipher + BERT Sentiment Analysis

> **Dual-domain project combining a from-scratch DES Feistel cipher implementation with a BERT fine-tuning pipeline for sentiment classification.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)](https://pytorch.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/)

---

## Overview

This repository contains two independent, production-quality implementations:

1. **DES Feistel Cipher** — complete from-scratch implementation of the Data Encryption Standard
2. **BERT Sentiment Analysis** — fine-tuned BERT transformer for binary sentiment classification

Both serve as reference implementations for classical cryptography and modern NLP respectively.

---

## Part 1: DES Implementation

### Algorithm Overview
DES (Data Encryption Standard) is a symmetric-key block cipher that encrypts 64-bit blocks using a 56-bit key through 16 Feistel rounds.

### Implemented Components

```
Plaintext (64 bits)
        │
  Initial Permutation (IP)
        │
  ┌───────────────┐
  │ 16 Feistel Rounds  │
  │                   │
  │ Round i:           │
  │  R_i = L_{i-1} ⊕ F(R_{i-1}, K_i)
  │  L_i = R_{i-1}    │
  └───────────────┘
        │
  Inverse Permutation (IP⁻¹)
        │
  Ciphertext (64 bits)
```

| Component | Implementation Detail |
|---|---|
| **Initial Permutation** | Full IP and IP⁻¹ tables |
| **Key Schedule** | PC-1 (64→56 bits) + PC-2 (56→48 bits) permutations, 16 round keys |
| **Feistel F-function** | Expansion (32→48), XOR with round key, 8 S-boxes (6→4 bits each), P-permutation |
| **S-Boxes** | All 8 NIST-standard S-box substitution tables |
| **Block Modes** | ECB (Electronic Codebook) + CBC (Cipher Block Chaining) |

### Usage

```python
from des import DES

# Initialize with 8-character (64-bit) key
des = DES(key="secretke")

# ECB mode
ciphertext = des.encrypt("HelloWorld12345!")
plaintext = des.decrypt(ciphertext)

# CBC mode
ciphertext_cbc = des.encrypt_cbc("HelloWorld12345!", iv="initvect")
```

---

## Part 2: BERT Sentiment Analysis

### Model Configuration
```python
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
optimizer = AdamW(lr=2e-5, weight_decay=0.01)
max_len = 512       # Full context window
batch_size = 16
epochs = 3
```

### Training Pipeline
- **Tokenization**: `BertTokenizer` with `[CLS]`/`[SEP]` tokens and attention masks
- **Fine-tuning**: Last layer + classification head on binary sentiment task
- **Evaluation**: Accuracy, F1, confusion matrix

---

## Installation

```bash
git clone https://github.com/tamer017/DES.git
cd DES
pip install torch transformers numpy pandas scikit-learn
```

---

## Skills & Concepts

`Cryptography` `DES` `Feistel Networks` `S-Boxes` `ECB/CBC Modes` `BERT` `Transfer Learning` `Fine-Tuning` `PyTorch` `HuggingFace Transformers` `NLP` `Sentiment Analysis`

---

## Author

**Ahmed Tamer Assy** — [GitHub](https://github.com/tamer017) | Machine Learning Researcher @ Volkswagen AG
