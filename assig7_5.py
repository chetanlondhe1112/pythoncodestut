num=0
total=0
while True:
    x=input('enter the number:')
    try:
        ix=int(x)
    except:
        print('invalid')
    if x=='exit':
        break
    num=num+1
    total=total+ix
print(total,num,total/num)
