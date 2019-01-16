friends = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter to age < 37
millenials = []
for friend in friends:
    if row['age'] < 37:
        millenials.append(row)

print(millenials)

# filter whitelist
cool_people = []
whitelist = ['Rachel', 'Phoebe']
for row in rows:
    if row['name'] in whitelist:
        cool_people.append(row)

print(cool_people)


# filter blacklist names

cool_people = []
blacklist = ['Monica']
for row in rows:
    if row['name'] not in blacklist:
        cool_people.append(row)

print(cool_people)





