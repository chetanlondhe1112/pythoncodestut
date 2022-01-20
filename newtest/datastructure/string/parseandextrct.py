#from jyotichutani@gmail.com sat jan 519
data = 'from jyotichutani@gmail.com sat jan 519'
atpos = data.find('@')
print(atpos)
stops = data.find(' ', atpos)
print(stops)
host = data[atpos+1:stops]
print(host)


