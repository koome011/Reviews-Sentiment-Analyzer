import json
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

# Plot pie charts for sentiment distribution of each product
for product, distribution in product_sentiment_distribution.items():
    labels = distribution.keys()
    sizes = distribution.values()
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Sentiment Distribution for {product}')
    plt.axis('equal')
    plt.show()
