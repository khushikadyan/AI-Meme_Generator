import pandas as pd
import re
import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download NLTK resources if not already present
nltk.download("stopwords")
nltk.download("wordnet")

def load_data(json_path="memes.json/memes.json"):
    # Load JSON into a DataFrame
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)

    # Ensure required columns exist
    required_columns = {"name", "base_img", "text_box", "generated_memes"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Dataset must contain {required_columns}")

    # Extract captions from 'generated_memes'
    df["captions"] = df["generated_memes"].apply(lambda x: [item.get("alt_text", "") for item in x])
    df["text"] = df["captions"].apply(lambda x: " ".join(x))  # Combine captions into a single text field

    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    def clean_text(text):
        text = text.lower()  # Lowercase
        text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
        text = " ".join([word for word in text.split() if word not in stop_words])  # Remove stopwords
        text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])  # Lemmatize
        return text

    # Apply text cleaning
    df["text"] = df["text"].apply(clean_text)

    return df

def vectorize_text(df):
    """Creates a TF-IDF vectorizer and transforms text data."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["text"])
    return vectorizer, tfidf_matrix
