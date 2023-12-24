import random

class Car:
    def __init__(self, model):
        self.mileage = 0
        self.fuel = 100
        self.economy = random.randint(5, 15)  # Random fuel economy between 5 and 15
        self.color = random.choice(["Red", "Blue", "Green", "White", "Black"])
        self.model = model

    def drive(self, distance):
        required_fuel = (distance / 100) * self.economy
        if required_fuel > self.fuel:
            print(f"Not enough fuel to drive {distance} km.")
        else:
            self.fuel -= required_fuel
            self.mileage += distance
            print(f"Successfully drove {distance} km.")

    def distance_left(self):
        return (self.fuel / self.economy) * 100

    def fuel_up(self):
        self.fuel += 20
        print("Car has been refueled.")

# Step 3
cars = []

# Step 4
models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
for _ in range(10):
    model = random.choice(models)
    car = Car(model)
    cars.append(car)

# Step 4 (cont.)
for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

# Step 5
max_fuel_car = max(cars, key=lambda x: x.fuel)

# Step 6
print(f"The car with the most remaining fuel is a {max_fuel_car.color} {max_fuel_car.model}.")
print(f"Description: Model - {max_fuel_car.model}, Color - {max_fuel_car.color}, Mileage - {max_fuel_car.mileage}, Fuel - {max_fuel_car.fuel}, Economy - {max_fuel_car.economy}")
