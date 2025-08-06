"""
music.py - Music recommendation based on emotion
"""

from typing import List

class MusicRecommender:
    """Recommends music tracks based on emotion and language."""
    MUSIC_DB = {
        "happy": {
            "english": ["Happy - Pharrell Williams", "Good Life - OneRepublic"],
            "hindi": ["Zinda - Bhaag Milkha Bhaag", "Gallan Goodiyaan - Dil Dhadakne Do"],
            "punjabi": ["Laung Laachi - Mannat Noor", "Patiala Peg - Diljit Dosanjh"]
        },
        "sad": {
            "english": ["Someone Like You - Adele", "Fix You - Coldplay"],
            "hindi": ["Channa Mereya - Ae Dil Hai Mushkil", "Tadap Tadap - Hum Dil De Chuke Sanam"],
            "punjabi": ["Soch - Hardy Sandhu", "Qismat - Ammy Virk"]
        },
        "angry": {
            "english": ["Breaking the Habit - Linkin Park", "Stronger - Kanye West"],
            "hindi": ["Bhaag DK Bose - Delhi Belly", "Malhari - Bajirao Mastani"],
            "punjabi": ["5 Taara - Diljit Dosanjh", "Jatt Da Muqabala - Sidhu Moose Wala"]
        },
        "relaxed": {
            "english": ["Weightless - Marconi Union", "Sunset Lover - Petit Biscuit"],
            "hindi": ["Ilahi - Yeh Jawaani Hai Deewani", "Safarnama - Tamasha"],
            "punjabi": ["Lamberghini - The Doorbeen", "Photo - Karan Sehmbi"]
        },
        "neutral": {
            "english": ["Let It Be - The Beatles", "Viva La Vida - Coldplay"],
            "hindi": ["Yun Hi Chala Chal - Swades", "Dil Dhadakne Do - Zindagi Na Milegi Dobara"],
            "punjabi": ["High Rated Gabru - Guru Randhawa", "Suit Suit - Guru Randhawa"]
        }
    }

    def recommend(self, emotions: List[str], language: str = "english", max_songs: int = 10, min_songs: int = 5) -> List[str]:
        tracks = []
        for emotion in emotions:
            tracks.extend(self.MUSIC_DB.get(emotion, {}).get(language, []))
        if not tracks:
            tracks = self.MUSIC_DB["neutral"][language]
        # If not enough tracks, fill with neutral songs until min_songs is reached
        while len(tracks) < min_songs:
            for song in self.MUSIC_DB["neutral"][language]:
                if song not in tracks:
                    tracks.append(song)
                if len(tracks) >= min_songs:
                    break
        return tracks[:max_songs]
