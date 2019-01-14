import csv

# write csv
with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['col1', 'col2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])


# read csv
from pprint import pprint
with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    pprint(row)