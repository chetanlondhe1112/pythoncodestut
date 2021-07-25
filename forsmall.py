small=None
for i in[9,41,12,3,74,15]:
    if small is None:
        small=i
    elif i<small:
        small=i
print("smallest value:",small)
