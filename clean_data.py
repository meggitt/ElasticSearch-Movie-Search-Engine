import pandas as pd
import re

# Load the dataset
# Assuming your dataset is loaded into a DataFrame named df
df = pd.read_csv('imdb_top_1000.csv')

# Define columns to use
columns_to_use = ['Poster_Link', 'Series_Title', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 
                  'IMDB_Rating', 'Overview', 'Meta_score', 'Director', 'Star1', 
                  'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross']

# Clean your columns
def clean_text(text):
    if pd.isnull(text):  # Check for missing values
        return ''  # Return empty string for missing values
    elif isinstance(text, str):
        # Remove special characters, punctuation, and extra whitespaces
        text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
        text = re.sub(r'\s+', ' ', text.strip())  # Remove extra whitespaces
        return text.strip()
    elif isinstance(text, (int, float)):
        # Convert numbers and floats to string
        return str(text)
    else:
        return ''  # Return empty string for other types

def clean_year(year):
    if isinstance(year, str):
        if year.isdigit():
            return int(year)
        else:
            return 0
    else:
        return int(year)

def clean_certificate(certificate):
    if isinstance(certificate,str):
        return clean_text(certificate)
    else:
        return "NotApp"

def clean_score(score):
    if isinstance(score, str):
        if score.isdigit():
            return int(score)
        else:
            return 0
    else:
        if type(score) == float and pd.isna(score):
            return 0
        return int(score)

def clean_votes(votes):
    if isinstance(votes, str):
        return int(votes.replace(',', ''))
    else:
        return int(votes)

def clean_gross(gross):
    if isinstance(gross, str):
        return int(gross.replace(',', ''))
    else:
        if type(gross) == float and pd.isna(gross):
            return 0
        return int(gross)

# Apply cleaning functions to each column
df['Poster_Link'] = df['Poster_Link'].apply(str)
df['Series_Title'] = df['Series_Title'].apply(clean_text)
df['Released_Year'] = df['Released_Year'].apply(clean_year)
df['Certificate'] = df['Certificate'].apply(clean_certificate)
df['Runtime'] = df['Runtime'].apply(str)
df['Genre'] = df['Genre'].apply(str)
df['IMDB_Rating'] = df['IMDB_Rating'].astype(float)
df['Overview'] = df['Overview'].apply(clean_text)
df['Meta_score'] = df['Meta_score'].apply(clean_score)
df['Director'] = df['Director'].apply(clean_text)
df['Star1'] = df['Star1'].apply(clean_text)
df['Star2'] = df['Star2'].apply(clean_text)
df['Star3'] = df['Star3'].apply(clean_text)
df['Star4'] = df['Star4'].apply(clean_text)
df['No_of_Votes'] = df['No_of_Votes'].apply(clean_votes)
df['Gross'] = df['Gross'].apply(clean_gross)

# Drop rows with missing values in 'Series_Title'
df.dropna(subset=['Series_Title'], inplace=True)

# Concatenate fields and clean text
df['clean_text'] = df['Series_Title'] + " " + df['Overview'] + " " + df['Director'] + " " + df['Star1'] + " " + df['Star2'] + " " + df['Star3'] + " " + df['Star4'] + " " + df["Genre"]
df['clean_text'] = df['clean_text'].apply(clean_text)

df.to_csv('cleaned_dataset.csv', index=False)