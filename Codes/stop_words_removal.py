import os
import nltk
import pandas as pd
from nltk.corpus import stopwords

# Define Path
tokenized_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Tokenized Hotel Reviews.xlsx'
cleaned_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/SWR Hotel Reviews.xlsx'

# Load the tokenized reviews data from the sheet by its index (e.g., the first sheet, index=0)
cleaned_reviews = pd.read_excel(tokenized_file_path, sheet_name=1)  # Load sheet by index

# Stop Words Removal function
stop_words = set(stopwords.words('english'))
def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

# Convert string representation of list to actual list and remove stopwords
cleaned_reviews['Cleaned Reviews'] = cleaned_reviews['Tokenized Reviews'].apply(lambda x: eval(x))
cleaned_reviews['Cleaned Reviews'] = cleaned_reviews['Cleaned Reviews'].apply(remove_stopwords)

# Check if the cleaned file already exists
if not os.path.exists(cleaned_file_path):
    # If the file does not exist, create a new Excel file and write data
    with pd.ExcelWriter(cleaned_file_path, engine='openpyxl') as writer:
        cleaned_file_path[['Cleaned Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"New Excel file created and Cleaned Reviews saved to {cleaned_file_path}")
else:
    # If the file exists, load the workbook and append the new sheet
    with pd.ExcelWriter(cleaned_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        cleaned_reviews[['Cleaned Reviews']].to_excel(writer, index=False, sheet_name='Ascott The Residence Dhaka')
    print(f"Cleaned Reviews saved to an existing sheet in {cleaned_file_path}")