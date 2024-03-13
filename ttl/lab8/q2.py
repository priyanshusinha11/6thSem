import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('people_dataset.csv')

# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Age', y='IQ', data=df)
plt.title('Bar Plot: Age vs. IQ')
plt.xlabel('Age')
plt.ylabel('Mean IQ')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='IQ', bins=20, kde=True)
plt.title('Histogram of IQ')
plt.xlabel('IQ')
plt.ylabel('Frequency')
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age', y='IQ', data=df)
plt.title('Boxplot: Age vs. IQ')
plt.xlabel('Age')
plt.ylabel('IQ')
plt.show()

# Heatmap
heatmap_data = df.pivot_table(index='Age', columns='IQ', aggfunc='size')
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap='coolwarm')
plt.title('Heatmap: Age vs. IQ')
plt.xlabel('IQ')
plt.ylabel('Age')
plt.show()
