import json
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score

# Step 1: Load the Processed Data
json_file_path = 'D:/AIUB/Sentiment Analysis Research/JSON/TFIDF Hotel Reviews.json'  # Replace with your JSON file path

# Load the JSON data
with open(json_file_path, 'r') as json_file:
    tfidf_data = json.load(json_file)

# Convert the list of dictionaries to a numpy array (matrix)
# Note: This assumes that all documents have the same set of features (consistent TF-IDF processing)
tfidf_matrix = np.array([[doc.get(word, 0) for word in tfidf_data[0].keys()] for doc in tfidf_data])

# Step 2: Prepare the Data for Splitting
# Assuming you have labels (e.g., positive/negative sentiment) stored separately
# Replace `labels` with your actual labels array or list
labels = np.array([1 if i < len(tfidf_data)//2 else 0 for i in range(len(tfidf_data))])  # Example labels

# Step 3: Split the Data
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, labels, test_size=0.2, random_state=42)

# Optional: Check the shapes of the splits to confirm the operation
print(f"Training data shape: {X_train.shape}, Training labels shape: {y_train.shape}")
print(f"Testing data shape: {X_test.shape}, Testing labels shape: {y_test.shape}")

# Step 4: Train the Model
# Initialize the Logistic Regression model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Step 5: Evaluate the Model
# Predict on the test data
y_pred = model.predict(X_test)

# Step 6: Analyze the Results
# Calculate accuracy, precision, recall, f1 score
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')


print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Generate a classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Generate a confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Assuming 'model' is your trained model
model_file_path = 'D:/AIUB/Sentiment Analysis Research/Models/sentiment_model_zero.pkl'

# Save the model to disk
joblib.dump(model, model_file_path)
print(f"Model saved to {model_file_path}")