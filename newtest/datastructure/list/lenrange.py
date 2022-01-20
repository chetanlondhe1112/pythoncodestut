# Len()function:List length
# len() function takes a list as a parameters and returns numbers of elements in list
greet = 'hello bob'
print(len(greet))

x = [2,5,7,4,9,8]
print(len(x))


# Range Function
# the range function returns a list of numbers that range from zero to one less than the parameters
print(range(4))

# looping
students = ['chetan', 'ketan', 'alisha', 'priyanka']
for s in students:
    print('Hello', s)
for l in range(len(students)):
    print('hello', students[l])
