import nltk
import pandas as pd
from nltk.corpus import stopwords

# Define Path
tokenized_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Tokenized Hotel Reviews.xlsx'
cleaned_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/SWR Hotel Reviews.xlsx'

# Load the tokenized reviews data
tokenized_reviews = pd.read_excel(tokenized_file_path)

stop_words = set(stopwords.words('english'))
def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

# Convert string representation of list to actual list and remove stopwords
tokenized_reviews['Cleaned Reviews'] = tokenized_reviews['Tokenized Reviews'].apply(lambda x: eval(x))
tokenized_reviews['Dhaka Regency'] = tokenized_reviews['Cleaned Reviews'].apply(remove_stopwords)

# Save only the 'Cleaned' column to the new Excel file
tokenized_reviews[['Cleaned Reviews']].to_excel(cleaned_file_path, index=False, sheet_name='Dhaka Regency')

print(f"Stop Words Removed saved to {cleaned_file_path}")