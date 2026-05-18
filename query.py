from langchain_chroma import Chroma
from app.services.embedding_service import get_embeddings_model

embedding_model = get_embeddings_model()

vector_store = Chroma(
    persist_directory = "chroma_db",
    embedding_function = embedding_model
)

query = "what is this document about"

results = vector_store.similarity_search(query,k=3)

for i, result in enumerate(results):
    print(f"\n Result {i+1}")
    print(result.page_content)
    print("=" * 50)