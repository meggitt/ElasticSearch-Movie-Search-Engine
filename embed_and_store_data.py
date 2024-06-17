from sentence_transformers import SentenceTransformer
import pandas as pd
from elasticsearch import Elasticsearch
import numpy as np
from elasticsearch import Elasticsearch, helpers
import configparser
config = configparser.ConfigParser()
config.read('example.ini')
# Load a pre-trained Sentence Transformers model
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

df= pd.read_csv("cleaned_dataset.csv")
# Embed the text using Sentence Transformers
embeddings = model.encode(df['clean_text'].tolist())

# Convert embeddings to numpy array
embedding_array = np.array(embeddings)

# Connect to Elasticsearch
es = Elasticsearch(cloud_id=config['DEFAULT']['cloud_id'],
    api_key=(config['DEFAULT']['apikey_id'], config['DEFAULT']['apikey_key']),)

# Create index in Elasticsearch
index_name = "movie_embeddings"
es.indices.create(index=index_name, ignore=400)

# Store embeddings in Elasticsearch
for i, embedding in enumerate(embedding_array):
    document = {
        "Series_Title": df.loc[i, 'Series_Title'],
        "Poster_Link": df.loc[i, 'Poster_Link'],
        "Released_Year": df.loc[i, 'Released_Year'],
        "Certificate": df.loc[i, 'Certificate'],
        "Runtime": df.loc[i, 'Runtime'],
        "Genre": df.loc[i, 'Genre'],
        "IMDB_Rating": df.loc[i, 'IMDB_Rating'],
        "Overview": df.loc[i, 'Overview'],
        "Meta_score": df.loc[i, 'Meta_score'],
        "Director": df.loc[i, 'Director'],
        "Star1": df.loc[i, 'Star1'],
        "Star2": df.loc[i, 'Star2'],
        "Star3": df.loc[i, 'Star3'],
        "Star4": df.loc[i, 'Star4'],
        "No_of_Votes": df.loc[i, 'No_of_Votes'],
        "Gross": df.loc[i, 'Gross'],
        "Embedding": embedding.tolist(),
    }
    es.index(index=index_name, id=i, body=document)

print("Embeddings stored in Elasticsearch.")
