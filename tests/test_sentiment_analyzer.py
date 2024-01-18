import unittest

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        sentiment_positive = sentiment_analyzer("I love working with Python")
        sentiment_negative = sentiment_analyzer("I hate working with Python")
        sentiment_neutral = sentiment_analyzer("I am neutral on Python")

        self.assertEqual(sentiment_positive['label'], 'SENT_POSITIVE')
        self.assertEqual(sentiment_negative['label'], 'SENT_NEGATIVE')
        self.assertEqual(sentiment_neutral['label'], 'SENT_NEUTRAL')

if __name__ == '__main__':
    unittest.main()
