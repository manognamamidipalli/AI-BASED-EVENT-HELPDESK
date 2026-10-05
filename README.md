# AI-Based Event Helpdesk

## Project Overview

AI-Based Event Helpdesk is an intelligent chatbot that helps users
get information about an event.

The system uses Document RAG to retrieve relevant information from
event documents and uses Ollama to generate clear answers.

The chatbot also maintains conversation memory to provide
context-aware responses.

## Objectives

- Provide quick event-related information.
- Search event documents using RAG.
- Use semantic search for relevant information.
- Maintain chatbot conversation memory.
- Provide an easy-to-use chatbot interface.

## Features

- Interactive chatbot
- Document-based RAG
- Chat memory
- Semantic search
- ChromaDB
- Sentence Transformers
- Ollama
- Streamlit

## Technologies Used

- Python
- Streamlit
- Sentence Transformers
- ChromaDB
- Ollama
- RAG
- GitHub

## Project Architecture

User
↓
Streamlit
↓
Question Embedding
↓
ChromaDB
↓
Relevant Event Documents
↓
RAG
↓
Ollama
↓
AI Answer

## Project Structure

AI-Based-Event-Helpdesk/

├── app.py
├── ingest.py
├── memory.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    └── event_information.md

## How to Run

Install the required packages:

pip install -r requirements.txt

Create the RAG database:

python ingest.py

Start the chatbot:

streamlit run app.py