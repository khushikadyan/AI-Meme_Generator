from flask import Flask, request, jsonify
from data_loader import load_data, vectorize_text
from meme_suggester import suggest_meme_templates

app = Flask(__name__)

# Load data and vectorize text
df = load_data()
vectorizer, tfidf_matrix = vectorize_text(df)

@app.route("/suggest-memes", methods=["POST"])
def suggest_memes():
    # Get user input from the request
    data = request.json
    
    user_input = data.get("idea")
    
    # Get meme suggestions from the AI model
    suggestions = suggest_meme_templates(user_input, df, vectorizer, tfidf_matrix)
    
    print("Suggestions:", suggestions)
    # Return suggestions as JSON
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(port=5000)