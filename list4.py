x=list([])
while True:
    y=input('enter the number:')
    if y=="done":
        break
    no=float(y)
    x.append(no)
total=sum(x)
avg=total/len(x)
print('sum=',total)
print('average=',avg)
