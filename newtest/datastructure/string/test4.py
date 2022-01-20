#string slicing
#syntax : str_object[start_pos:end_pos:step]

s = 'hello world'
first_five_char = s[:5]
print(first_five_char)

third_to_fifth_char = s[2:5]
print(third_to_fifth_char)

#reverse string
s = 'hello world'
reverse_str = s[::-1]
print(reverse_str)

#string library function
#in as a logical operator

fruit = 'banana'
print('n' in fruit)
print('m' in fruit)