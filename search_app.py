import streamlit as st
from elasticsearch import Elasticsearch
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

# Connect to Elasticsearch
es = Elasticsearch(cloud_id=config['DEFAULT']['cloud_id'],
                   api_key=(config['DEFAULT']['apikey_id'], config['DEFAULT']['apikey_key']))


def search_movies(query, index_name="movie_embeddings", size=5):
    """
    Function to search for movies in Elasticsearch index.
    """
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["Series_Title", "Overview", "Director", "Star1", "Star2", "Star3", "Star4", "Genre"]
            }
        }
    }
    response = es.search(index=index_name, body=body, size=size)
    return response["hits"]["hits"]


def main():
    st.title("Movie Search Engine")

    # Input field for search query
    query = st.text_input("Enter movie title, actor, genre, or any other keyword")

    if st.button("Search"):
        # Search for movies
        results = search_movies(query)
        
        if results:
            st.subheader("Search Results:")
            for hit in results:
                st.markdown('---')
                movie_title = hit["_source"]["Series_Title"]
                st.write(f"**{movie_title}**")
                
                # Display poster image as a small square box
                st.image(hit['_source']['Poster_Link'], width=100)
                
                fields = ['Released_Year', 'Runtime', 'Genre', 'IMDB_Rating', 'Director', 'Overview']
                for field in fields:
                    if field in hit['_source'] and hit['_source'][field]:
                        st.write(f"**{field.replace('_', ' ')}:** {hit['_source'][field]}")
                if 'Certificate' in hit['_source'] and hit['_source']['Certificate'] and hit['_source']['Certificate'] != 'NotApp':
                    st.write(f"**Certificate:** {hit['_source']['Certificate']}")
        
        else:
            st.write("No results found.")


if __name__ == "__main__":
    main()
