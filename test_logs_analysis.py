import unittest
from unittest.mock import patch, MagicMock
from logs_analysis import (
    get_top_three_articles,
    get_top_article_authors,
    get_days_with_more_than_one_percent_errors,
)

class TestLogAnalysis(unittest.TestCase):

    @patch('logs_analysis.run_query')
    def test_get_top_three_articles(self, mock_run_query):
        # Mock the run_query function to return a predefined result
        mock_run_query.return_value = [
            ('Article A', 100),
            ('Article B', 90),
            ('Article C', 80),
        ]

        # Call the function to be tested
        result = get_top_three_articles()

        # Assert that the function returns the expected result
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][0], 'Article A')
        self.assertEqual(result[1][0], 'Article B')
        self.assertEqual(result[2][0], 'Article C')

    @patch('logs_analysis.run_query')
    def test_get_top_article_authors(self, mock_run_query):
        # Mock the run_query function to return a predefined result
        mock_run_query.return_value = [
            ('Author X', 200),
            ('Author Y', 180),
            ('Author Z', 150),
        ]

        # Call the function to be tested
        result = get_top_article_authors()

        # Assert that the function returns the expected result
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][0], 'Author X')
        self.assertEqual(result[1][0], 'Author Y')
        self.assertEqual(result[2][0], 'Author Z')

    @patch('logs_analysis.run_query')
    def test_get_days_with_more_than_one_percent_errors(self, mock_run_query):
        # Mock the run_query function to return a predefined result
        mock_run_query.return_value = [
            ('July 1, 2024', 2.5),
            ('July 2, 2024', 1.5),
        ]

        # Call the function to be tested
        result = get_days_with_more_than_one_percent_errors()

        # Assert that the function returns the expected result
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], 'July 1, 2024')
        self.assertEqual(result[1][0], 'July 2, 2024')

if __name__ == '__main__':
    unittest.main()
