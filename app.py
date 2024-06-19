from flask import Flask, render_template, request, jsonify
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load the sentiment analysis results
with open('sentiment_scores.json') as f:
    sentiment_data = json.load(f)

# Initialize the SentimentIntensityAnalyzer (VADER)
sid = SentimentIntensityAnalyzer()

# Create lists to store sentiment scores for each product
product_sentiments = {}

# Aggregate sentiment scores for each product
for review in sentiment_data:
    product = review['Product']
    sentiment_score = sid.polarity_scores(review['cleaned_text'])['compound']
    
    if product not in product_sentiments:
        product_sentiments[product] = []
    
    product_sentiments[product].append(sentiment_score)

# Calculate proportion of positive, neutral, and negative reviews for each product
product_sentiment_distribution = {}
for product, scores in product_sentiments.items():
    positive_count = sum(score > 0 for score in scores)
    neutral_count = sum(score == 0 for score in scores)
    negative_count = sum(score < 0 for score in scores)
    total_count = len(scores)
    product_sentiment_distribution[product] = {
        'Positive': positive_count / total_count,
        'Neutral': neutral_count / total_count,
        'Negative': negative_count / total_count
    }

# Define a route to serve the main page
@app.route('/')
def index():
    products = list(product_sentiment_distribution.keys())
    return render_template('index.html', products=products)

# Define a route to handle product selection
@app.route('/get_sentiment', methods=['POST'])
def get_sentiment():
    selected_product = request.json['product']
    sentiment_distribution = product_sentiment_distribution.get(selected_product, {})
    return jsonify(sentiment_distribution)

if __name__ == '__main__':
    app.run(debug=True)
