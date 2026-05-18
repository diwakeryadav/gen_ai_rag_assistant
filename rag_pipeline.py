from langchain_chroma import Chroma
from app.services.embedding_service import get_embeddings_model
from app.services.llm_service import get_llm

embedding_model =get_embeddings_model()

vector_store = Chroma(
    persist_directory = "chroma_db",
    embedding_function = embedding_model 
)

retriever =vector_store.as_retriever(search_kwargs={"k":3})

llm = get_llm()

query = "what is this document about ?"

docs = retriever.invoke(query)

context = "\n\n".join([doc.page_content for doc in docs])

prompt =f"""
Answer the question based ONLY on the context below.

context:
{context}

question:
{query}
"""

response = llm.invoke(prompt)

print(response)