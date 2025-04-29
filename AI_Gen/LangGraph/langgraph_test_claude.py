# This code depends on pip install langchain[anthropic]
# pip install langchain[anthropic]
# Create a .env file in the same directory as your script
# and add:
# ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY"

import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage

# Load environment variables from .env file
load_dotenv()

def search(query: str): #this is considered a potential tool for the model
    """Call to surf the web."""
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."

agent = create_react_agent("anthropic:claude-3-7-sonnet-latest", tools=[search])

result = agent.invoke(
    {"messages": [HumanMessage(content="what is the weather in sf")]}
)

print(result)

# # This code depends on pip install langchain[anthropic]
# #pip install langchain[anthropic]
# #export ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY"


# from langgraph.prebuilt import create_react_agent


# # import os
# # from dotenv import load_dotenv
# # import logging
# # # Load environment variables
# # load_dotenv()


# # # Get API keys and other environment variables
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# def search(query: str):
#     """Call to surf the web."""
#     if "sf" in query.lower() or "san francisco" in query.lower():
#         return "It's 60 degrees and foggy."
#     return "It's 90 degrees and sunny."

# agent = create_react_agent("anthropic:claude-3-7-sonnet-latest", tools=[search])
# agent.invoke(
#     {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
# )