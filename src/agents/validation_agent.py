# src/agents/validation_agent.py

from langchain.agents import tool
from langchain_openai import ChatOpenAI

from typing import Dict,List

@tool
def validation_agent(summary_text: str, original_links: List[str]) -> dict:
    """Validates summarized points for correctness."""

    validator_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    prompt = f"""
    You are a fact-checker. Carefully review the following bullet points for accuracy and clarity.
    Correct any mistakes or misleading information.

   {summary_text}
    """

    response = validator_llm.invoke(prompt)
    return {"validated_text": response.content, "original_links": original_links}
