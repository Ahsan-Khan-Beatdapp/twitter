# Using python raw reddit api library to fetch data from reddit and store it in a database
# Using SQLite3 to create a database and store the data
import praw
import sqlite3
import pandas as pd

# Reddit API credentialsbu
reddit = praw.Reddit(
    client_id="nkz3_hdkPvfyLdA3USbrSg",
    client_secret="joCDWyS5B5yBOKGZyBYdPKuwAyc_JA",
    user_agent="Living_Entire",
)

# List of subreddits
subreddits = ['lakers', 'celtics', 'raptors']

def fetch_data_and_create_db():
    for subreddit in subreddits:
        # Connect to the database
        conn = sqlite3.connect(f'{subreddit}.db')
        c = conn.cursor()

        # Drop the 'posts' table if it exists
        c.execute('DROP TABLE IF EXISTS posts')

        # Create the 'posts' table
        c.execute('''
            CREATE TABLE posts (
                title TEXT,
                created_at REAL,
                post_text TEXT,
                subreddit TEXT
            )
        ''')

        # Fetch posts from the subreddit
        posts = reddit.subreddit(subreddit).hot(limit=200)

        # Insert posts into the database
        for post in posts:
            c.execute('''
                INSERT INTO posts (title, created_at, post_text, subreddit)
                VALUES (?, ?, ?, ?)
            ''', (post.title, post.created_utc, post.selftext, subreddit))

        # Commit changes
        conn.commit()

        # Load the data from the 'posts' table into a DataFrame
        #df = pd.read_sql_query("SELECT * FROM posts", conn)

        # Print the DataFrame
        #print(df)

        # Close connection
        conn.close()

if __name__ == "__main__":
    fetch_data_and_create_db()