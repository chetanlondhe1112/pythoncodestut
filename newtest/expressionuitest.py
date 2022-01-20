days = input('Enter the days:')
try:
    idays = int(days)
except:
    print('Error,Please Enter the numeric input')

rpd = input('Enter the Rate per Day')
try:
    irpd = int(rpd)
except:
    print('Error,Please Enter the numeric input')

total = idays*irpd
print('Total pay is',total)