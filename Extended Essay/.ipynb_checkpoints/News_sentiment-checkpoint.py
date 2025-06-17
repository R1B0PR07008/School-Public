import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Generate simulated news sentiment data for 30 days
dates = pd.date_range(start='2025-04-08', periods=30)
sentiments = np.random.normal(loc=0.5, scale=0.2, size=30)  # Mean 0.5 (slightly positive), std dev 0.2

df = pd.DataFrame({
    'date': dates,
    'sentiment_score': sentiments,
    'absolute_sentiment': np.abs(sentiments),
    'sentiment_category': pd.cut(
        sentiments,
        bins=[-float('inf'), 0, 0.3, float('inf')],
        labels=['negative', 'neutral', 'positive']
    )
})

# Calculate key statistics
stats = df['sentiment_score'].describe()
print("\nSentiment Statistics:")
print(stats)

# Set up the plotting style
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(15, 10))

# 1. Sentiment Score Distribution
plt.subplot(2, 2, 1)
sns.histplot(data=df, x='sentiment_score', bins=20, kde=True)
plt.title('Distribution of Daily News Sentiment Scores')
plt.xlabel('Sentiment Score (-1 to 1)')
plt.ylabel('Frequency')

# 2. Daily Sentiment Trend
plt.subplot(2, 2, 2)
plt.plot(df['date'], df['sentiment_score'], marker='o', linestyle='-', linewidth=1, markersize=4)
plt.title('Daily News Sentiment Trend')
plt.xticks(rotation=45)
plt.ylabel('Sentiment Score')

# 3. Sentiment Categories
plt.subplot(2, 2, 3)
category_counts = df['sentiment_category'].value_counts()
colors = {'negative': 'red', 'neutral': 'gray', 'positive': 'green'}
category_counts.plot(kind='pie', autopct='%1.1f%%', colors=[colors[c] for c in category_counts.index])
plt.title('Sentiment Category Distribution')

# 4. Absolute Sentiment Intensity
plt.subplot(2, 2, 4)
df['absolute_sentiment'].rolling(window=3).mean().plot(marker='o', linestyle='-', linewidth=1, markersize=4)
plt.title('Moving Average of Absolute Sentiment Intensity')
plt.xticks(rotation=45)
plt.ylabel('Absolute Sentiment')

plt.tight_layout()
plt.show()

# Calculate additional quantitative metrics
print("\nQuantitative Metrics:")
print(f"Average absolute sentiment intensity: {df['absolute_sentiment'].mean():.3f}")
print(f"Days with positive sentiment: {(df['sentiment_category'] == 'positive').sum()}/{len(df)} ({((df['sentiment_category'] == 'positive').sum()/len(df)*100):.1f}%)")
print(f"Days with negative sentiment: {(df['sentiment_category'] == 'negative').sum()}/{len(df)} ({((df['sentiment_category'] == 'negative').sum()/len(df)*100):.1f}%)")