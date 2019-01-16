import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'length'])
	for i in vegetables:
		name = i["name"]
		color = i["color"]
		length_veggie = len(name)
		writer.writerow([name,color, length_veggie])

from pprint import pprint
with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    for row in rows:
    	if row['color'] == "green":
    		print(row)
 
	

# with open('testwrite.csv', 'w') as f:
# 		# writer = csv.writer(f)
#    	 	writer.writerow(['name', 'col2'])

# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])