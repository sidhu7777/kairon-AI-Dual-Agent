# src/utils/config.py

import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables
load_dotenv()

# Fetch API keys
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Tavily client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# Optional: Debug print for sanity (remove in production)
print("Loaded TAVILY_API_KEY:", TAVILY_API_KEY[:8] + "*****")
print("Loaded OPENAI_API_KEY:", OPENAI_API_KEY[:8] + "*****")
