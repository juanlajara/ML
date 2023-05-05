from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from decouple import config
import os

# Load the API keys from the .env file
SERPAPI_API_KEY_VAL = config('SERPAPI_API_KEY')
OPENAI_API_KEY_VAL = config('OPENAI_API_KEY')

# Set the API keys as environment variables
os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY_VAL
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY_VAL


# First, let's load the language model we're going to use to control the agent.
llm = OpenAI(temperature=0)

# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)


# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Now let's test it out!
agent.run("What are the best courses for learning Large Language Model integrations?")
