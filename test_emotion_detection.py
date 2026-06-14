import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # test 1
        test_1 = emotion_detector('I am glad this happened')
        self.assertEqual(test_1['dominant_emotion'], 'joy')

        # test 2
        test_2 = emotion_detector('I am really mad about this')
        self.assertEqual(test_2['dominant_emotion'], 'anger')

        # test 3
        test_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_3['dominant_emotion'], 'disgust')

        # test 4
        test_4 = emotion_detector('I am so sad about this')
        self.assertEqual(test_4['dominant_emotion'], 'sadness')

        # test 5
        test_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()