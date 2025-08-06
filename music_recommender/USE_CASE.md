# Use Case Document: AI-Powered Emotion-Based Music Recommender

## Overview
This application uses AI to detect emotions from user text input and recommends music tracks that match the detected emotion and preferred language. It is designed for personal use, music streaming platforms, and mental wellness apps.

## Actors
- **User:** Provides mood or feeling as text input and selects preferred song language.
- **System:** Detects emotion, recommends music, and displays results.

## Main Use Case: Personalized Music Recommendation
### 1. User Interaction
- User launches the app.
- User enters a description of their mood or feeling (e.g., "I am feeling happy today!").
- User selects a song language (English/Hindi).

### 2. Emotion Detection
- System analyzes the input text to detect one or more emotions (happy, sad, angry, relaxed, neutral).

### 3. Music Recommendation
- System recommends a list of music tracks that match the detected emotion and selected language.
- System displays the recommended tracks to the user.

### 4. Example Scenario
- User input: "I am feeling sad."
- Language: Hindi
- System detects emotion: sad
- System recommends: "Channa Mereya - Ae Dil Hai Mushkil", "Tadap Tadap - Hum Dil De Chuke Sanam"

## Extensions
- If no emotion is detected, system defaults to "neutral" recommendations.
- If an invalid language is entered, system defaults to English.

## Benefits
- Personalized music experience
- Supports multiple languages
- Can be integrated into music streaming or wellness platforms

## Future Enhancements
- Add more languages and songs
- Integrate advanced NLP for emotion detection
- Connect to real music APIs (Spotify, YouTube)
- Add user feedback for recommendations
