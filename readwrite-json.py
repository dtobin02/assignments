# read json
from pprint import pprint
import json

with open('superheroes.json', 'r') as f:
    data = json.load(f)

pprint(data)

# write json
import json

rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('friends.json', 'w') as f:
    json.dump(rows, f, indent=2)
    # data and file you will dump to
