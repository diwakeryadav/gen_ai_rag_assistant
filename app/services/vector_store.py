import os
import shutil
from langchain_chroma import Chroma
from app.services.embedding_service import get_embeddings_model

def create_vector_store(chunks, persist_directory: str = "chroma_db"):
    embedding_model = get_embeddings_model()
    vector_store = Chroma.from_documents(
        documents = chunks,
        embedding = embedding_model,
        persist_directory = persist_directory
    )
    return vector_store

def add_to_vector_store(chunks, persist_directory: str = "chroma_db"):
    embedding_model = get_embeddings_model()
    vector_store = Chroma(
        persist_directory = persist_directory,
        embedding_function = embedding_model
    )
    vector_store.add_documents(chunks)
    return vector_store

def reset_vector_store(persist_directory: str = "chroma_db"):
    embedding_model = get_embeddings_model()
    try:
        vector_store = Chroma(
            persist_directory = persist_directory,
            embedding_function = embedding_model
        )
        vector_store.delete_collection()
        print(f"Cleared Chroma collection dynamically.")
    except Exception as e:
        print(f"Dynamic collection deletion failed: {e}. Falling back to directory removal...")
        if os.path.exists(persist_directory):
            try:
                shutil.rmtree(persist_directory)
                print(f"Purged vector store directory: {persist_directory}")
            except Exception as re:
                print(f"Error purging directory: {re}. If you have uvicorn/fastapi running, please stop it first.")
