day=input('enter the days')
rpd=input('enter rate per day')
try:
    cday=int(day)
    crpd=int(rpd)
    total=crpd*cday
    print('total pay is',total)
except:
    print('Error,please enter the numeric input')
