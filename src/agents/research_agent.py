# src/agents/research_agent.py

from langchain.agents import tool
from utils.config import tavily_client  #  import ready TavilyClient instance

@tool
def research_agent(input_query: str) -> dict:
    """Use Tavily to get search results for a query."""
    
    try:
        response = tavily_client.search(
            query=input_query,
            max_results=5
        )
    except Exception as e:
        print(f"Search failed: {e}")
        return {"raw_search_results": "", "original_links": []}

    serialized_results = ""
    original_links = []

    results = response.get("results", [])

    for item in results:
        serialized_results += f"Title: {item.get('title')}\nSnippet: {item.get('content')}\nLink: {item.get('url')}\n\n"
        original_links.append(item.get('url'))

    return {"raw_search_results": serialized_results, "original_links": original_links}
