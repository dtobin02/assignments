def multiply(a, b):
	return a * b

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def divide(a, b):
	return a / b

print("I'm going to use the calculator to divide 64 and 8")
x = divide(64, 8)
print(x)

def square(a):
	return a ** 2

def cube(a):
	return a ** 3

def square_n_times(number, n):
	new_num = number
	i = 0
	while i < n:
		new_num = number ** 2
		i += 1
	return new_num