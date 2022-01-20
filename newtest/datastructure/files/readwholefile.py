# we can read the whole file(newlines and all) into a single string
f = open('text.txt')
input = f.read()
print(len(input))
print(input[:20])
#first 20 char

