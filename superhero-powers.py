# load libraries
import json
import csv

# read json file
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

print(superheroes)
# get the members
members = superheroes['members']

data = []
# loop through each member
for member in members:
	powers = member['powers']

# foreach member get list of powers
	for power in powers:
		print(power)
		data.append(power)

unique_powers = list(set(data))
print(unique_powers)
#  loop through powers and print each one