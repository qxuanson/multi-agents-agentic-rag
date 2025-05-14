# Save data to Chroma DB
import os
import pandas as pd
from flask import Flask, request, jsonify, Blueprint
from werkzeug.utils import secure_filename
from google import genai
from google.genai import types
from dotenv import load_dotenv
import re
import chromadb
import uuid
import time
from key import GOOGLE_API_KEY
load_dotenv()

# Flask App Initialization
app = Flask(__name__)


# Gemini Client for embeddings
client = genai.Client(api_key=GOOGLE_API_KEY)

training_bp = Blueprint('training', __name__, url_prefix='/training')

def get_embedding(text: str) -> list[float]:
    """Generates an embedding for a given text using OpenAI."""
    time.sleep(10)  # Wait 5 seconds between API calls
    response = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=text,
        config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)
    return response.embeddings[0].values

def sanitize_collection_name(name: str) -> str:
    """Sanitize collection name to be MongoDB-compatible."""
    name = re.sub(r'[^a-zA-Z0-9_]', '_', name)  # Replace invalid characters with '_'
    name = name.strip("_")  # Remove leading/trailing underscores
    return name.lower()  # Convert to lowercase for consistency

def sanitize_metadata(record):
    """Convert None values in metadata to empty string or default values, and exclude embeddings."""
    sanitized_record = {
        k: (str(v) if v is not None else "") for k, v in record.items() if k != "embedding"
    }
    return sanitized_record

df = pd.read_csv("./data.csv")


import ast
def join_string(item):
    for i in range(len(item)):
        name, endow, content, price, technical_info = item

        final_string = ""
        if name:
            final_string += f"{name}"

        if endow:
            endow = endow.replace("<br>", " ").replace("\n", " ")
            final_string += f" {endow}"

        if content:
            content = content.replace("<br>", " ").replace("\n", " ")
            final_string += f" {content}"

        if price:
            final_string += f" có giá: {price}"

        if technical_info:
            technical_info = technical_info.replace("<br>", " ").replace("\n", " ")
            final_string += f" có thông số kĩ thuật: {technical_info}"

    return final_string

df['information'] = df[
    [
     'name',
     'endow',
     'content',
     'price',
     'technical_info']
    ].astype(str).apply(join_string, axis=1)


# Display the DataFrame to confirm
df = df.head(10)

# Prepare data
df = df[df['information'].notna()]
print(df.head())
print(df.info())
total_items = len(df)
print(f"\nStarting embedding process for {total_items} items...")

# Add progress tracking with item counter
def get_embedding_with_progress(text, idx):
    print(f"Processing item {idx+1}/{total_items}...")
    return get_embedding(text)

df["embedding"] = [get_embedding_with_progress(x, i) for i, x in enumerate(df["information"])]
print("Embedding process completed!")

# Metadata
metadatas = [{"information": row["information"]} for _, row in df.iterrows()]
ids = [str(uuid.uuid4()) for _ in range(len(df))]

# ChromaDB setup
# ChromaDB setup
chroma_client = chromadb.PersistentClient(path="./chroma_db_product")
collection = chroma_client.create_collection(name="product_info")

# Insert data
collection.add(
    ids=ids,
    embeddings=df["embedding"].tolist(),
    metadatas=metadatas
)
print(collection.get())
print(f"Inserted {len(df)} documents into ChromaDB collection '{collection.name}'.")