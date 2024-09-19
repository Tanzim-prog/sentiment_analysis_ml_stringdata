import json
import numpy as np
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Load the Saved Logistic Regression Model
model_file_path = 'D:/AIUB/Sentiment Analysis Research/Models/sentiment_model_zero.pkl'
model = joblib.load(model_file_path)
print("Model loaded successfully.")

# Step 2: Load the Saved TF-IDF Vectorizer
# This is the vectorizer used to train your model
tfidf_vectorizer_file_path = 'D:/AIUB/Sentiment Analysis Research/Models/Dhaka Regency tfidf_vectorizer.pkl'
tfidf_vectorizer = joblib.load(tfidf_vectorizer_file_path)
print("TF-IDF Vectorizer loaded successfully.")

# Step 3: Load and Vectorize the New Dataset
new_reviews_file_path = 'D:/AIUB/Sentiment Analysis Research/Data Sets/Lemmatized Hotel Reviews.xlsx'
new_reviews = pd.read_excel(new_reviews_file_path, sheet_name=1)  # Load the new dataset

# Assuming the new dataset has a 'Cleaned Reviews' column
tfidf_matrix_new = tfidf_vectorizer.transform(new_reviews['Lemmatized Reviews'])  # Use transform, not fit_transform

# Convert the TF-IDF matrix to an array
tfidf_array_new = tfidf_matrix_new.toarray()
print("New data vectorized successfully.")

# Step 4: Make Predictions Using the Loaded Model
predictions = model.predict(tfidf_array_new)

# Step 5: Interpret and Save Predictions
# Map predictions to sentiment labels
sentiment_labels = ['Negative', 'Positive']
predicted_sentiments = [sentiment_labels[pred] for pred in predictions]

# Save Predictions to Excel
new_reviews['Predicted Sentiment'] = predicted_sentiments
predictions_file_path = 'D:/AIUB/Sentiment Analysis Research/Predictions/Predicted Ascott The Residence Dhaka Hotel Reviews.xlsx'
new_reviews[['Predicted Sentiment']].to_excel(predictions_file_path, index=False)

print(f"Predicted sentiments saved to {predictions_file_path}")
