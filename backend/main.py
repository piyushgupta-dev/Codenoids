import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv

from agent import ask_agent

# Load Environment Variables
load_dotenv()

# FastAPI App
app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Model
class ChatRequest(BaseModel):
    message: str


# Root Route
@app.get("/")
async def root():
    return {
        "message": "FastAPI + LangChain + Gemini Running Successfully"
    }


# Test Route
@app.get("/test")
async def test():
    return {
        "message": "Backend Working Successfully"
    }


# Chat Endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = ask_agent(
            request.message
        )

        return {
            "response": response
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "response": f"Error: {str(e)}"
        }