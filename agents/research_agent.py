# agents/research_agent.py

import yfinance as yf


class ResearchAgent:
    """
    Fetches basic company information.

    Returns:
    - Company Name
    - Business Description
    - Industry
    - Sector
    - Ticker
    """

    def get_company_profile(self, ticker: str) -> dict:
        """
        Fetch company information from Yahoo Finance.

        Args:
            ticker (str): Stock ticker (e.g., AAPL, MSFT, TSLA)

        Returns:
            dict: Company profile information
        """

        try:
            stock = yf.Ticker(ticker.upper())
            info = stock.info

            if not info or "longName" not in info:
                return {
                    "success": False,
                    "error": f"No company found for ticker '{ticker}'."
                }

            profile = {
                "success": True,
                "ticker": ticker.upper(),
                "company_name": info.get("longName", "N/A"),
                "business_description": info.get("longBusinessSummary", "N/A"),
                "industry": info.get("industry", "N/A"),
                "sector": info.get("sector", "N/A")
            }

            return profile

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


if __name__ == "__main__":
    agent = ResearchAgent()

    company = input("Enter Stock Ticker: ")

    result = agent.get_company_profile(company)

    if result["success"]:
        print("\n========== COMPANY PROFILE ==========")
        print(f"Ticker      : {result['ticker']}")
        print(f"Company     : {result['company_name']}")
        print(f"Sector      : {result['sector']}")
        print(f"Industry    : {result['industry']}")
        print(f"\nBusiness Description:\n")
        print(result["business_description"])
    else:
        print(result["error"])