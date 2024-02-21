import csv
import random

# Function to generate random data
def generate_data():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    data = []
    for _ in range(20):
        name = random.choice(names)
        age = random.randint(20, 60)
        city = random.choice(cities)
        data.append((name, age, city))
    return data

# Write data to CSV file
def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerows(data)

if __name__ == "__main__":
    data = generate_data()
    write_to_csv('data.csv', data)
    print("CSV file created successfully.")
