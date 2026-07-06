# 📈 AI Investment Research Assistant

An AI-powered Python application that generates a basic investment research report for a publicly listed company using real financial data and a Large Language Model (LLM).


---

## Features

- Search a company using its stock ticker
- Fetch real-time company information
- Retrieve key financial metrics
- Generate an AI-powered investment research report
- Save the generated report as a Markdown (.md) file.

---

## Tech Stack

- Python
- Google Gemini API
- Yahoo Finance (yfinance)
- Python Dotenv (python-dotenv)
- Tavily Search API (tavily-python)

---

## Project Structure

```
AI-Investment-Research-Assistant/
│
├── agents/
│   ├── research_agent.py
│   ├── financial_agent.py
│   ├── news_agent.py
│   └── report_agent.py
├── output/
│   ├── META_research.json
│   ├── META_financial.json
│   └── META_news.json
│
├── results/
│   └── META_report.md
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

## Example

<img width="1693" height="321" alt="Screenshot 2026-07-06 203046" src="https://github.com/user-attachments/assets/ea00ff52-1e72-4944-8edd-2eb34f1748eb" />

Input

```
Enter Stock Ticker (e.g. AAPL): META
```

Output

```
Fetching company profile...
Fetching financial data...
Fetching latest news...
Generating report...

META Report Generated
```

A detailed investment research report is saved inside the `reports/` folder.

---

## Sample Report

The application generates reports containing:

- Company Overview
- Business Description
- Financial Metrics
- Stock Performance
- Latest News
- Market Sentiment
- Opportunities
- Risks
- Investment Recommendation
- Disclaimer

Example output: [META Report](results/META_report.md)

---
