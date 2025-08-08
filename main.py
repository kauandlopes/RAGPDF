from langchain_chroma import Chroma
from g4f.client import Client
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

class LocalEmbeddings:
    def embed_documents(self, texts):
        return embedding_model.encode(texts).tolist()

    def embed_query(self, text):
        return embedding_model.encode([text])[0].tolist()

def responder(pergunta):
    

    db = Chroma(
        persist_directory="db",
        embedding_function=LocalEmbeddings()
    )

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=4)

    contexto = "\n\n".join([doc.page_content for doc, _ in resultados])

    client = Client()

    prompt = f"""
Baseie-se apenas nas informações abaixo para responder.

Contexto:
{contexto}

Pergunta: {pergunta}
"""

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return resposta.choices[0].message.content

if __name__ == "__main__":
    responder()
