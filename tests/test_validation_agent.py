# tests/test_validation_agent.py

import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agents.validation_agent import validation_agent

def main():
    # Load summarizer output
    with open("tests/summarizer_output.json", "r", encoding="utf-8") as f:
        summarizer_output = json.load(f)

    summary_text = summarizer_output["summary_text"]

    validation_output = validation_agent.invoke({
        "summary_text": summary_text
    })

    # Print validation result
    print("=== Validation Output ===")
    print(validation_output)

    # Optional assert
    assert "validation_notes" in validation_output

if __name__ == "__main__":
    main()
