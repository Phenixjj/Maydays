from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.llms.ollama import Ollama
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
# from llama_index.llms.openai import OpenAI




load_dotenv()

llm = Ollama(model="mistral")

# response = llm.complete("What is the capital of France?")
# print(response)

airplane_path = os.path.join(os.path.dirname(__file__), 'data', 'Airplane_Crashes_and_Fatalities_Since_1908.csv')
airplane_df = pd.read_csv(airplane_path)

airplane_query_engine = PandasQueryEngine(
    df=airplane_df,
    verbose=True,
    instruction_str=instruction_str
)
airplane_query_engine.update_prompts({"pandas_prompt": new_prompt})
tools = [
    note_engine,
    QueryEngineTool(
        query_engine=airplane_query_engine,
        metadata=ToolMetadata(
            name="airplane_data_tool",
            description="this gives information about the airplane data"
        ),
    ),
]

# llm = OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"), request_timeout=30.0) # Don't work cause they ask me for my credit card XD ... and nope
agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True, context=context)


while (prompt := input("Enter your query (q to quit): ")) != "q":
    response = agent.query(prompt)
    print(response)