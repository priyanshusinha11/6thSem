import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

df[['First Name', 'Last Name']] = df['Name'].str.split(' ', expand=True)

groupedData = df[(df['Gender'] == 'M') & (df['Age'] > 30) & (df['Salary'] > 500000)]

percentage = groupedData.groupby('City').size() / df[df['Gender'] == 'M'].groupby('City').size() * 100

# Plot
percentage.plot(kind='bar', color='skyblue')
plt.title('Percentage of Male Employees (Age > 30 and Salary > 500,000) by City')
plt.xlabel('City')
plt.ylabel('Percentage')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
