import pandas as pd

# Sample Data for Sentiment Analysis
data = {
    "text": ["I love this product!", "This is terrible!", "It is okay, not great."],
    "sentiment": ["positive", "negative", "neutral"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as an Excel file
df.to_excel("C:/Users/SIRI LASYA/OneDrive/Desktop/projects/sentiment_dataset.xlsx", index=False)

print("Excel file 'sentiment_dataset.xlsx' created successfully!")