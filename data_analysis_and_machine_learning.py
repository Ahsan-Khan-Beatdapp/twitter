import time
from transformers import pipeline, DistilBertTokenizer
import sqlite3
import pandas as pd

def calculate_average_sentiment(team_db, nlp):
    # Connect to the database
    conn = sqlite3.connect(team_db)
    # Fetch the posts
    cursor = conn.cursor()
    cursor.execute("SELECT post_text FROM posts")
    posts = [row[0] for row in cursor.fetchall()]

    # Initialize the sentiment analysis pipeline
    #nlp = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
    # Define a batch size
    batch_size = 10

    # Perform sentiment analysis on each batch of posts and store the results
    sentiment_scores = []
    for i in range(0, len(posts), batch_size):
        batch = posts[i:i+batch_size]
        results = nlp(batch, truncation=True, max_length=128, padding=True)

        for result in results:
            score = result['score'] * 100 if result['label'] == 'POSITIVE' else -(result['score'] * 100)
            # Transform the score range from -100 to 100 to 0 to 100
            score = (score + 100) / 2
            sentiment_scores.append(score)

        # Introduce a delay
        #time.sleep(3)

    # Calculate and return the average sentiment score
    return sum(sentiment_scores) / len(sentiment_scores)