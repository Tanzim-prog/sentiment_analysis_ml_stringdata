import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
#nltk.download('punkt_tab')

# Define Path
cleanedtext_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Cleaned Text Hotel Reviews.xlsx'
tokenized_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Tokenized Hotel Reviews.xlsx'

# Load the cleaned reviews data
cleaned_reviews = pd.read_excel(cleanedtext_file_path)

# Tokenize the cleaned reviews
cleaned_reviews['Tokenized Reviews'] = cleaned_reviews['Cleaned Reviews'].apply(word_tokenize)

# Save file
cleaned_reviews[['Tokenized Reviews']].to_excel(tokenized_file_path, index=False, sheet_name='Dhaka Regency')

print(f"Tokenized saved to {tokenized_file_path}")