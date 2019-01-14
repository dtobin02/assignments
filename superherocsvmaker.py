import json
import csv


# read json file
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

# get the members
members = superheroes['members']

# Loop through each mmember
# Save data for each mmember into csv row
for member in members:
	print(member)

	with open('members.csv', 'w') as f:
		writer = csv.writer(f)
		header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
		writer.writerow(header)
		for member in members:
			row = [ 
			member['name'], 
			member['age'], 
			member['secretIdentity'], 
			member['powers'], 
			superheroes['squadName'], 
			superheroes['homeTown'], 
			superheroes['formed'], 
			superheroes['secretBase'], 
			superheroes['active']
			]
			writer.writerow(row)
