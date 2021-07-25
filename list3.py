list=['chetan','uma','shweta','dhoni',12,34,53,65,47,87]
print(list[4:])
list.append('umesh')
list.append('amruta')
list.append('namrata')
print(list)
if 53 in list:
    print('yes')
if 'dhanashri' not in list:
    print('No')

list.sort()
print(list)
