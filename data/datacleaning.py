import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the data
df = pd.read_csv('sample_feedback.csv')

# Define preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    cleaned_text = ' '.join(tokens)
    return cleaned_text

# Apply preprocessing
df['cleaned_feedback'] = df['feedback'].apply(preprocess_text)

# Save to new CSV
df.to_csv('preprocessed_feedback.csv', index=False)

# Verify
print(df.head())