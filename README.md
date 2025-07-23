# Mini RAG -¿Qué dijo el Filósofo?

## Descripción

Este proyecto crea un mini sistema RAG (Retrieval-Augmented Generation) que recibe una frase del usuario y responde con una cita filosófica relacionada, incluyendo el autor. Usa ChromaDB para almacenar y buscar frases vectorizadas, y un modelo local Bloom-560m para generar respuestas estilo filósofo.

## Contenido principal

- vectorizar.py: carga y vectoriza frases filosóficas desde frases.csv a ChromaDB.  
- consulta.py: recibe una frase, busca las citas más similares y genera una respuesta filosófica.  
- frases.csv: archivo con 30+ frases y sus autores.  
- requirements.txt: dependencias Python

## Instalación

1. Clonar el repositorio  
2. Instalar dependencias:

pip install -r requirements.txt

## Uso

Ejecutar los scripts en este orden:

### Vectorizar frases y cargar a la base ChromaDB:

python vectorizar.py

### Consulta para probar el RAG:

python consulta.py

## Detalles

Utilicé Hugging face, ya que es una manera bastante didáctica de conocer y aprender, además de que es local y gratuita y fácil de usar.

No pude utilizar OpenAi porque llegó un momento que no podía utilizarlo, por lo que decidí cambiar.

Además, existe la posibilidad de que, al empezar a ejecutar, al principio, pueda tardar, es normal.
