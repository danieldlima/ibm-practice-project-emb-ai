import unittest

from EmotionDetection.emotion_detection import emotion_detector

EMOTIONS = {
    'anger': {"emotion": 'ANGER', "text": "I am really mad about this"},
    'disgust': {"emotion": 'DISGUST', "text": "I feel disgusted just hearing about this"},
    'fear': {"emotion": 'FEAR', "text": "I am really afraid that this will happen"},
    'joy': {"emotion": 'JOY', "text": "I am glad this happened"},
    'sadness': {"emotion": 'SADNESS', "text": "I am so sad about this"}
}

class TestEmotionDetection(unittest.TestCase):
    def test_sentiment_analyzer(self):
        anger = emotion_detector(EMOTIONS['anger']['text'])
        disgust = emotion_detector(EMOTIONS['disgust']['text'])
        fear = emotion_detector(EMOTIONS['fear']['text'])
        joy = emotion_detector(EMOTIONS['joy']['text'])
        sadness = emotion_detector(EMOTIONS['sadness']['text'])
        is_none = emotion_detector("")

        self.assertEqual(anger['dominant_emotion'], EMOTIONS['anger']['emotion'])
        self.assertEqual(disgust['dominant_emotion'], EMOTIONS['disgust']['emotion'])
        self.assertEqual(fear['dominant_emotion'], EMOTIONS['fear']['emotion'])
        self.assertEqual(joy['dominant_emotion'], EMOTIONS['joy']['emotion'])
        self.assertEqual(sadness['dominant_emotion'], EMOTIONS['sadness']['emotion'])
        self.assertIsNone(is_none)

if __name__ == '__main__':
    unittest.main()
