x = ['1 jan','2 jan','3 jan','4 jan','5 jan'
        ,'6 jan','7 jan','8 jan']
y = [6,14,22,6,14,22,6,14,22,6,14,22,6,14,22,6,14,22,6,14,22,6,14,22,]

x_axis=[]
for el in x:
    for el2 in range(3):
        d=y[el2]
        el2s=str(y[el2])
        r = el + el2s
        x_axis.append(r)
print(x_axis)
print(len(x_axis))

