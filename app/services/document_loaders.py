import os
import pymupdf4llm
from langchain_core.documents import Document

def load_pdf(file_path : str):
    try:
        md_text = pymupdf4llm.to_markdown(file_path)
    except Exception as e:
        print(f"Error loading PDF {file_path}: {e}")
        raise e

    if isinstance(md_text, list):
        md_text = "\n".join(
            [
                item.get("text", "")
                if isinstance(item, dict)
                else str(item)
                for item in md_text
            ]
        )

    # Use only the base filename for source to avoid leaking local username/paths on resume
    source_name = os.path.basename(file_path)

    return [
        Document(
            page_content=md_text,
            metadata={
                "source": source_name
            }
        )
    ]

def load_directory(directory_path: str) -> list[Document]:
    documents = []
    if not os.path.exists(directory_path):
        return documents

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if not os.path.isfile(file_path):
            continue

        ext = filename.lower()
        try:
            if ext.endswith('.pdf'):
                documents.extend(load_pdf(file_path))
            elif ext.endswith(('.txt', '.md')):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                documents.append(
                    Document(
                        page_content=content,
                        metadata={
                            "source": filename
                        }
                    )
                )
        except Exception as e:
            print(f"Failed to load document {filename}: {e}")

    return documents