# DES Cipher Implementation + BERT Sentiment Analysis Pipeline

> A dual-purpose cryptography and NLP project implementing the full **Data Encryption Standard (DES)** cipher with CBC/ECB modes, alongside a **BERT-based sentiment analysis** pipeline.

[![Language](https://img.shields.io/badge/Language-Python%203.x-green?style=flat-square)](https://www.python.org/)
[![Crypto](https://img.shields.io/badge/Cryptography-DES%20%2B%20CBC%2FECB-red?style=flat-square)]()
[![NLP](https://img.shields.io/badge/NLP-BERT%20Sentiment-blue?style=flat-square)](https://huggingface.co/)

---

## Overview

This project combines two distinct but complementary domains: **classical symmetric cryptography** and **modern NLP**.

1. **DES Cipher:** A complete Python implementation of the Data Encryption Standard (DES), including both Electronic Codebook (ECB) and Cipher Block Chaining (CBC) modes of operation, built from first principles without relying on cryptographic libraries.

2. **BERT Sentiment Pipeline:** A transfer-learning-based sentiment analysis system using a pre-trained BERT model fine-tuned for binary/multi-class sentiment classification on text data.

---

## Part 1 — DES Cipher

### Algorithm Overview

```
[64-bit Plaintext Block]
        |
        v
  [Initial Permutation (IP)]
        |
        v
  [16 Feistel Rounds]
  Each round:
    ├─ Expand R (32→48 bits via E-permutation)
    ├─ XOR with 48-bit Round Key
    ├─ S-Box substitution (48→32 bits)
    ├─ P-Box permutation
    └─ XOR with L, swap L↔R
        |
        v
  [Final Permutation (IP⁻¹)]
        |
        v
[64-bit Ciphertext Block]
```

### Key Schedule
- 64-bit key → **PC-1 permutation** drops parity bits → 56-bit effective key
- Split into two 28-bit halves (C, D)
- Each round: left circular shift by 1 or 2 positions (schedule-dependent)
- **PC-2 permutation** selects 48 bits per round → 16 subkeys

### Modes of Operation

| Mode | Description | Use Case |
|---|---|---|
| **ECB** (Electronic Codebook) | Each block encrypted independently | Simple, parallelizable (insecure for patterns) |
| **CBC** (Cipher Block Chaining) | Each block XORed with previous ciphertext before encryption | Secure for structured data, requires IV |

### S-Box Substitution
The 8 DES S-Boxes are the core non-linear component providing confusion. Each 6-bit input maps to a 4-bit output via the FIPS-46-3 lookup tables, implemented as hardcoded 2D arrays in Python.

---

## Part 2 — BERT Sentiment Analysis

### Pipeline Architecture

```
[Raw Text Input]
        |
        v
  [BERT Tokenizer]
  WordPiece tokenization, [CLS]/[SEP] tokens
  Truncation to 512 tokens
        |
        v
  [Pre-trained BERT Encoder]
  bert-base-uncased / bert-base-multilingual
        |
        v
  [CLS Token Representation (768-dim)]
        |
        v
  [Classification Head]
  Linear(768 → num_classes) + Softmax
        |
        v
  [Sentiment Label + Confidence Score]
```

### Training Configuration
| Parameter | Value |
|---|---|
| Base model | `bert-base-uncased` |
| Optimizer | AdamW |
| Learning rate | 2e-5 (with warm-up) |
| Batch size | 16 |
| Max sequence length | 512 tokens |
| Framework | HuggingFace Transformers + PyTorch |

---

## Project Structure

```
DES/
├── des/
│   ├── des.py              # Core DES cipher (IP, Feistel, S-boxes, key schedule)
│   ├── modes.py            # ECB and CBC mode implementations
│   └── utils.py            # Bit manipulation helpers
├── bert/
│   ├── sentiment.ipynb     # BERT fine-tuning and inference notebook
│   └── preprocess.py       # Text cleaning and tokenization pipeline
└── README.md
```

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/tamer017/DES.git
cd DES

# Install dependencies
pip install torch transformers pandas numpy scikit-learn

# Run DES cipher
python des/des.py

# Run BERT sentiment notebook
jupyter notebook bert/sentiment.ipynb
```

---

## Skills Demonstrated

- **Cryptography:** DES algorithm, Feistel network, S-box design, key schedule, CBC/ECB modes
- **NLP:** BERT, HuggingFace Transformers, fine-tuning, transfer learning, tokenization
- **Python:** Bit manipulation, lookup tables, PyTorch model training
- **Security:** Block cipher modes, padding schemes, IV management

---

## ⚠️ Security Notice

> DES is **cryptographically broken** and deprecated (56-bit key is brute-forceable). This implementation is for **educational purposes only**. Use AES-256-GCM for any production cryptographic needs.

---

## References

- [FIPS 46-3 — DES Standard](https://csrc.nist.gov/publications/detail/fips/46/3/archive/1999-10-25)
- [BERT: Pre-training of Deep Bidirectional Transformers — Devlin et al., 2019](https://arxiv.org/abs/1810.04805)
- [HuggingFace Transformers Documentation](https://huggingface.co/docs/transformers)
