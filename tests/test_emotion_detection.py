import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionAnalysis(unittest.TestCase):
    def test_sentiment_analyzer(self): # I love this new technology
        sentiment_positive = emotion_detector("I love working with Python")
        sentiment_negative = emotion_detector("I hate working with Python")
        sentiment_neutral = emotion_detector("I am neutral on Python")

        self.assertEqual(sentiment_positive['label'], 'SENT_POSITIVE')
        self.assertEqual(sentiment_negative['label'], 'SENT_NEGATIVE')
        self.assertEqual(sentiment_neutral['label'], 'SENT_NEUTRAL')

if __name__ == '__main__':
    unittest.main()
