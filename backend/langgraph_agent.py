import os

from dotenv import load_dotenv

from typing import TypedDict

from langgraph.graph import StateGraph, END

from langchain_google_genai import ChatGoogleGenerativeAI

from tools import calculator

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

class AgentState(TypedDict):
    message: str
    response: str


def router_node(state):

    message = state["message"]

    if any(op in message for op in ["+", "-", "*", "/"]):

        return {
            "response": calculator(message)
        }

    response = llm.invoke(message)

    return {
        "response": response.content
    }


graph = StateGraph(AgentState)

graph.add_node(
    "router",
    router_node
)

graph.set_entry_point(
    "router"
)

graph.add_edge(
    "router",
    END
)

agent = graph.compile()


def ask_graph(question):

    result = agent.invoke(
        {
            "message": question
        }
    )

    return result["response"]