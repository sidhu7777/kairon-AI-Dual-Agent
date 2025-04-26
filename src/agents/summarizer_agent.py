# src/agents/summarizer_agent.py

from langchain.agents import tool
from langchain_openai import ChatOpenAI

from typing import Dict, List

@tool
def summarizer_agent(raw_search_results: str, original_links: List[str]) -> Dict[str, str | List[str]]:
    """
    Summarizes the raw search results into bullet points using an LLM.

    Args:
        raw_search_results (str): The raw text of search results.
        original_links (List[str]): List of original URLs from search.

    Returns:
        dict: A dictionary containing the summary and the original links.
    """
    summarizer_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    prompt: str = f"""
    You are a research assistant. Summarize the following search results into clean bullet points.
    Focus only on important facts. Ignore unnecessary details.

    Search Results:
    {raw_search_results}
    """

    response = summarizer_llm.invoke(prompt)
    
    return {
        "summary_text": response.content,
        "original_links": original_links
    }
