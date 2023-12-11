import unittest
from unittest.mock import patch, MagicMock
import fetch_reddit_data_and_create_db

class TestRedditDataFetcher(unittest.TestCase):

    @patch('fetch_reddit_data_and_create_db.praw')
    def test_reddit_api_call(self, mock_praw):
        """
        Test if the Reddit API is called correctly.
        """
        # Setup
        mock_reddit = MagicMock()
        mock_praw.Reddit.return_value = mock_reddit
        mock_reddit.subreddit().new.return_value = iter([])

        # Execute
        fetch_reddit_data_and_create_db.fetch_data_and_create_db()

        # Assert
        mock_praw.Reddit.assert_called_once_with(
            client_id="nkz3_hdkPvfyLdA3USbrSg",
            client_secret="joCDWyS5B5yBOKGZyBYdPKuwAyc_JA",
            user_agent="Living_Entire",
        )
        mock_reddit.subreddit.assert_called()
        mock_reddit.subreddit().new.assert_called()

    @patch('fetch_reddit_data_and_create_db.sqlite3')
    def test_database_creation(self, mock_sqlite3):
        """
        Test if the database is created and tables are set up correctly.
        """
        # Setup
        mock_connection = mock_sqlite3.connect.return_value
        mock_cursor = mock_connection.cursor.return_value

        # Execute
        fetch_reddit_data_and_create_db.fetch_data_and_create_db()

        # Assert
        mock_sqlite3.connect.assert_called()
        mock_cursor.execute.assert_called()
        mock_connection.commit.assert_called()
        mock_connection.close.assert_called()

if __name__ == '__main__':
    unittest.main()
