from pprint import pprint
import csv
import json

with open('veggies.csv', 'r') as f:
	reader = csv.DictReader(f)
	veggies = list(reader)

vegetables_by_color = {}
for veggie in veggies:
	veggie_color = veggie["color"]
	if veggie_color in vegetables_by_color:
		vegetables_by_color[veggie_color].append(veggie)
	else:
		vegetables_by_color[veggie_color] = [veggie]

pprint(vegetables_by_color)

# color count
vegetables_color_count = {}
for veggie in veggies:
	color = veggie["color"]
	if color in vegetables_color_count:
		vegetables_color_count[color] += 1
	else:
		vegetables_color_count[color] = 1

pprint(vegetables_color_count)

with open('vegetables_by_color.json', 'w') as d:
    json.dump(vegetables_by_color, d, indent=2)

