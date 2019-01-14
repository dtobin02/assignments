# Reading a text file
with open('myfile.txt') as f:
    full_text = f.read()

print(full_text)

# Writing a text file
with open('testwrite.txt', 'w') as f:
    f.write('hello')
    f.write('\n')

 