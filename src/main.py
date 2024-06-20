import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
from lyrics import Lyrics

# Example sentiment analysis using NLTK's Vader
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['compound']


sid = SentimentIntensityAnalyzer()

# Perform sentiment analysis and update the dictionary with sentiment scores
for key, text in Lyrics.items():
    scores = sid.polarity_scores(text)
    Lyrics[key] = {
        'text': text,
        'sentiment_scores': scores,
        'sentiment_label': 'positive' if scores['compound'] > 0 else 'negative' if scores['compound'] < 0 else 'neutral'
    }


# Function to find key with closest sentiment score
def closest_sentiment(dict_obj, given_score):
    closest_key = None
    closest_difference = float('inf')  # Initialize with a large number
    
    for key, value in dict_obj.items():
        sentiment_score = value['sentiment_scores']['compound']
        difference = abs(sentiment_score - given_score)
        
        if difference < closest_difference:
            closest_difference = difference
            closest_key = key
    
    return closest_key

# Example usage:
if __name__ == "__main__":
    # Replace with user input or predefined sentiment
    user_sentiment_text = input("How are you feeling?\n")
    user_sentiment_score = analyze_sentiment(user_sentiment_text)
    
    song = closest_sentiment(Lyrics,user_sentiment_score)
    print(f"You should listen to {song}")
