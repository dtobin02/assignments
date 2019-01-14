with open('name.txt') as f:
    my_name = f.read()

with open("hello.txt", "w") as n:
	n.write('Hello my name is ' + my_name)

with open("hello.txt") as h:
	greeting = h.read()
	print(greeting)