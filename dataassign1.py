str = 'Perfect-Plan-B:0.7541'
atpos=str.find(':')
print(atpos)
x=str[atpos+1:]
print(x,type(x))
fx=float(x)
print(fx,type(fx))
