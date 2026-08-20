class Vehicle:
    def __init__(self,model,fuel_type,price):
        self.model = model
        self.fuel_type = fuel_type
        self.__price = price

    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return(self.__price)

    def show_vehicle(self):
        print(f"Model: {self.model} Fuel Type: {self.fuel_type} Price: {self.__price}")

class Car(Vehicle):
    def show_car(self):
        print("Type: Car")

class LuxuryCar(Car):
    def show_luxury(self):
        print("Category: Luxury Car")

class Bike(Vehicle):
    def show_bike(self):
        print("Type: Bike")

class Truck(Vehicle):
    def show_truck(self):
        print("Type: Truck")

class GPS:
    def show_gps(self):
        print("GPS: Available")

class SmartCar(Vehicle,GPS):
    def show_smart_car(self):
        print("Type: Smart Car")

class Smartluxurycar(LuxuryCar,GPS):
    def show_smart_luxury(self):
        print("Type: Smart Luxury Car")


# Single Inheritance
print("-------Single Inheritance--------")
car = Car("Toyota","Petrol",1200000)
car.show_vehicle()
car.show_car()

# Multiple Inheritance
print("-------Multiple Inheritance-------")
luxury =LuxuryCar("BMW","Petrol",5500000)
luxury.show_vehicle()
luxury.show_car()
luxury.show_luxury()

# Hierarchical Inheritance
print("-------Hierarchical Inheritance-------")
bike = Bike("Honda Shine","Petrol",85000)
bike.show_vehicle()
bike.show_bike()

truck = Truck("Tata 407","Diesal",900000)
truck.show_vehicle()
truck.show_truck()

# Multiple Inheritance
print("--------Multiple Inheritance-------")
smart = SmartCar("TeslaModel 3","Electric",4500000)
smart.show_vehicle()
smart.show_gps()
smart.show_smart_car()

# Hybrid Inheritance
print("-------Hybrid Inheritance-------")
smart_luxury = Smartluxurycar("Mercedes EQS",  "Electric", 150000000)
smart_luxury.show_vehicle()
smart_luxury.show_car()
smart_luxury.show_luxury()
smart_luxury.show_gps()
smart_luxury.show_smart_luxury()


print("Old Price:", smart_luxury.get_price())
smart_luxury.set_price(16000000)
print("Updated Price:", smart_luxury.get_price())


print("Vehicle")
