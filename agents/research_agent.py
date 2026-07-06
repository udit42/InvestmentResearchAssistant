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


