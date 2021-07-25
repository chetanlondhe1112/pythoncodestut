name=input('enter file name')
f=open(name)
for l in f:
    s=l.strip()
    print(s)
