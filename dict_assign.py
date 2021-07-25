fname=input('Enter file')
if len(fname)<1:fname='file.txt'
hand=open(fname)
di=dict
for lin in hand:
    lin=lin.rstrip()
    wds=lin.split()
    for w in wds:
        di[w]=di.get(w,0)+1
largest=-1
theword=none
for k,v in di.items():
    print(k,v)
    if v>largets:
        largets=v
        theword=k
print('Done',theword,largest)
