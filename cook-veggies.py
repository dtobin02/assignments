import csv
import json

# read veggies.csv into var called "vegetables"
with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

# print varaible vegetables
# print(vegetables)

# save to json as vegetables.json
with open('cookedvegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=2)
