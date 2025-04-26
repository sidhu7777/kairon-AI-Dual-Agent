# tests/test_drafting_agent.py

import sys
import os
import json

# Add src/ to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agents.drafting_agent import drafting_agent

def main():
    # Load the summarizer output (because validated_text will come from there for now)
    with open("tests/summarizer_output.json", "r", encoding="utf-8") as f:
        summarizer_output = json.load(f)

    summary_text = summarizer_output["summary_text"]
    original_links = summarizer_output["original_links"]

    # Call drafting_agent (default detailed answer)
    drafted_content = drafting_agent.invoke({
        "validated_text": summary_text,
        "original_links": original_links,
        "answer_type": "short"   # You can also try "detailed"
    })

    # Print drafted article
    print("=== Drafted Content ===")
    print(drafted_content)

    
if __name__ == "__main__":
    main()
