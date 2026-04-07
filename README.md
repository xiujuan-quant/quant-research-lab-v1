# quant-research-lab-v1

A beginner-friendly quantitative research project for stock factor research using Python.

## Project Overview

This project is designed to build a basic quantitative research workflow around stock factor generation.  
It covers the complete pipeline from raw stock data acquisition to data cleaning and technical factor calculation.

Current implemented factors include:

- MA (Moving Average)
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)

The project focuses on:

- Modular Python engineering structure
- Config-based parameter management
- Reproducible factor research workflow
- Beginner-friendly quantitative research practice

---

## Project Structure

```bash
quant-research-lab-v1/
├── config/
│   └── config.yaml              # Project configuration file
├── data/
│   ├── raw/                     # Raw stock data
│   ├── processed/               # Cleaned stock data
│   └── factors/                 # Factor-enriched stock data
├── notebooks/                   # Research notebooks (optional)
├── reports/                     # Output reports / notes
├── src/
│   ├── __init__.py
│   ├── data.py                  # Config loading & data processing functions
│   ├── factors.py               # MA / RSI / MACD factor calculation functions
│   └── run_factors.py           # Main program entry for factor generation
├── .gitignore
├── README.md
└── requirements.txt