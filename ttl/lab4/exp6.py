class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def __add__(self, other):
        return self.make + other.make, self.model + other.model


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}, Fuel Type: {self.fuel_type}")

vehicle1 = Vehicle("Toyota", "Corolla", 2022)
vehicle2 = Vehicle("Honda", "Civic", 2023)

print("Information for Vehicle 1:")
vehicle1.display_info()
print("\nInformation for Vehicle 2:")
vehicle2.display_info()

result_make, result_model = vehicle1 + vehicle2
print("\nResult of operator overloading (make + model):", result_make, result_model)

car1 = Car("Tesla", "Model S", 2024, 4, "Electric")
car2 = Car("Ford", "Mustang", 2021, 2, "Gasoline")

print("\nInformation for Car 1:")
car1.display_info()
print("\nInformation for Car 2:")
car2.display_info()
