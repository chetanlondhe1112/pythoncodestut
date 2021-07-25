f=open('demotext.txt')

for l in f:
    s=l.rstrip()
    if  s.startswith('in'):
        continue
    print(s)
