# Write a python program to translate a message into secret code language. Use the rules 
# below to translate normal English into secret code language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string
# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter a


import random
import string
n=input('Enter a line:')
# for i in n:
    # if len(i)<3:
# u=i[1:]+i[0]
a1=random.choices(string.ascii_letters+string.digits,k=3)
print(type(a1))
print(a1)
# a2=random.choices(string.ascii_letters+string.digits,k=3)
# print(a1+u+a2)
        














# a='abcdef'
# for i,x in enumerate(a,start=2):
#     print(i,x)


'''random_chars_start = ''.join(random.choices(string.ascii_letters + string.digits, k=3))'''
# print(random_chars_start)
# print(string.ascii_letters + string.digits,)