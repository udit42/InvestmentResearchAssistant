import yfinance as yf


class FinancialAgent:
    """
    Fetches financial metrics and historical stock prices.
    """

    def get_financial_data(self, ticker: str, period: str = "6mo") -> dict:
        """
        Args:
            ticker : Stock ticker (AAPL, MSFT, TSLA)
            period : 1mo,3mo,6mo,1y,2y,5y,max

        Returns:
            dict containing financial metrics and stock history
        """

        try:
            stock = yf.Ticker(ticker.upper())
            info = stock.info

            history = stock.history(period=period)

            if history.empty:
                return {
                    "success": False,
                    "error": "No historical data found."
                }

            financial_metrics = {
                "current_price": info.get("currentPrice"),
                "market_cap": info.get("marketCap"),
                "pe_ratio": info.get("trailingPE"),
                "eps": info.get("trailingEps"),
                "dividend_yield": info.get("dividendYield"),
                "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
                "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
            }

            stock_history = []

            for date, row in history.iterrows():
                stock_history.append({
                    "date": str(date.date()),
                    "open": round(row["Open"], 2),
                    "high": round(row["High"], 2),
                    "low": round(row["Low"], 2),
                    "close": round(row["Close"], 2),
                    "volume": int(row["Volume"])
                })

            return {
                "success": True,
                "ticker": ticker.upper(),
                "financial_metrics": financial_metrics,
                "stock_history": stock_history
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


if __name__ == "__main__":

    agent = FinancialAgent()

    ticker = input("Enter Stock Ticker: ")

    result = agent.get_financial_data(ticker)

    if result["success"]:

        print("\n========== FINANCIAL METRICS ==========\n")

        for key, value in result["financial_metrics"].items():
            print(f"{key:20}: {value}")

        print("\n========== LAST 5 DAYS ==========\n")

        for day in result["stock_history"][-5:]:
            print(day)

    else:
        print(result["error"])