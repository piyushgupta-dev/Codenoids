from langchain_ollama import ChatOllama

from router import route_query

from tools import *

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.7
)

def ask_agent(question: str):

    route = route_query(question)

    print(f"ROUTE SELECTED: {route}")

    if route == "calculator":
        return calculator(question)

    elif route == "weather":
        return weather_tool(question)

    elif route == "github":
        return github_tool(question)

    elif route == "railway":
        return railway_tool(question)

    elif route == "parking":
        return parking_tool(question)

    elif route == "traffic":
        return traffic_tool(question)

    elif route == "hospital":
        return hospital_tool(question)

    elif route == "police":
        return police_tool(question)

    elif route == "news":
        return news_tool(question)

    elif route == "fuel":
        return fuel_tool(question)

    elif route == "ev":
        return ev_station_tool(question)

    elif route == "resume":
        return resume_tool(question)

    elif route == "portfolio":
        return portfolio_tool(question)

    elif route == "research":
        return research_tool(question)

    elif route == "pdf":
        return pdf_tool(question)

    elif route == "image":
        return image_tool(question)

    elif route == "sensor":
        return sensor_tool(question)

    elif route == "code":
        return code_tool(question)

    response = llm.invoke(question)

    return response.content