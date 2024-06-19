import json
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the cleaned data
with open('cleaned_reviews.json') as f:
    reviews_data = json.load(f)

# Initialize the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# Perform sentiment analysis on each review
for review in reviews_data:
    review['sentiment_score'] = sid.polarity_scores(review['cleaned_text'])['compound']

# Save the sentiment analysis results back to the JSON file
with open('sentiment_scores.json', 'w') as f:
    json.dump(reviews_data, f, indent=4)
