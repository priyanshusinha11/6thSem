import numpy as np
import csv
from faker import Faker
import random
fake = Faker()

data = []
for _ in range(20):
    name = fake.name()
    age = random.randint(18, 80)  # Age between 18 and 80
    height = round(random.uniform(150, 200), 2)  # Height in centimeters
    weight = round(random.uniform(50, 120), 2)   # Weight in kilograms
    iq_level = random.randint(70, 150)  # IQ level between 70 and 150
    data.append([name, age, height, weight, iq_level])

# Write the data to a CSV file
with open('numerical_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Height (cm)', 'Weight (kg)', 'IQ Level'])
    writer.writerows(data)
