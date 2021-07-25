#purse=dict()
#purse['book']=34
#purse['take']=55
#purse['make']=67
#print(purse)
t="i  you hello my world! hi i the my you name the the is you king, my i the you and hi i im my the specially designed AI from my owner chetan londhe"
#l=t.split()
#print(l)
d=dict()
for el in t:
    d[el]=d.get(el,0)+1
print(d)
#print(d.sort())
print(max(d.values()))
print(d.key(34))
