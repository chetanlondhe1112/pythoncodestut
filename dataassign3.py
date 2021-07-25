z=list([])
f=open('assign3.txt')
for l in f:
    x=l.split('@')
    x2=x[1]
    x3=x2.split()
    z.append(x3[1])
for i in z:
    print(i)
