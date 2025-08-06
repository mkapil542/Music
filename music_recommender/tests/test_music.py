"""
test_music.py - Unit tests for music recommender
"""

import unittest
from src.music import MusicRecommender

class TestMusicRecommender(unittest.TestCase):
    def test_happy_tracks(self):
        recommender = MusicRecommender()
        tracks = recommender.recommend(["happy"])
        self.assertTrue(any("Pharrell Williams" in t for t in tracks))
    def test_neutral_tracks(self):
        recommender = MusicRecommender()
        tracks = recommender.recommend(["neutral"])
        self.assertTrue(any("Beatles" in t for t in tracks))

if __name__ == "__main__":
    unittest.main()
