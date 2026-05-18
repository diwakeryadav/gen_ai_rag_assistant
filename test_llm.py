from app.services.llm_service import get_llm

llm = get_llm()

response = llm.invoke("explain RAG in simple words")

print(response)