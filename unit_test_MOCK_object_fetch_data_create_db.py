import unittest
from unittest.mock import patch, MagicMock
import os
import sqlite3
from fetch_reddit_data_and_create_db import fetch_data_and_create_db  

class TestFetchDataAndCreateDB(unittest.TestCase):
    def setUp(self):
        self.reddit_patcher = patch('praw.Reddit')
        self.sqlite3_patcher = patch('sqlite3.connect')

        self.mock_reddit = self.reddit_patcher.start()
        self.mock_sqlite3 = self.sqlite3_patcher.start()

        self.mock_reddit.return_value.subreddit.return_value.new.return_value = [MagicMock() for _ in range(1000)]
        self.mock_sqlite3.return_value.cursor.return_value.execute.return_value = None

    def test_fetch_data_and_create_db(self):
        fetch_data_and_create_db()
        self.assertTrue(os.path.isfile('lakers.db'))
        self.assertTrue(os.path.isfile('raptors.db'))
        self.assertTrue(os.path.isfile('celtics.db'))

    def tearDown(self):
        self.reddit_patcher.stop()
        self.sqlite3_patcher.stop()

if __name__ == "__main__":
    unittest.main()