import json
from agents.research_agent import ResearchAgent
from agents.financial_agent import FinancialAgent
from agents.news_agent import NewsAgent
from agents.report_agent import ReportAgent


def main():

    # Initialize agents
    research_agent = ResearchAgent()
    financial_agent = FinancialAgent()
    news_agent = NewsAgent()
    report_agent = ReportAgent()

    # Get user input
    ticker = input("Enter Stock Ticker (e.g. AAPL): ").upper()

    print("\nFetching company profile...")
    research_data = research_agent.get_company_profile(ticker)
   
    with open(f"outputs/{ticker}_research.json", "w", encoding="utf-8") as f:
        json.dump(research_data, f, indent=4)

    if not research_data["success"]:
        print(research_data["error"])
        return

    print("Fetching financial data...")
    financial_data = financial_agent.get_financial_data(ticker)
    
    with open(f"outputs/{ticker}_financial.json", "w", encoding="utf-8") as f:
        json.dump(financial_data, f, indent=4)
    
    if not financial_data["success"]:
        print(financial_data["error"])
        return

    print("Fetching latest news...")

    news_data = news_agent.get_news(
        research_data["company_name"],
        ticker
    )

    with open(f"outputs/{ticker}_news.json", "w", encoding="utf-8") as f:
        json.dump(news_data, f, indent=4)

    if not news_data["success"]:
        print(news_data["error"])
        return

    print("Generating report...\n")

    report = report_agent.generate_report(
        research_data,
        financial_data,
        news_data
    )

    with open(f"results/{ticker}_report.md", "w", encoding="utf-8") as f:
        f.write(report)
        print(f"{ticker} Report Generated")


if __name__ == "__main__":
    main()