# Using python raw reddit api library to fetch data from reddit and store it in a database
# Using SQLite3 to create a database and store the data
import praw
import sqlite3
import pandas as pd

# Reddit API credentials
reddit = praw.Reddit(
    client_id="nkz3_hdkPvfyLdA3USbrSg",
    client_secret="joCDWyS5B5yBOKGZyBYdPKuwAyc_JA",
    user_agent="Living_Entire",
)

# Get posts from subreddit
posts = reddit.subreddit("raptors").new(limit=10)


# Connect to the database
conn = sqlite3.connect('posts.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        title TEXT,
        created_at TEXT,
        post_text TEXT
    )
''')

# THIS CODE BELOW CREATES A DATAFRAME AND PRINTS IT SIMILARLY TO THE DATABASE. For demonstration purposes only..
# Create an empty DataFrame
df = pd.DataFrame(columns=['title', 'created_at', 'post_text'])

# Insert posts into the database
for post in posts:
    c.execute('''
        INSERT INTO posts (title, created_at, post_text)
        VALUES (?, ?, ?)
    ''', (post.title, post.created_utc, post.selftext))
    
    # Append post data to DataFrame
    df = df.append({'title': post.title, 'created_at': post.created_utc, 'post_text': post.selftext}, ignore_index=True)

# Commit changes and close connection
conn.commit()
conn.close()

# Display the DataFrame
print(df)