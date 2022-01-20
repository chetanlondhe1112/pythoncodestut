# prompting for a file namete
fname = input('Enter the file name:')
f = open(fname)
count = 0
for l in f:
    count = count+1
    print(l)
print(count)