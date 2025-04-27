# Tavily Web Research Assistant (LangGraph Project)

This project implements an automated Web Research Assistant that combines Tavily API, OpenAI language models, and LangGraph orchestration. It transforms a simple user query into a complete research output by dynamically performing web search, summarization, fact validation, and final answer drafting with proper citations. The system is designed in a modular, scalable architecture where each task is handled by a specialized agent, coordinated through a LangGraph stateful workflow.

## Project Overview

The Web Research Assistant follows a four-stage process for every user query:

Research: It retrieves real-time web search results using Tavily API.

Summarization: It extracts and condenses important points from the search data using OpenAI language models.

Validation: It fact-checks the summarized points for correctness and clarity.

Drafting: It produces a final answer in either short or detailed format, along with references to the original sources.

The workflow is built using LangGraph, where each specialized task is handled by a modular agent connected through a dynamic, stateful graph.

## Features

Automated Web Research: Uses Tavily API to fetch real-time, relevant search results.

Bullet-point Summarization: Condenses raw search data into clear, concise bullet points using OpenAI LLMs.

Fact Validation: Verifies the accuracy and consistency of the summarized information.

Final Answer Drafting: Generates a user-ready final answer, either short or detailed, based on user preference.

Citation Management: Attaches references to original web sources for traceability.

Modular Agent Design: Each task (research, summarize, validate, draft) is handled by a dedicated, isolated agent.

Stateful Workflow: Coordinates agents dynamically using LangGraph’s state management and conditional execution.

Environment Configuration: Securely manages API keys and environment settings via .env.

Basic Testing Suite: Includes simple test scripts to validate key modules independently.

## Tech Stack

Python 3.10+ — Core programming language.

LangChain — Framework for building language model applications (langchain_openai, langgraph).

Tavily Python SDK — For web search integration through Tavily's API.

OpenAI — For summarization, validation, and drafting tasks using GPT models.

python-dotenv — For managing environment variables securely.

## Project Structure

```
project/

├── notebook/
│   └── tavily.ipynb
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
├── .gitignore
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

## How to Run

Execute the main script :

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
