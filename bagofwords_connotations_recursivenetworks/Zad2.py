# Import required libraries
from nltk.sentiment import SentimentIntensityAnalyzer
from text2emotion import get_emotion
import nltk


nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

positive_review = """
Great location, really pleasant and clean rooms, but the thing that makes this such a good place to stay are the staff.
All of the people are incredibly helpful and generous with their time and advice.
"""

negative_review = """
Worst hotel I've stayed in. The lock housing was exposed meaning it wasn't difficult to break into our room.
No safety deposit boxes in rooms.
"""

def analyze_with_vader(review):
    scores = sia.polarity_scores(review)
    return scores

def analyze_with_text2emotion(review):
    emotions = get_emotion(review)
    return emotions

vader_positive = analyze_with_vader(positive_review)
vader_negative = analyze_with_vader(negative_review)

t2e_positive = analyze_with_text2emotion(positive_review)
t2e_negative = analyze_with_text2emotion(negative_review)

print("Vader Analysis - Positive Review:", vader_positive)
print("Vader Analysis - Negative Review:", vader_negative)

print("\nText2Emotion Analysis - Positive Review:", t2e_positive)
print("Text2Emotion Analysis - Negative Review:", t2e_negative)

# Vader Analysis - Positive Review: {'neg': 0.0, 'neu': 0.596, 'pos': 0.404, 'compound': 0.9621}
# Vader Analysis - Negative Review: {'neg': 0.234, 'neu': 0.615, 'pos': 0.151, 'compound': -0.3999}
#
# Text2Emotion Analysis - Positive Review: {'Happy': 0.44, 'Angry': 0.11, 'Surprise': 0.0, 'Sad': 0.11, 'Fear': 0.33}
# Text2Emotion Analysis - Negative Review: {'Happy': 0.0, 'Angry': 0.17, 'Surprise': 0.17, 'Sad': 0.17, 'Fear': 0.5}

# Wyniki są zgodne z oczekiwaniami, a nawet zaskakująco prawidłowe dla Text2Emotion
