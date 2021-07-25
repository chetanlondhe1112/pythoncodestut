s="from chetanlondhe1112@gmail.com"
atpos=s.find('@')
print(atpos)
sppos=s.find(' ',atpos)
print(sppos)
host=s[atpos+1:sppos]
print(host)
