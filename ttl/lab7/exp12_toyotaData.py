import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Toyota.csv')

data.replace({'??': pd.NA, '????': pd.NA}, inplace=True)

numCols = ['Price', 'Age', 'KM', 'HP', 'MetColor', 'Automatic', 'CC', 'Doors', 'Weight']
data[numCols] = data[numCols].apply(pd.to_numeric, errors='coerce')

print("Head of the DataFrame:")
print(data.head())

print("Tail of the DataFrame:")
print(data.tail())

print("\nSelecting a single column:")
print(data['Price'])

print("\nFilter data based on conditions:")
print(data[data['Price'] > 20000])

print("\nMissing values:")
print(data.isnull().sum())

grpData = data.groupby('FuelType').mean()
print("\nGrouped DataFrame:")
print(grpData)

data.boxplot(column=numCols[:4], figsize=(10, 8), notch=True, vert=False, patch_artist=True)
plt.title('Boxplot Analysis for Toyota Dataset')
plt.xlabel('Values')
plt.ylabel('Features')
plt.show()

