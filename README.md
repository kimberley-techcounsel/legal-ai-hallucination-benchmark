# Legal AI Hallucination Benchmark

A legal-tech and responsible-AI project exploring how **legal hallucinations can be identified, verified, and evaluated using authoritative legal sources and transparent screening methods**.

## Project Overview

Generative AI can produce legal propositions and citations that sound convincing while being inaccurate, unsupported, outdated, or fabricated.

This project develops an auditable workflow for evaluating those risks.

Rather than treating dataset labels or model outputs as automatically correct, the project applies a core legal-AI principle:

> **Legal claims should be verified against authoritative sources, not judged solely by how plausible they sound.**

The project evaluates legal propositions across areas including **data protection, securities regulation, copyright and AI, electronic transactions, and marketing regulation**.

## Project Workflow

### 01 — Benchmark Audit & Validation

Audits the original legal hallucination dataset before treating its labels as ground truth.

The notebook examines:

* benchmark structure and completeness;
* duplicate and missing records;
* existing hallucination labels;
* benchmark limitations;
* legal-source verification requirements; and
* a taxonomy of legal-AI hallucinations.

The audit identified that the original dataset contained only **2 seed cases**, making independent legal validation and benchmark expansion necessary.

### 02 — Verified Benchmark & Hallucination Screener

Develops an expanded mini-benchmark containing **11 legally reviewed propositions** grounded in authoritative or primary legal sources.

The notebook introduces a transparent baseline hallucination-risk screener and evaluates claims involving:

* GDPR requirements;
* U.S. securities regulation;
* copyright and generative AI;
* CAN-SPAM requirements; and
* electronic signatures and transactions.

Hallucination categories include fabricated or unsupported legal rules, citation mismatch, jurisdictional errors, temporal errors, doctrinal hallucinations, and overclaiming.

### 03 — Model Evaluation & Error Analysis

Evaluates the hallucination-screening approach using:

* accuracy;
* precision;
* recall;
* F1 score;
* confusion matrices;
* threshold sensitivity;
* false-positive analysis; and
* false-negative analysis.

The analysis demonstrates an important limitation of language-only hallucination detection:

**Incorrect legal claims can sound perfectly plausible, while correct legal rules can contain language that appears suspicious to a simple classifier.**

This supports a source-grounded approach to legal AI verification.

## Responsible Legal-AI Architecture

The project proposes the following workflow:

**Legal Claim → Jurisdiction Detection → Authority Retrieval → Citation Validation → Legal Support Analysis → Confidence Assessment → Human Review**

The objective is not to automate legal judgment.

Instead, AI and analytics are used to identify claims requiring verification while authoritative legal sources and human legal reasoning remain central to the final assessment.

## Tools

Python · pandas · Jupyter Notebook · Matplotlib · Legal Data Analysis · Responsible AI Evaluation

## Legal-Tech Focus

This project demonstrates the intersection of:

**Law · Artificial Intelligence · Legal Research · AI Governance · Regulatory Compliance · Responsible AI · Data Analytics**

It also demonstrates how legal expertise can contribute directly to AI system design through **benchmark validation, explainability, source verification, risk classification, and human-in-the-loop review**.

## Key Takeaway

A legal AI system should not merely ask:

> *Does this legal answer sound correct?*

It should ask:

> **What authoritative source supports this claim, does that authority actually say what the model claims, and when should a human lawyer review the result?**

## Disclaimer

This project is an educational and portfolio prototype. Its benchmark is intentionally small and is not intended to provide production-grade performance estimates.

Hallucination flags and model outputs are analytical indicators only and do not constitute legal advice or definitive determinations of legal accuracy.
