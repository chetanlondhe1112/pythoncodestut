# counting lines in files
f = open("text.txt", "r")
count = 0
for l in f:
    count = count+1
print('count:', count)
