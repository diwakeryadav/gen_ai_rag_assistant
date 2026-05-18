from app.services.document_loaders import load_pdf
from app.services.text_splitter import split_documents
from app.services.vector_store import create_vector_store

docs = load_pdf("data/sample.pdf")

chunks = split_documents(docs)

vector_store = create_vector_store(chunks)

print("Vector DB created successfully")
print(f"Total chunks : {len(chunks)}")
print(docs[0].page_content)