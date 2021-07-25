rawstr=input('enter a number')
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print('Nice work')
elif ival==0:
    print('its zero')
else:
    print('Not A number')
