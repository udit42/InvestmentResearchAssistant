import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class ReportAgent:
    """
    Uses Gemini to generate a readable investment research report.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

    def generate_report(self, research_data, financial_data, news_data):
        """
        Generate a report using the collected information.
        """

        prompt = f"""
You are a professional investment research analyst.

Analyze the following information and generate a well-structured investment research report.

Research Data:
{research_data}

Financial Data:
{financial_data}

Latest News:
{news_data}

Generate the report in the following format:

# Investment Research Report

## 1. Company Overview
Include:
- Company Name
- Stock Ticker
- Sector
- Industry

## 2. Business Description
Summarize the company's business in 2-3 paragraphs.

## 3. Financial Metrics
Present the following in a markdown table:

| Metric | Value |
|--------|-------|
| Current Price | |
| Market Cap | |
| P/E Ratio | |
| EPS | |
| Dividend Yield | |
| 52 Week High | |
| 52 Week Low | |

## 4. Stock Performance
Summarize the historical stock price trend in a short paragraph.

## 5. Latest News
Summarize the important recent news in 3-5 bullet points.

## 6. Market Sentiment
Based on the recent news, classify the overall sentiment as:
- Positive
- Neutral
- Negative

Explain your reasoning in 2-3 sentences.

## 7. Key Opportunities
List 3-5 potential growth opportunities.

## 8. Key Risks
List 3-5 major risks or concerns.

## 9. Investment Recommendation
Recommend one of:
- Buy
- Hold
- Sell

Provide a balanced explanation based on the company profile, financial metrics, and recent news.

## 10. Disclaimer
State that this report is generated using publicly available information and is for educational purposes only. It should not be considered financial advice.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text


if __name__ == "__main__":

    # Example only
    research = {
        "company_name": "Apple Inc.",
        "ticker": "AAPL",
        "sector": "Technology",
        "industry": "Consumer Electronics",
        "business_description": "Apple designs and sells consumer electronics..."
    }

    financial = {
        "current_price": 212.45,
        "market_cap": "3.1T",
        "pe_ratio": 31.4,
        "eps": 6.8,
        "dividend_yield": "0.43%",
        "fifty_two_week_high": 260,
        "fifty_two_week_low": 169
    }

    agent = ReportAgent()

    report = agent.generate_report(research, financial)

    print(report)