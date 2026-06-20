import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.models.schemas import QueryRequest, QueryResponse
from app.services.rag_service import ask_question
from app.services.document_loaders import load_pdf
from app.services.text_splitter import split_documents
from app.services.vector_store import add_to_vector_store
from langchain_core.documents import Document

router = APIRouter()
DATA_DIR = "data"

@router.post("/query", response_model = QueryResponse)
def query_rag(request: QueryRequest):
    result = ask_question(request.question)
    return QueryResponse(
        answer=result["answer"],
        sources=result["sources"]
    )

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, file.filename)

    # Save the file locally
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

    # Load, chunk and ingest
    ext = file.filename.lower()
    try:
        if ext.endswith('.pdf'):
            documents = load_pdf(file_path)
        elif ext.endswith(('.txt', '.md')):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            documents = [
                Document(
                    page_content=content,
                    metadata={"source": file.filename}
                )
            ]
        else:
            # Clean up the file if format unsupported
            if os.path.exists(file_path):
                os.remove(file_path)
            raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a PDF, TXT, or MD file.")

        chunks = split_documents(documents)
        add_to_vector_store(chunks)

    except Exception as e:
        # Clean up the file on ingestion failure
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Failed to process and ingest file: {str(e)}")

    return {
        "message": f"Successfully uploaded and ingested {file.filename}",
        "chunks": len(chunks)
    }