purse=dict()
line=input('Enter a line\n')
word=line.split()

print(word)

for wor in word:
    purse[wor]=purse.get(wor,0) + 1
print('counts',purse)
