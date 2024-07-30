from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from textblob import TextBlob  # type: ignore # You can replace this with any sentiment analysis library

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    # Analyze sentiment using TextBlob (or your preferred method)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    # Determine sentiment label
    sentiment_label = 'positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral'
    
    return jsonify({'sentiment': sentiment_label})

if __name__ == '__main__':
    app.run(debug=True)
