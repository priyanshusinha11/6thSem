import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('people_dataset.csv')

#Line plot
plt.figure(figsize=(10, 6))
plt.plot(df['Age'], df['IQ'], marker='o', linestyle='-')
plt.title('Age vs. IQ: Simple Line Plot')
plt.xlabel('Age')
plt.ylabel('IQ')
plt.grid(True)
plt.show()

#scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['IQ'], color='blue', alpha=0.5)
plt.title('Age vs. IQ: Scatter plot')
plt.xlabel('Age')
plt.ylabel('IQ')
plt.grid(True)
plt.show()
