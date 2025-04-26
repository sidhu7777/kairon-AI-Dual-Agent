# Tavily Web Research Assistant (LangGraph Project)

This project is a modular Web Research Assistant built using Tavily API, OpenAI models, LangGraph orchestration, and Python. It performs a complete automated research pipeline including Web Search, Summarization, Fact Validation, and Final Answer Drafting with citations.

## Project Overview

Given a user's query (e.g., "What is LangChain?"), the system:

- Performs web search using Tavily API
- Summarizes important facts using an OpenAI LLM
- Validates the facts for hallucinations or misinformation
- Drafts a clean, final answer in either short or detailed form, including citations

The system uses a LangGraph to structure the workflow as interconnected nodes (agents). Each agent focuses on a specialized subtask.

## Features

- Automated Web Research using Tavily
- Bullet-point Summarization using OpenAI GPT models
- Fact-checking Validation step
- Final Answer Drafting with Short/Detailed control
- Citations for sources used
- Modular Python structure
- Environment-safe configuration handling
- LangGraph based dynamic workflow
- Tests included for easier debugging

## Tech Stack

- Python 3.10+
- LangChain (langchain_openai, langgraph)
- Tavily Python SDK
- OpenAI
- Pydantic
- python-dotenv

## Project Structure

```
project/
│
├── src/
│   ├── agents/
│   │   ├── research_agent.py
│   │   ├── summarizer_agent.py
│   │   ├── validation_agent.py
│   │   ├── drafting_agent.py
│   ├── graph/
│   │   └── build_graph.py
│   ├── utils/
│   │   └── config.py
│
├── tests/
│   ├── test_research_agent.py
│
├── .env
├── requirements.txt
├── README.md
└── run.py
```

- `src/agents/`: Houses independent agent modules.
- `src/graph/`: Defines LangGraph setup connecting the agents.
- `src/utils/`: Handles environment variables and Tavily/OpenAI clients.
- `tests/`: Basic agent tests.
- `.env`: Stores API keys securely.
- `run.py`: Entry point for user interaction.

## Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/sidhu7777/kairon-AI-Dual-Agent.git
cd tavily-web-research-assistant
```

2. Create and activate a virtual environment:

```bash
python -m venv tavily
source tavily/bin/activate         # Linux/Mac
tavily\Scripts\activate.bat        # Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```
TAVILY_API_KEY=your-tavily-production-api-key
OPENAI_API_KEY=your-openai-api-key
```

Note: Use a production key in Tavily (not a development key). In Tavily dashboard, while creating an API key, select:

- Key Name: Any unique name like "langgraph-project-key"
- Key Type: Production
- Limit: Leave empty or set a limit if needed

## How to Run

Execute the main script:

```bash
python src/run.py
```

The program will prompt you:

- Enter your research query
- Choose between a short or detailed answer

It will output a fully drafted answer with validated facts and listed sources.

## How to Test

Basic test scripts are available inside the `tests/` folder.

To run Research Agent test:

```bash
python tests/test_research_agent.py
```

This will check whether the Tavily client is properly fetching search results.

## Requirements

Example `requirements.txt`:

```
python-dotenv
langchain
langgraph
langchain-openai
tavily-python
openai
pydantic
```

Install all dependencies via `pip install -r requirements.txt`.

## Future Improvements

- Migrate to LangGraph's Pydantic GraphState model for better validation.
- Add error handling and retry mechanisms for network/API failures.
- Cache search results to reduce redundant Tavily calls.
- Add user interface via Streamlit or Flask.
- Implement LLM output guardrails for safer generation.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Tavily API
- LangChain and LangGraph
- OpenAI

---
