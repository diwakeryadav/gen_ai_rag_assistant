from langchain_chroma import Chroma
from app.services.embedding_service import get_embeddings_model
from app.services.llm_service import get_llm

embedding_model = get_embeddings_model()

vector_store = Chroma (
    persist_directory = "chroma_db",
    embedding_function = embedding_model
)

retriever = vector_store.as_retriever(search_kwargs={"k":3})

llm = get_llm()

def ask_question(question: str):
    
    docs = retriever.invoke(question)

    # Extract unique source names from metadata
    sources = []
    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        if source not in sources:
            sources.append(source)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question based ONLY on the context below.

    context :
    {context}

    question:
    {question}
    """

    response = llm.invoke(prompt)
    return {
        "answer": response,
        "sources": sources
    }



