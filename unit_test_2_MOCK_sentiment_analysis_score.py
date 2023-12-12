import unittest
from unittest.mock import Mock, patch
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sqlite3
import data_analysis_and_machine_learning as daml  # assuming the function is in this module

class TestCalculateAverageSentiment(unittest.TestCase):
    @patch.object(sqlite3, 'connect')
    @patch.object(SentimentIntensityAnalyzer, 'polarity_scores')
    def test_calculate_average_sentiment(self, mock_polarity_scores, mock_connect):
        # Mock the database connection and cursor
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('post1',), ('post2',), ('post3',)]

        # Mock the sentiment analyzer
        mock_sia = Mock()
        mock_sia.polarity_scores.return_value = {'compound': 0.5}
        daml.SentimentIntensityAnalyzer = Mock(return_value=mock_sia)

        # Call the function and assert the result
        result = daml.calculate_average_sentiment('dummy_db')
        self.assertEqual(result, 75.0)

if __name__ == '__main__':
    unittest.main()