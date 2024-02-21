import numpy as np
import csv
from collections import Counter
from scipy.spatial import distance

data = []
with open('numerical_data.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Convert string values to float/int
for row in data:
    row['Age'] = int(row['Age'])
    row['Height (cm)'] = float(row['Height (cm)'])
    row['Weight (kg)'] = float(row['Weight (kg)'])
    row['IQ Level'] = int(row['IQ Level'])

# Extract values for age, height, weight, and IQ
ages = [row['Age'] for row in data]
heights = [row['Height (cm)'] for row in data]
weights = [row['Weight (kg)'] for row in data]
iq_levels = [row['IQ Level'] for row in data]


mean_age = np.mean(ages)
mean_height = np.mean(heights)
mean_weight = np.mean(weights)
mean_iq = np.mean(iq_levels)

median_age = np.median(ages)
median_height = np.median(heights)
median_weight = np.median(weights)
median_iq = np.median(iq_levels)

mode_age = Counter(ages).most_common(1)[0][0]
mode_height = Counter(heights).most_common(1)[0][0]
mode_weight = Counter(weights).most_common(1)[0][0]
mode_iq = Counter(iq_levels).most_common(1)[0][0]

std_age = np.std(ages)
std_height = np.std(heights)
std_weight = np.std(weights)
std_iq = np.std(iq_levels)


euclidean_distance = distance.euclidean([mean_age, mean_height, mean_weight, mean_iq], [median_age, median_height, median_weight, median_iq])

manhattan_distance = distance.cityblock([mean_age, mean_height, mean_weight, mean_iq], [median_age, median_height, median_weight, median_iq])

d4_distance = distance.minkowski([mean_age, mean_height, mean_weight, mean_iq], [median_age, median_height, median_weight, median_iq], p=4)

d8_distance = distance.minkowski([mean_age, mean_height, mean_weight, mean_iq], [median_age, median_height, median_weight, median_iq], p=8)

print("Mean Age:", mean_age)
print("Mean Height:", mean_height)
print("Mean Weight:", mean_weight)
print("Mean IQ:", mean_iq)
print()
print("Median Age:", median_age)
print("Median Height:", median_height)
print("Median Weight:", median_weight)
print("Median IQ:", median_iq)
print()
print("Mode Age:", mode_age)
print("Mode Height:", mode_height)
print("Mode Weight:", mode_weight)
print("Mode IQ:", mode_iq)
print()
print("Standard Deviation Age:", std_age)
print("Standard Deviation Height:", std_height)
print("Standard Deviation Weight:", std_weight)
print("Standard Deviation IQ:", std_iq)
print()
print("Euclidean Distance:", euclidean_distance)
print("Manhattan Distance:", manhattan_distance)
print("d4 Distance:", d4_distance)
print("d8 Distance:", d8_distance)
