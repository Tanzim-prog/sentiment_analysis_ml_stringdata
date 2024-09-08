import re
import openpyxl
import pandas as pd

# Load the dataset

file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Hotel Review Data Table.xlsx'
hotel_reviews = pd.read_excel(file_path, sheet_name = 0)

print(hotel_reviews.head())

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

# New Excel file path
new_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Cleaned Text Hotel Reviews.xlsx'

# Save the cleaned reviews dataframe
cleaned_reviews.to_excel(new_file_path, index=False, sheet_name='Dhaka Regency')

print(f"Cleaned Text saved to {new_file_path}")