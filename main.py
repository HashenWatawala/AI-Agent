from dotenv import load_dotenv
import os
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful AI research assistant.
            Use available tools (search, wiki, save_text_to_file) to find, summarize, 
            and save information.
            Respond strictly in JSON format as:\n{format_instructions}
            """,
        ),

        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  
    google_api_key=api_key,
    temperature=0.3,
)


tools = [search_tool, wiki_tool, save_tool]


agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


query = input("🔍 What would you like me to research? ")

result = agent_executor.invoke({"query": query})

print("\n🧾 Raw Agent Output:\n", result)
