x="from chetanlondhe1112@gamil.com 23 453 34 787 98"
words=x.split()
print(words[1])
email=words[1]
email_split=email.split('@')
print(email_split[0])
print(email_split[1])
host=email_split[1]
com=host.split('.')
print(com[1])
