while True:
    line=input('Enter>>> ')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print("DONE!")
