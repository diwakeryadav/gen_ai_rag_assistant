from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI(title="GenAI RAG Assistant")

@app.get("/")
def home():
    return {"message":"GenAI RAG Assistant is running"}

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print(api_key)