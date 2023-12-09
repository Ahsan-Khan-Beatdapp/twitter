from transformers import pipeline, DistilBertTokenizer
import sqlite3
import pandas as pd


def calculate_average_sentiment(team_db):
    # Connect to the database
    conn = sqlite3.connect(team_db)
    # Load the posts into a DataFrame
    df = pd.read_sql_query("SELECT * FROM posts", conn)

    # Initialize the sentiment analysis pipeline
    nlp = pipeline('sentiment-analysis')

    # Perform sentiment analysis on each post and store the results
    sentiment_scores = []
    posts = df['post_text'].tolist()
    # Define a batch size
    batch_size = 100

    # Perform sentiment analysis on each batch of posts and store the results
    sentiment_scores = []
    for i in range(0, len(posts), batch_size):
        batch = posts[i:i+batch_size]
        results = nlp(batch, truncation=True, max_length=512, padding=True)

        for result in results:
            score = result['score'] * 100 if result['label'] == 'POSITIVE' else -(result['score'] * 100)
            # Transform the score range from -100 to 100 to 0 to 100
            score = (score + 100) / 2
            sentiment_scores.append(score)

    # Calculate the average sentiment score
    if len(sentiment_scores) > 0:
        average_score = sum(sentiment_scores) / len(sentiment_scores)
        return average_score
    else:
        print("No posts were processed.")
        return None

