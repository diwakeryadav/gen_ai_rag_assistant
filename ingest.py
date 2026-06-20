import argparse
import os
from app.services.document_loaders import load_directory
from app.services.text_splitter import split_documents
from app.services.vector_store import create_vector_store, reset_vector_store

def main():
    parser = argparse.ArgumentParser(description="Ingest documents into the vector database.")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Purge the existing vector store before ingesting new documents."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default="data",
        help="Directory containing the documents to ingest."
    )
    parser.add_argument(
        "--db-dir",
        type=str,
        default="chroma_db",
        help="Directory to persist the Chroma database."
    )

    args = parser.parse_args()

    if args.reset:
        print(f"Resetting vector store database in '{args.db_dir}'...")
        reset_vector_store(args.db_dir)

    print(f"Scanning directory '{args.dir}' for documents...")
    docs = load_directory(args.dir)

    if not docs:
        print("No documents found to ingest.")
        return

    print(f"Loaded {len(docs)} document(s). Splitting into chunks...")
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks.")

    print("Generating embeddings and writing to vector store...")
    create_vector_store(chunks, args.db_dir)
    print("Vector database ingestion completed successfully!")

if __name__ == "__main__":
    main()
