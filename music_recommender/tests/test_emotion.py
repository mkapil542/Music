"""
test_emotion.py - Unit tests for emotion detection
"""

import unittest
from src.emotion import EmotionDetector

class TestEmotionDetector(unittest.TestCase):
    def test_happy(self):
        detector = EmotionDetector()
        self.assertIn("happy", detector.detect("I am feeling very happy today!"))
    def test_sad(self):
        detector = EmotionDetector()
        self.assertIn("sad", detector.detect("I am so sad and down."))
    def test_neutral(self):
        detector = EmotionDetector()
        self.assertIn("neutral", detector.detect("I am just here."))

if __name__ == "__main__":
    unittest.main()
