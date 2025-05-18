import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('netflix_content_2023.csv')

# Clean Hours Viewed
df['Hours Viewed'] = df['Hours Viewed'].str.replace(',', '', regex=False).astype(np.int64)

# Convert Release Date
df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')
df['Release Month'] = df['Release Date'].dt.month
df['Release Day'] = df['Release Date'].dt.day_name()
df['Release Season'] = df['Release Month'].map({
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Fall', 10: 'Fall', 11: 'Fall'
})

# Set style
sns.set(style='whitegrid')

# Plot 1: Content Type Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Content Type', palette='Set2', hue='Content Type', legend=False)
plt.title('Content Type Distribution')
plt.tight_layout()
plt.show()

# Plot 2: Top 10 Most Watched Titles
top10 = df.sort_values('Hours Viewed', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top10, y='Title', x='Hours Viewed', palette='magma')
plt.title('Top 10 Most Watched Netflix Titles (2023)')
plt.tight_layout()
plt.show()

# Plot 3: Viewership by Season
seasonal = df.groupby('Release Season')['Hours Viewed'].sum().reindex(['Winter', 'Spring', 'Summer', 'Fall'])
seasonal.plot(kind='bar', color='skyblue', title='Viewership by Release Season')
plt.ylabel('Hours Viewed')
plt.tight_layout()
plt.show()

# Plot 4: Top 10 Languages by Viewership
top_langs = df.groupby('Language Indicator')['Hours Viewed'].sum().sort_values(ascending=False).head(10)
top_langs.plot(kind='bar', color='coral', title='Top 10 Languages by Viewership')
plt.ylabel('Total Hours Viewed')
plt.tight_layout()
plt.show()

# Plot 5: Content Releases by Day
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
release_day_counts = df['Release Day'].value_counts().reindex(day_order)
release_day_counts.plot(kind='bar', color='mediumseagreen', title='Content Releases by Day')
plt.ylabel('Number of Releases')
plt.tight_layout()
plt.show()
plt.savefig('assets/plot1_content_type.png')
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Content Type', palette='Set2', hue='Content Type', legend=False)
plt.title('Content Type Distribution')
plt.tight_layout()
plt.savefig('assets/plot1_content_type.png')  # Save the image
plt.show()
