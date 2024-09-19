import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'D:/AIUB/Sentiment Analysis Research/Predictions/Predicted Ascott The Residence Dhaka Hotel Reviews.xlsx'
predicted_reviews = pd.read_excel(file_path, sheet_name=0)

# Show the first few rows of the data
print(predicted_reviews.head())

sentiment_counts = predicted_reviews['Predicted Sentiment'].value_counts()
print(sentiment_counts)

# Create a bar chart
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='Blues_d')
plt.title('Sentiment Distribution of Hotel Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

