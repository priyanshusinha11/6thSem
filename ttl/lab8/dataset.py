import csv
import random

# Function to generate random IQ level based on age group
def generate_iq(age):
    if age < 20:
        return random.randint(70, 120)
    elif age < 40:
        return random.randint(80, 130)
    elif age < 60:
        return random.randint(85, 135)
    else:
        return random.randint(70, 120)

# Function to generate dataset
def generate_dataset(num_people):
    with open('people_dataset.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age', 'IQ']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for _ in range(num_people):
            name = f'Person{_+1}'
            age = random.randint(10, 80)
            iq = generate_iq(age)
            writer.writerow({'Name': name, 'Age': age, 'IQ': iq})

# Generate dataset with 100 people
generate_dataset(100)
print("Dataset created successfully as 'people_dataset.csv'")
