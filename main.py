from data_loader import load_data, vectorize_text
from meme_suggester import suggest_meme_templates

# Load and process data
df = load_data()
vectorizer, tfidf_matrix = vectorize_text(df)

# Get user input
if __name__ == "__main__":
    user_input = input("Enter a meme idea: ")
    suggestions = suggest_meme_templates(user_input, df, vectorizer, tfidf_matrix)
    print("Suggested Meme Templates:", suggestions)
