def computetotalpay(days,rate):
    total = days*rate
    return total
x = float(input("enter days:"))
y = float(input("enter rate:"))
print("pay:",computetotalpay(x,y))
