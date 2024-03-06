import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Iris_data_sample.csv')
data.replace({'??': pd.NA, '###': pd.NA}, inplace=True)

numCol = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
data[numCol] = data[numCol].apply(pd.to_numeric, errors='coerce')

print("Head of the DataFrame:")
print(data.head())
print("Tail of the DataFrame:")
print(data.tail())

print("\nSelecting a single column:")
print(data['SepalLengthCm'])

print("\nFilter data based on conditions:")
print(data[data['SepalLengthCm'] > 5.0])

print("\nMissing values:")
print(data.isnull().sum())

groupData = data.groupby('Species').mean()
print("\nGrouped DataFrame:")
print(groupData)

# data.hist()
# plt.show()
data.boxplot(column=numCol, by='Species', figsize=(10, 8))
plt.title('Boxplot Analysis for Iris Dataset')
plt.xlabel('Features')
plt.ylabel('Values')
plt.show()