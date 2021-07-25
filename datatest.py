count=0
sum=0
while True:
    x=input("enter the number:")
    if x=="done":
        break
    xc=float(x)
    count=count+1
    sum=sum+xc
print('sum:',sum)
print('average:',sum/count)
