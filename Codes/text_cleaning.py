import os
import re
import openpyxl
import pandas as pd
from openpyxl import load_workbook

# Load the dataset
file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Hotel Review Data Table.xlsx'
hotel_reviews = pd.read_excel(file_path, sheet_name = 1)

# Text Cleaning
def clean_text(text):
    # remove html tags
    text = re.sub(r'<.*?>', '', text)
    # remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # convert to lowercase
    text = text.lower()
    return text

# Apply those methods
hotel_reviews ['Cleaned Reviews'] = hotel_reviews ['Review'].apply(clean_text)

# Keep only the 'Cleaned_Review' column
cleaned_reviews = hotel_reviews[['Cleaned Reviews']]

# New excel file path
new_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Cleaned Text Hotel Reviews.xlsx'

# Check if the cleaned file already exists
if not os.path.exists(new_file_path):
    # If the file does not exist, create a new Excel file and write data
    with pd.ExcelWriter(new_file_path, engine='openpyxl') as writer:
        cleaned_reviews[['Cleaned Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"New Excel file created and tokenized reviews saved to {new_file_path}")
else:
    # If the file exists, load the workbook and append the new sheet
    with pd.ExcelWriter(new_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        cleaned_reviews[['Cleaned Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"Tokenized reviews saved to an existing sheet in {new_file_path}")