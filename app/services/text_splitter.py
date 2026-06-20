from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_core.documents import Document

headers_to_split_on = [
    ("#", " Chapter"),
    ("##", "Section"),
    ("###", "subsection")
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = headers_to_split_on
)

def split_documents(documents):

    final_docs = []

    for doc in documents:

        splits = markdown_splitter.split_text(
            doc.page_content
        )

        for split in splits:

            # preserve orgiinal source metdata
            split.metadata["source"] = doc.metadata.get(
                "source",
                "unknown"
            )

            final_docs.append(split)

    return final_docs