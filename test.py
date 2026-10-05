from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

text = ["This is my handwritten notes search project."]
embedding = model.encode(text)

print(embedding.shape)