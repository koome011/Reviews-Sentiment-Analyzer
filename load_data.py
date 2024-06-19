import json

# Load the JSON data
with open('reviews.json') as f:
    reviews_data = json.load(f)

# Print the first few entries
for review in reviews_data[:10]:
    print(review)
