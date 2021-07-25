c={'a':10,'b':1,'c':22}
tmp=list()
tmp1=list()
print(c)
for k,v in c.items():
    tmp.append((k,v))
print(tmp)
print(sorted(tmp))
rev=sorted(tmp,reverse=True)
print(rev)
print(sorted([(v,k) for k,v in c.items()]))
for k,v in c.items():
    tmp1.append((v,k))
print(tmp1)
print(sorted(tmp1))
rev1=sorted(tmp1,reverse=True)
print(rev1)
print(sorted([(v,k) for k,v in c.items()]))
