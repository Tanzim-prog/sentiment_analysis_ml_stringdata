import nltk
import pandas as pd
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Define the paths
cleaned_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/SWR Hotel Reviews.xlsx'
lemmatized_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Lemmatized Hotel Reviews.xlsx'

# Load the cleaned reviews data
cleaned_reviews = pd.read_excel(cleaned_file_path)

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function to perform stemming
def stem_words(tokens):
    return [stemmer.stem(word) for word in tokens]

# Function to perform lemmatization
def lemmatize_words(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

# Convert string representation of list to actual list and perform stemming or lemmatization
cleaned_reviews['Cleaned Reviews'] = cleaned_reviews['Cleaned Reviews'].apply(lambda x: eval(x))

# Choose either stemming or lemmatization
# cleaned_reviews['Stemmed Reviews'] = cleaned_reviews['Cleaned'].apply(stem_words)
cleaned_reviews['Lemmatized Reviews'] = cleaned_reviews['Cleaned Reviews'].apply(lemmatize_words)

# Save only the 'Stemmed or Lemmatized' column to the new Excel file
cleaned_reviews[['Lemmatized Reviews']].to_excel(lemmatized_file_path, index=False, sheet_name='Dhaka Regency')

print(f"Lemmatized reviews saved to {lemmatized_file_path}")