# tests/test_summarizer_agent.py

import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agents.summarizer_agent import summarizer_agent

def main():
    # Load the saved research output
    with open("tests/research_output.json", "r", encoding="utf-8") as f:
        research_output = json.load(f)

    raw_search_results = research_output["raw_search_results"]
    original_links = research_output["original_links"]

    summarizer_output = summarizer_agent.invoke({
        "raw_search_results": raw_search_results,
        "original_links": original_links
    })

    # Print summarizer result
    print("=== Summarizer Output ===")
    print(summarizer_output)

    with open("tests/summarizer_output.json", "w", encoding="utf-8") as f:
        json.dump(summarizer_output, f, indent=4)



   

if __name__ == "__main__":
    main()
    