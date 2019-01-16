from pprint import pprint
import json

with open('redcars.json', 'r') as f:
	red_cars = json_load(f)


red_cars_by_make = {}
for car in red_cars:
    make = car['make']
    if make in red_cars_by_make:
        red_cars_by_make[make].append(car)
    else:
        red_cars_by_make[make] = [car]

pprint(red_cars_by_make)