import os
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
#nltk.download('punkt_tab')

# Define Path
cleanedtext_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Cleaned Text Hotel Reviews.xlsx'
tokenized_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Tokenized Hotel Reviews.xlsx'

# Load the tokenized reviews data from the sheet by its index (e.g., the first sheet, index=0)
tokenized_reviews = pd.read_excel(cleanedtext_file_path, sheet_name=1)  # Load sheet by index

# Tokenize the cleaned reviews
tokenized_reviews['Tokenized Reviews'] = tokenized_reviews['Cleaned Reviews'].apply(word_tokenize)

# Check if the cleaned file already exists
if not os.path.exists(tokenized_file_path):
    # If the file does not exist, create a new Excel file and write data
    with pd.ExcelWriter(tokenized_file_path, engine='openpyxl') as writer:
        tokenized_reviews[['Tokenized Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"New Excel file created and tokenized reviews saved to {tokenized_file_path}")
else:
    # If the file exists, load the workbook and append the new sheet
    with pd.ExcelWriter(tokenized_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        tokenized_reviews[['Tokenized Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"Tokenized reviews saved to an existing sheet in {tokenized_file_path}")