import sqlite3
import pandas as pd
from transformers import pipeline

# Connect to the database
conn = sqlite3.connect('posts.db')

# Fetch the post_text data
df = pd.read_sql_query("SELECT post_text FROM posts", conn)

# Close the database connection
conn.close()

# Initialize the sentiment analysis pipeline
nlp = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

from transformers import DistilBertTokenizer

# Initialize the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Perform sentiment analysis on each post and store the results
sentiment_scores = []
for post in df['post_text']:
    try:
        result = nlp(post, truncation=True, max_length=512)[0]  # Enable truncation here
        score = result['score'] * 100 if result['label'] == 'POSITIVE' else -(result['score'] * 100)
        # Transform the score range from -100 to 100 to 0 to 100
        score = (score + 100) / 2
        sentiment_scores.append(score)
    except Exception as e:
        print(f"Error processing post: {e}")

# Calculate the average sentiment score
if len(sentiment_scores) > 0:
    average_score = sum(sentiment_scores) / len(sentiment_scores)
    print(f'The average sentiment score is {average_score}')
else:
    print("No posts were processed.")

