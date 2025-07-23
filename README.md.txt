# Mini RAG -¿Qué dijo el Filósofo?

## Descripción

Este proyecto crea un mini sistema RAG (Retrieval-Augmented Generation) que recibe una frase del usuario y responde con una cita filosófica relacionada, incluyendo el autor. Usa ChromaDB para almacenar y buscar frases vectorizadas, y un modelo local Bloom-560m para generar respuestas estilo filósofo.

## Contenido principal

- `vectorizar.py`: carga y vectoriza frases filosóficas desde `frases.csv` a ChromaDB.  
- `consulta.py`: recibe una frase, busca las citas más similares y genera una respuesta filosófica.  
- `frases.csv`: archivo con 30+ frases y sus autores.  
- `Dockerfile`: para correr el proyecto en un contenedor Docker  
- `requirements.txt`: dependencias Python

## Instalación

1. Clonar el repositorio  
2. Instalar dependencias:

pip install -r requirements.txt

## Uso

Ejecutar los scripts en este orden:

### Vectorizar frases y cargar a la base ChromaDB:

python vectorizar.py

### Consulatpara probar el RAG:

Python consulta.py