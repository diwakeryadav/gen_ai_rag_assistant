from fastapi import FastAPI

app = FastAPI(title="GenAI RAG Assistant")

@app.get("/")
def home():
    return {"message":"GenAI RAG Assistant is running"}