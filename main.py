import os
from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

class ResearchReasponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object = ResearchReasponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that helps generate research summaries.
            Use necessary tools (like search or wiki if provided).
            Output only in this JSON format:\n{format_instructions}
            """,
        ),
        ("human", "{query}"),
    ]
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # or gemini-1.5-pro
    google_api_key=api_key,
    temperature=0.3
)

formatted_prompt = prompt.format_prompt(
    query="Explain the impact of quantum computing on cybersecurity.",
    format_instructions=parser.get_format_instructions(),
)

response = llm.invoke(formatted_prompt.to_messages())



genai.configure(api_key=api_key)

parsed = parser.parse(response.content)

print(parsed)