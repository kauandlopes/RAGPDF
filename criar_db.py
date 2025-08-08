from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# pasta onde esta o banco de dados e para onde os arquivos vetorizados vão
PASTA_BASE = "base"  
CAMINHO_DB = "db"    

def carregar_documentos():
    loader = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = loader.load()
    print(f"Documentos carregados: {len(documentos)}")
    return documentos

def dividir_chunks(documentos):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )

    chunks = splitter.split_documents(documentos)
    print(f"Chunks criados: {len(chunks)}")
    return chunks

def vetorizar_chunks(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  
    
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CAMINHO_DB
    )
    print("Banco vetorial criado e salvo em:", CAMINHO_DB)

def criar_db():
    documentos = carregar_documentos()
    chunks = dividir_chunks(documentos)
    vetorizar_chunks(chunks)

if __name__ == "__main__":
    # caso rodar esse arquivo, substituir o antigo banco de dados
    if os.path.exists(CAMINHO_DB):
        import shutil
        shutil.rmtree(CAMINHO_DB)
        print("DB antigo apagado.")
    

    criar_db()
