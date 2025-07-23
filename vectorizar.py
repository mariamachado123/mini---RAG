# vectorizar.py
import csv
import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

client = chromadb.PersistentClient(path="db")
embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = client.get_or_create_collection("filosofos", embedding_function=embedding_fn)

if collection.count() == 0:
    with open("frases.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            collection.add(
                documents=[row["frase"]],
                metadatas=[{"autor": row["autor"]}],
                ids=[f"frase_{idx}"]
            )
    print("Base cargada con éxito.")
else:
    print("La colección ya contiene datos.")
