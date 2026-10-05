import streamlit as st
import chromadb
import ollama
from sentence_transformers import SentenceTransformer

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI-Based Event Helpdesk",
    page_icon="🤖"
)

st.title("🤖 AI-Based Event Helpdesk")
st.write("Ask questions about the event.")

# -----------------------------
# Load embedding model
# -----------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )


model = load_model()

# -----------------------------
# Connect to ChromaDB
# -----------------------------
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="event_helpdesk"
)

# -----------------------------
# Chat memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# -----------------------------
# User question
# -----------------------------
question = st.chat_input("Ask your event question...")

if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Create question embedding
    query_embedding = model.encode(
        [question]
    ).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    # Get relevant documents
    documents = results["documents"][0]

    context = "\n\n".join(documents)

    # Create conversation history
    history = ""

    for message in st.session_state.messages[-6:]:
        history += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    # Prompt for Ollama
    prompt = f"""
You are an AI-Based Event Helpdesk assistant.

Answer the user's question using the event information
provided below.

If the answer is not available in the event information,
say that the information is not available.

Do not invent event information.

EVENT INFORMATION:
{context}

CONVERSATION HISTORY:
{history}

USER QUESTION:
{question}

Give a clear and simple answer.
"""

    # Ask Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    # Display answer
    with st.chat_message("assistant"):
        st.write(answer)

    # Save answer to memory
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })