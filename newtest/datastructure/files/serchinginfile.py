# searching in a file
f = open("text.txt")
for l in f:
    line = l.strip()
    if(l.startswith('I')):
        print(l)