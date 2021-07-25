num = 0
sum = 0.0
while True:
    val = input("Enter a number: ")
    if val == 'exit':
        break
        try:
            fval = float(val)
        except:
            print('Invalid')
            continue
            num = num + 1
            sum = sum + fval

print(sum,num,sum/num)
