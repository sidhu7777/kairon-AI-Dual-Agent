# src/utils/config.py

import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "").strip()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

print("Loaded TAVILY_API_KEY:", repr(TAVILY_API_KEY[:10] + "*****"))
