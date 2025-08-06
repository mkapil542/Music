"""
emotion.py - Simple emotion detection from text
"""

from typing import List

class EmotionDetector:
    """Detects emotion from text input."""
    EMOTION_KEYWORDS = {
        "happy": ["happy", "joy", "excited", "glad"],
        "sad": ["sad", "down", "unhappy", "depressed"],
        "angry": ["angry", "mad", "furious", "irritated"],
        "relaxed": ["relaxed", "calm", "peaceful", "chill"]
    }

    def detect(self, text: str) -> List[str]:
        text = text.lower()
        detected = [emotion for emotion, keywords in self.EMOTION_KEYWORDS.items() if any(word in text for word in keywords)]
        return detected if detected else ["neutral"]
