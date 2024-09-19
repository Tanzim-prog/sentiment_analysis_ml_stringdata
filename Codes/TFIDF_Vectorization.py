import json
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Load the Lemmatized Dataset
file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Lemmatized Hotel Reviews.xlsx'  # Replace with your file path
lemmatized_reviews = pd.read_excel(file_path, sheet_name = 1)

# Step 2: Apply TF-IDF Vectorization
# Initialize the TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Assuming the relevant column with lemmatized text is named 'Lemmatized'
tfidf_matrix = tfidf_vectorizer.fit_transform(lemmatized_reviews['Lemmatized Reviews'])

# Save the TF-IDF vectorizer for later use
vectorizer_file_path = 'D:/AIUB/Sentiment Analysis Research/Models/Ascott The Residence Dhaka tfidf_vectorizer.pkl'
joblib.dump(tfidf_vectorizer, vectorizer_file_path)

print(f"TF-IDF Vectorizer saved to {vectorizer_file_path}")

# Convert the TF-IDF matrix to an array
tfidf_array = tfidf_matrix.toarray()

# Get the feature names (i.e., words)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Step 3: Convert the TF-IDF Matrix to JSON
# Create a list of dictionaries where each dictionary corresponds to a document's TF-IDF scores
tfidf_data = []
for doc_index in range(tfidf_array.shape[0]):
    doc_tfidf = {feature_names[word_index]: tfidf_array[doc_index, word_index]
                 for word_index in range(len(feature_names))}
    tfidf_data.append(doc_tfidf)

# Convert the TF-IDF data to JSON format
tfidf_json = json.dumps(tfidf_data, indent=4)

# Step 4: Save the JSON Data to a File
json_file_path = 'D:/AIUB/Sentiment Analysis Research/JSON/TFIDF Ascott The Residence Dhaka Hotel Reviews.json'  # Replace with your desired save path
with open(json_file_path, 'w') as json_file:
    json_file.write(tfidf_json)

print(f"TF-IDF data saved to {json_file_path}")