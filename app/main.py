from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.routes.rag import router as rag_router
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(title="GenAI RAG Assistant")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(rag_router)

@app.get("/")
def home():
    return {"message": "GENAI RAG Assistant is running"}