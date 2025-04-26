# src/agents/drafting_agent.py

from langchain.agents import tool
from langchain_openai import ChatOpenAI

from typing import List, Optional

@tool
def drafting_agent(validated_text: str, original_links: List[str], answer_type: Optional[str] = "detailed") -> str:
    """
    Drafts the final answer (short or detailed) based on user preference, then appends citations.
    """

    drafting_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    citations = "\n".join([f"[{i+1}] {link}" for i, link in enumerate(original_links)])

    if answer_type == "short":
        prompt = f"""
        You are an expert research assistant.
        Write a short, concise 1-2 sentence answer based on the following validated content.
        Then list the sources at the end.

        You MUST only use the provided validated content to draft the answer. 

        Validated Content:
        {validated_text}

        Sources:
        {citations}
        """
    else:
        prompt = f"""
        You are an expert research answer writer.
        Write a final detailed answer based on the following validated content.
        Then list the sources at the end.
        You MUST only use the provided validated content to draft the answer. 

        Validated Content:
        {validated_text}

        Sources:
        {citations}
        """

    response = drafting_llm.invoke(prompt)
    return response.content
