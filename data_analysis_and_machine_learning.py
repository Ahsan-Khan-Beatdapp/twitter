import time
#from transformers import pipeline, DistilBertTokenizer
import sqlite3
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def calculate_average_sentiment(team_db):
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
    sia = SentimentIntensityAnalyzer()

    for i in range(0, len(posts), batch_size):
        batch = posts[i:i+batch_size]

        for post in batch:
            polarity_scores = sia.polarity_scores(post)
            # The 'compound' score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence. Calling it a 'normalized, weighted composite score' is accurate.
            # Transform the score range from -1 to 1 to 0 to 100
            score = (polarity_scores['compound'] + 1) * 50
            sentiment_scores.append(score)

        # Introduce a delay
        #time.sleep(3)

    # Calculate and return the average sentiment score
    return sum(sentiment_scores) / len(sentiment_scores)