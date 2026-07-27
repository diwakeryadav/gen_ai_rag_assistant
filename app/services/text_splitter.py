from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.documents import Document

headers_to_split_on = [
    ("#", " Chapter"),
    ("##", "Section"),
    ("###", "subsection")
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = headers_to_split_on
)

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 800,
    chunk_overlap = 100
)

def split_documents(documents):

    final_docs = []

    for doc in documents:

        splits = markdown_splitter.split_text(
            doc.page_content
        )
        
        # Sub-split large markdown structural sections recursively
        chunks = recursive_splitter.split_documents(splits)

        for chunk in chunks:

            # preserve original source metadata
            chunk.metadata["source"] = doc.metadata.get(
                "source",
                "unknown"
            )

            final_docs.append(chunk)

    return final_docs