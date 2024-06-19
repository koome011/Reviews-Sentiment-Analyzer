import re
import json

# Load the JSON data
with open('reviews.json') as f:
    reviews_data = json.load(f)

def clean_text(text):
    # Remove special characters, punctuation, and extra spaces
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

# Clean the text data in each review
for review in reviews_data:
    review['cleaned_text'] = clean_text(review['Text'])

# Save the cleaned data back to the JSON file
with open('cleaned_reviews.json', 'w') as f:
    json.dump(reviews_data, f, indent=4)
