# ElasticSearch-Movie-Search-Engine

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Security Considerations](#security-considerations)
- [Scenarios Handled](#scenarios-handled)
- [Contributions](#contributions)

## Project Description

This project is a movie search engine that allows users to search for movies based on various attributes such as title, actors, genre, and more. It leverages Elasticsearch for efficient search capabilities and Sentence Transformers for embedding movie descriptions. The application consists of three main components:

1. **Data Cleaning**: Cleans and preprocesses the movie dataset.
2. **Embedding and Storing**: Generates embeddings for the cleaned data and stores them in Elasticsearch.
3. **Search Application**: Provides a user interface for searching movies.

## Features

- **Data Cleaning**: Handles missing values, converts data types, and cleans text fields.
- **Embedding Generation**: Uses Sentence Transformers to generate embeddings for movie descriptions.
- **Elasticsearch Integration**: Stores movie data and embeddings in Elasticsearch for fast and efficient search.
- **Search Interface**: A Streamlit-based web application for searching movies.

## Requirements

- Python 3.7 or higher
- Pandas
- Sentence Transformers
- Elasticsearch Python client
- Streamlit

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/movie-search-engine.git
   cd movie-search-engine
   ```

2. **Install required packages**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Download the movie dataset**:
   Ensure you have the `imdb_top_1000.csv` file in the root directory.

## Configuration

1. **Configure Elasticsearch**:
   - Create an `example.ini` file with your Elasticsearch cloud ID and API keys(You can get a 14 day free trial at [Elastic Cloud](https://www.elastic.co/cloud/cloud-trial-overview?utm_campaign=Google-B-Amer-US-RLSA&utm_content=Brand-Core-Cloud-EXT&utm_source=google&utm_medium=cpc&device=c&utm_term=elastic%20cloud&gad_source=1&gclid=CjwKCAjwmrqzBhAoEiwAXVpgokDEdaz5YMR50Y1LTTtJNhSLyopAfQFtXNUrWdHEgsQH_Y4o_Hn3uRoCKuUQAvD_BwE)):
     ```ini
     [DEFAULT]
     cloud_id = "DeploymentCloudID"
     apikey_id = "API Key ID"
     apikey_key = "API Key"
     ```

## Running the Application

### Step 1: Data Cleaning

1. **Run the data cleaning script**:
   ```sh
   python clean_data.py
   ```
   This script will clean the dataset and save it as `cleaned_dataset.csv`.

### Step 2: Embedding and Storing

1. **Run the embedding and storing script**:
   ```sh
   python embed_and_store.py
   ```
   This script will generate embeddings for the cleaned data and store them in Elasticsearch.

### Step 3: Search Application

1. **Run the search application**:
   ```sh
   streamlit run search_app.py
   ```
   Open the provided URL in your browser to access the search interface.


## Security Considerations

- Ensure Elasticsearch is securely configured to prevent unauthorized access.
- Keep your API keys and sensitive information secure.
- Validate and sanitize user inputs to prevent injection attacks.

## Scenarios Handled

- **Search by Title**: Users can search for movies by entering the title.
- **Search by Actor**: Users can search for movies by entering an actor's name.
- **Search by Genre**: Users can search for movies by entering a genre.
- **Search by Keywords**: Users can search using any relevant keywords.

## Contributions

Contributions are welcome! Please create an issue or submit a pull request with your changes.