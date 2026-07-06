import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


class NewsAgent:
    """
    Fetches the latest news about a company using Tavily.
    """

    def __init__(self):
        self.client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

    def get_news(self, company_name, ticker, max_results=5):
        """
        Returns the latest news articles.
        """

        try:
            response = self.client.search(
                query=f"{company_name} ({ticker}) latest stock news",
                topic="news",
                max_results=max_results,
                search_depth="advanced",
                include_answer=True
                
            )

            articles = []

            for item in response.get("results", []):
                articles.append({
                    "title": item.get("title"),
                    "url": item.get("url")
                })

            return {
                "success": True,
                "summary": response.get("answer", "Not Found"),
                "articles": articles
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


