# GenAI RAG Assistant

A production-style Retrieval-Augmented Generation (RAG) backend built with FastAPI, ChromaDB, LangChain, local Hugging Face embeddings, and Ollama for local LLM inference.

This project is designed to demonstrate an end-to-end GenAI system: document ingestion, chunking, embedding generation, vector search, grounded answer generation, and API delivery.

## Why this project exists

Most GenAI demos stop at a notebook or a simple script. This project goes further by turning RAG into a structured backend service with clean architecture, local inference, and a clear path toward deployment.

## What it does

* Ingests PDF documents
* Splits documents into chunks
* Generates embeddings locally using Hugging Face
* Stores vectors in ChromaDB
* Retrieves relevant chunks for a user query
* Uses a local Ollama model to generate grounded answers
* Exposes the system through a FastAPI backend

## Current architecture

```text
PDFs in /data
   ↓
Document Loader
   ↓
Text Splitter
   ↓
Embedding Model
   ↓
Chroma Vector DB
   ↓
Retriever
   ↓
Local LLM (Ollama)
   ↓
FastAPI API
```

## Tech stack

### Backend

* FastAPI
* Uvicorn
* Pydantic

### RAG / AI

* LangChain
* ChromaDB
* Hugging Face sentence-transformers
* Ollama
* Local LLM inference

### DevOps / tooling

* Docker
* Docker Compose
* Git
* .env-based configuration

## Features completed so far

* PDF loading
* Text chunking
* Embedding generation
* Vector database persistence
* Semantic retrieval
* Local LLM response generation
* FastAPI health endpoint
* FastAPI RAG endpoint

## API endpoints

### `GET /`

Health check endpoint.

Response:

```json
{
  "message": "GENAI RAG Assistant is running"
}
```

### `POST /query`

Ask a question against the indexed document set.

Request:

```json
{
  "question": "What is this document about?"
}
```

Response:

```json
{
  "answer": "..."
}
```

## Project structure

```text
GENAI_PROJECT/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── rag.py
│   ├── core/
│   ├── models/
│   │   └── schemas.py
│   ├── services/
│   │   ├── document_loaders.py
│   │   ├── embedding_service.py
│   │   ├── llm_service.py
│   │   ├── text_splitter.py
│   │   ├── vector_store.py
│   │   └── rag_service.py
│   └── main.py
├── chroma_db/
├── data/
├── notebooks/
├── tests/
├── query.py
├── rag_pipeline.py
├── test_loader.py
├── test_llm.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd genai-rag-assistant
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Start Ollama

Install Ollama and pull a local model:

```powershell
ollama run phi3
```

### 5. Run the backend

```powershell
uvicorn app.main:app --reload
```

### 6. Open the API docs

Visit:

```text
http://127.0.0.1:8000/docs
```

## Environment variables

Create a `.env` file in the project root for local configuration.

Example:

```env
HF_TOKEN=
```

If you use additional services later, add their variables here as well.

## Testing the pipeline

### Ingestion test

```powershell
python test_loader.py
```

### Local LLM test

```powershell
python test_llm.py
```

### End-to-end RAG test

```powershell
python rag_pipeline.py
```

## Docker

Build and run the application with Docker:

```powershell
docker compose up --build
```

## Roadmap

This project is being extended into a full production-style GenAI service.

Planned upgrades:

* FastAPI upload endpoint for PDFs
* Multi-document ingestion
* Streamlit or React frontend
* Conversation memory
* Better retrieval with reranking and hybrid search
* Metadata filtering
* RAG evaluation suite for retrieval quality, hallucinations, and latency
* Deployment with Dockerized backend and hosted demo

## Why this project matters

This project demonstrates practical GenAI engineering skills:

* backend API design
* retrieval-augmented generation
* local model orchestration
* vector search
* modular service architecture
* Docker-based deployment readiness

It is a strong foundation for GenAI, AI platform, and applied ML engineering interviews.

## Notes

* Keep `.env`, PDFs, and other sensitive files out of Git.
* Use public or dummy documents while experimenting.
* Treat warnings carefully: some are deprecation notices, while others are harmless environment warnings.

## License

Add a license before public release.
