# tests/test_research_agent.py

import sys
import os

# Add src/ to sys.path so that agents can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agents.research_agent import research_agent

def main():
    query = "What is LangChain?"
    result = research_agent.invoke({"input_query": query})
    
    # Show the result
    print("=== Test Output ===")
    print(result)
    
    

if __name__ == "__main__":
    main()
