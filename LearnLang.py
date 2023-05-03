""" from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

import os
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("technology coaching services"))

 """

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from decouple import config
import os

SERPAPI_API_KEY_VAL = config('SERPAPI_API_KEY_VAL')
OPENAI_API_KEY_VAL = config('OPENAI_API_KEY_VAL')


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
