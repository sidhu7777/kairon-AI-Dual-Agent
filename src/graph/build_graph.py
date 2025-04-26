

from langgraph.graph import StateGraph
from agents.research_agent import research_agent
from agents.summarizer_agent import summarizer_agent
from agents.validation_agent import validation_agent
from agents.drafting_agent import drafting_agent

# Defining the LangGraph work flow
graph = StateGraph(input="input_query", output="final_answer")

# Adding the four agents to the workflow
graph.add_node("research", research_agent)
graph.add_node("summarize", summarizer_agent)
graph.add_node("validate", validation_agent)
graph.add_node("draft", drafting_agent)

# Setting up the flow
graph.set_entry_point("research")

graph.add_edge("research", "summarize")
graph.add_edge("summarize", "validate")
graph.add_edge("validate", "draft")

graph.set_finish_point("draft")

# Compile the graph
graph_app = graph.compile()
