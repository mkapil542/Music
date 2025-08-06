"""
main.py - Entry point for AI-powered emotion-based music recommender
"""

from emotion import EmotionDetector
from music import MusicRecommender

def main():
    print("Welcome to the AI-powered Emotion-Based Music Recommender!")
    text = input("Describe your mood or feeling: ")
    language = input("Choose song language (english/hindi/punjabi): ").strip().lower()
    if language not in ["english", "hindi", "punjabi"]:
        print("Invalid language, defaulting to English.")
        language = "english"
    detector = EmotionDetector()
    emotions = detector.detect(text)
    print(f"Detected emotion(s): {', '.join(emotions)}")
    recommender = MusicRecommender()
    tracks = recommender.recommend(emotions, language, max_songs=10, min_songs=5)
    print("Recommended tracks:")
    for track in tracks:
        print(f"- {track}")

if __name__ == "__main__":
    main()
