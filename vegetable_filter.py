

# vegetables try it
import csv
green_veggies = []
with open('veggies.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	for row in rows:
		if row["color"] == "green":
			print(row)

#
# print(green_veggies)
# with open('green_veggies.csv', 'w') as d:
# 		writer = csv.writer(d)
# 		writer.writerow(['name', 'color'])

with open('green_veggies.csv', 'w') as d:
    writer = csv.writer(d)
    writer.writerow(['name', 'color'])
    for row in rows:
    	if row['color'] == "green":
    		writer.writerow([row['name'], row['color']])

# alternatively
import json
with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

green_veggies = []
whitelist = ['green']
for row in rows: 
    if row['color'] in whitelist:
        green_veggies.append(row)

print(json.dumps(green_veggies, indent=2))

# Write to JSON file
with open('greenvegetables.json', 'w') as f:
    json.dump(green_veggies, f, indent=2)

    # writer.writerow(['val1', 'val2'])
    # writer.writerow(['val1', 'val2'])
    # writer.writerow(['val1', 'val2'])
# write to CSV
with open('greenveggies3.csv', 'w') as x:
    writer = csv.writer(x)
    writer.writerow(['name', 'color'])
    for veggie in green_veggies:
        writer.writerow([veggie["name"], veggie["color"]])



