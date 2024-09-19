import os
import nltk
import pandas as pd
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Define the paths
cleaned_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/SWR Hotel Reviews.xlsx'
lemmatized_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Lemmatized Hotel Reviews.xlsx'

# Load the cleaned reviews data from the sheet by its index (e.g., the first sheet, index=0)
cleaned_reviews = pd.read_excel(cleaned_file_path, sheet_name=1)  # Load sheet by index

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

# Check if the cleaned file already exists
if not os.path.exists(lemmatized_file_path):
    # If the file does not exist, create a new Excel file and write data
    with pd.ExcelWriter(lemmatized_file_path, engine='openpyxl') as writer:
        lemmatized_file_path[['Lemmatized Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"New Excel file created and Lemmattized Reviews saved to {lemmatized_file_path}")
else:
    # If the file exists, load the workbook and append the new sheet
    with pd.ExcelWriter(lemmatized_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        cleaned_reviews[['Lemmatized Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"Lemmatized Reviews saved to an existing sheet in {lemmatized_file_path}")