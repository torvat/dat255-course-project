import re, os
from pypdf import PdfReader
from langchain_community.document_loaders import (
    UnstructuredExcelLoader,
    UnstructuredWordDocumentLoader)
from langchain.schema import Document
from typing import List
from langchain.text_splitter import TokenTextSplitter

def clean_text(text):
    # Remove excessive newlines and keep only ASCII + æøå characters.
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'[^\x00-\x7FæøåÆØÅ]+', '', text)
    # Remove empty strings
    text = "\n".join([line for line in text.split('\n') if line.strip() != ''])
    return text

def word_document_to_document(file: str) -> Document:
    loader = UnstructuredWordDocumentLoader(file_path=file)
    data = loader.load()
    return data[0]

def pdf_to_document(file) -> Document:
    reader = PdfReader(file)
    text = ''
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    cleaned_text = clean_text(text)
    return Document(page_content=cleaned_text)

def excel_to_document(file) -> Document:
    loader = UnstructuredExcelLoader(file)
    data = loader.load()
    return data[0]

def process_file(file) -> Document:
    filename: str = file if isinstance(file, str) else file.filename
    if filename.endswith('.docx') or filename.endswith('.doc'):
        return word_document_to_document(file)
    elif filename.endswith('.pdf'):
        return pdf_to_document(file)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        return excel_to_document(file)

    raise Exception(f"Unsupported file type: {filename}")

def read_files(content_path):
    documents: List[Document] = list()
    for dirname, _, filenames in os.walk(content_path):
        for filename in filenames:
            documents.append(process_file(os.path.join(dirname, filename)))
    return documents

def split_document_by_tokens(document: list[Document], chunk_size: int, overlap: int):
    splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_documents(document)