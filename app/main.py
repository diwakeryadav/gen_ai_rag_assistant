from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.routes.rag import router as rag_router

load_dotenv()

app = FastAPI(title="GenAI RAG Assistant")

@app.get("/")
def home():
    return {"message": "GENAI RAG Assistant is running"}

app.include_router(rag_router)