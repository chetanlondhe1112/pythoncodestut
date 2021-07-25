h=input('enter the file:')
f=open(h)
for x in f:
    print(x)
d=dict()
sp=x.split()
print(sp)
for el in sp:
    d[el]=d.get(el,0)+1
print(d)
print(d.items())
#print(sort(d.items()))
