from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Create persistent ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get collection
collection = client.get_or_create_collection(
    name="event_helpdesk"
)

# Read event document
with open("data/event_information.md", "r", encoding="utf-8") as file:
    text = file.read()

# Split document into sections
documents = [
    section.strip()
    for section in text.split("\n\n")
    if section.strip()
]

# Create IDs
ids = [f"event_{i}" for i in range(len(documents))]

# Create embeddings
embeddings = model.encode(documents).tolist()

# Store in ChromaDB
collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings
)

print("Event document successfully stored in ChromaDB!")
print(f"Number of documents stored: {len(documents)}")