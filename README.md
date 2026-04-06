# quant-research-lab-v1

A beginner-friendly quantitative research project for building a reproducible and extensible stock factor research pipeline.

## Overview

This project is designed to simulate a basic quantitative research workflow, including:

- historical stock data fetching
- raw data cleaning and preprocessing
- technical factor generation
- factor result storage and management

The current research target is **CATL (300750)**.

---

## Project Structure

```bash id="c8k5f2"
quant-research-lab-v1/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── factors/
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── factors.py
│   └── run_factors.py
│
├── notebooks/
│
├── README.md
├── requirements.txt
└── .gitignore