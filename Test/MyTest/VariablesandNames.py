cars = 100
space_in_car = 4.0
driver = 30
passengers = 90
cars_not_driven = cars-driver
cars_driven = driver
carpool_capactiy = cars_driven * space_in_car
average_passengers_per_Car = passengers/cars_driven


print ("there are", cars, "cars availabe")
print("there are only", driver, "drivers available")
print("there will be", cars_not_driven, "empty cars")
print("we can transport", carpool_capactiy, "to carpool today")
print("we have", passengers, "to carpool today")
print("we need to put about", average_passengers_per_Car, "in each car.")