#A class is blueprint of creating objects. It defines attributes and methods.

#An object is an instance of a class

# Define a class named Car
class Car:
    def __init__(self, brand, model, year):
        # Attributes
        self.brand = brand
        self.model = model
        self.year = year

    # Method/function
    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")

# Creating an object  of the Car class
my_car = Car("Audi", "A6", 2024)

# Calling the method
my_car.display_info()