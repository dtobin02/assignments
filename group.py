
from pprint import pprint

cars = [
    {"model": "Yaris", "make": "Toyota", "color": "red"},
    {"model": "Auris", "make": "Toyota", "color": "red"},
    {"model": "Camry", "make": "Toyota", "color": "green"},
    {"model": "Prius", "make": "Toyota", "color": "yellow"},
    {"model": "Civic", "make": "Honda", "color": "red"},
    {"model": "Model 3", "make": "Tesla", "color": "red"}
]

# Group cars by make
cars_by_make = {}
for car in cars:
    make = car['make']
    if make in cars_by_make:
        cars_by_make[make].append(car)
    else:
        cars_by_make[make] = [car]
pprint(cars_by_make)


# Count cars in each make
cars_by_make_count = {}
for car in cars:
    make = car['make']
    if make in cars_by_make_count:
        cars_by_make_count[make] += 1
    else:
        cars_by_make_count[make] = 1

pprint(cars_by_make_count)






