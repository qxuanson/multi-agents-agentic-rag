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
import numpy as np

chroma_client = chromadb.PersistentClient(path="./chroma_db_product")
collection_name = "product_info"

load_dotenv()
# Gemini Client for embeddings
client = genai.Client(api_key="AIzaSyCIqLFWBr3S2T-91BP3-E0pCtwuOGsooHU")

def get_embedding(text: str) -> list[float]:
    """Generates an embedding for a given text using OpenAI."""
    time.sleep(10)  # Wait 5 seconds between API calls
    response = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=text,
        config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)
    return response.embeddings[0].values

def rag(query: str) -> str:

    print('----Product', query)

    collection = chroma_client.get_collection(name=collection_name)
    query_embedding = get_embedding(query)
    query_embedding = query_embedding / np.linalg.norm(query_embedding)

    # Perform vector search
    search_results = collection.query(
        query_embeddings=query_embedding, 
        n_results=10
    )

    metadatas = search_results.get('metadatas', [])

    search_result = ""
    i = 0

    for i, metadata_list in enumerate(metadatas):
        if isinstance(metadata_list, list):  # Ensure it's a list
            for metadata in metadata_list:  # Iterate through all dicts in the list
                if isinstance(metadata, dict):
                    combined_text = metadata.get('information', 'No text available').strip()

                    search_result += f"{i}). \n{combined_text}\n\n"
                    i += 1
    return search_result