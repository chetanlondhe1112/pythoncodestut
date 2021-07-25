f=open("textfile2.txt")
#count=0
#for l in f:
    #count=count+1
    #strp=l.strip()
    #print(strp)
#print(count)
x=f.read()
#print(x)
print(x[5])
print(len(x))
count=0
for n in x:
    if n=='a':
        count=count+1
    print(n)
print(count)
