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
print('\n')
print(d.items())
print('\n')

#print(sort(d.items()))
m=list()
k=list()
print(sorted(d.items()))
for k,v in sorted(d.items()):
    print(k,v)
    m.append((v,k))
print(m)
print(sorted([(v,k) for k,v in d.items()]))
m=sorted(m, reverse = True)
print(m)
for v,k in m:
    print(v,k)
