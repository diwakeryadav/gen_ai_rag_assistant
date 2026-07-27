from app.services.vector_store import get_vector_store
from app.services.llm_service import get_llm

llm = get_llm()

def ask_question(question: str):
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k":3})
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



