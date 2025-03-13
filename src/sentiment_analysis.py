import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import nltk
# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('vader_lexicon')


# Load your feedback data
df = pd.read_csv('/Users/amarnathgowda/Desktop/pojects/Pulse/data/preprocessed_feedback.csv')  # Use 'sample_feedback.csv' if skipping preprocessing

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Function to get sentiment scores
def get_sentiment_scores(text):
    return sia.polarity_scores(text)

# Apply sentiment analysis (use 'cleaned_feedback' or 'feedback' depending on your file)
df['sentiment_scores'] = df['cleaned_feedback'].apply(get_sentiment_scores)  # For preprocessed data
# OR: df['sentiment_scores'] = df['feedback'].apply(get_sentiment_scores)  # For original data

# Extract the compound score (ranges from -1 to 1)
df['compound'] = df['sentiment_scores'].apply(lambda x: x['compound'])

# Classify sentiment based on compound score
df['sentiment'] = df['compound'].apply(lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral'))

# Save the updated data to a new file
df.to_csv('feedback_with_sentiment.csv', index=False)

# Check the first few rows to confirm
print(df[['date', 'feedback', 'compound', 'sentiment']].head())