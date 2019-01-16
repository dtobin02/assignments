import csv
reader = csv.reader(open(r"veggies.csv"),delimiter=' ')
filtered = filter(lambda veggies: 'green' == veggies, reader)
csv.writer(open(r"green_veggies2.csv",'w'),delimiter=' ').writerows(filtered)

