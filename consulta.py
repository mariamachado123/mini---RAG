import os
from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

load_dotenv()
client = PersistentClient(path="db")
sentence_ef=SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection=client.get_or_create_collection("filosofos", embedding_function=sentence_ef)
frase_usuario="Tenemos un alma inmortal"

resultados=collection.query(query_texts=[frase_usuario], n_results=4)
fragmentos=resultados['documents'][0]
metadatos=resultados['metadatas'][0]
autores=[m["autor"] for m in metadatos]
contexto = "\n".join(f"- \"{f}\" ({a})" for f, a in zip(fragmentos, autores))

prompt = f"""
Eres un sabio filósofo de la antigüedad, conocedor de las enseñanzas de Platón, Aristóteles, Kant, Nietzsche y otros grandes pensadores.

Una persona se te acerca y te dice:
\"{frase_usuario}\"

A continuación, te comparto algunas citas relevantes de filósofos clásicos para que las uses como referencia para tu respuesta:

{contexto}

Por favor, responde con una reflexión profunda, clara y elegante, en un estilo filosófico que encaje con las ideas presentadas. Menciona al menos uno de los autores de las citas y no agregues información que no esté basada en ellas.
"""

model_name = "bigscience/bloom-560m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

respuesta_generada = generator(
    prompt,
    max_new_tokens=100,
    temperature=0.5,
    top_p=0.9,
    repetition_penalty=1.2,
    do_sample=True
)[0]['generated_text']

print("\n frase del usuario:")
print(frase_usuario)
print("\nautores sugeridos:")
print(", ".join(set(autores)))
print("\n respuesta del sabio:")
print(respuesta_generada)


