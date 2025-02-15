# meme_suggester.py
from sklearn.metrics.pairwise import cosine_similarity

def suggest_meme_templates(user_input, df, vectorizer, tfidf_matrix, top_n=3):
    # Preprocess user input
    def clean_text(text):
        import re
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer

        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words("english"))

        # Lowercase
        text = text.lower()
        # Remove punctuation
        text = re.sub(r"[^\w\s]", "", text)
        # Remove stopwords
        text = " ".join([word for word in text.split() if word not in stop_words])
        # Lemmatize
        text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])
        return text

    user_input = clean_text(user_input)

    # Vectorize user input
    user_input_vec = vectorizer.transform([user_input])

    # Compute cosine similarity
    similarities = cosine_similarity(user_input_vec, tfidf_matrix).flatten()

    # Get top N meme templates
    top_indices = similarities.argsort()[-top_n:][::-1]
    suggested_templates = df.iloc[top_indices][["name", "base_img", "text_box"]].to_dict("records")

    return suggested_templates