import pandas as pd

# Load the data
df = pd.read_csv('data/feedback_with_sentiment.csv')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Set date as index
df.set_index('date', inplace=True)

# Group by month and aggregate
monthly_sentiment = df.resample('W').agg({
    'compound': 'mean',
    'sentiment': lambda x: x.value_counts().to_dict()
})

# Extract sentiment counts
monthly_sentiment['positive_count'] = monthly_sentiment['sentiment'].apply(lambda x: x.get('positive', 0))
monthly_sentiment['negative_count'] = monthly_sentiment['sentiment'].apply(lambda x: x.get('negative', 0))
monthly_sentiment['neutral_count'] = monthly_sentiment['sentiment'].apply(lambda x: x.get('neutral', 0))

# Drop the sentiment dictionary column
monthly_sentiment.drop(columns=['sentiment'], inplace=True)

# Save to CSV
monthly_sentiment.to_csv('data/aggregated_sentiment.csv')
print("Aggregated data saved to 'data/aggregated_sentiment.csv'")