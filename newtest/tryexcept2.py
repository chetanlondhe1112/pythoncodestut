num = input("Enter a number")
try:
    ival = int(num)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not A Number')
