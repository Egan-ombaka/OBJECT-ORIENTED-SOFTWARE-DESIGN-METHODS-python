#Encapsulation is an object-oriented programming principle that restricts direct access to an object's data and methods, allowing controlled access through public methods. It helps in data hiding, ensuring that an object's internal state cannot be directly modified from outside the class.

class Car:
    def __init__(self, brand, model, year):
        # Private attributes
        self.__brand = brand
        self.__model = model
        self.__year = year

    # Getter methods
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setter methods
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    # Method to display car information
    def display_info(self):
        print(f"Car: {self.__year} {self.__brand} {self.__model}")

# Creating an object of the Car class
my_car = Car("Audi", "A6", 2024)

# Accessing and modifying attributes using getter and setter methods
print(my_car.get_brand())
my_car.set_year(2025)
my_car.display_info()