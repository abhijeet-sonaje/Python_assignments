'''
Created on Sep 20, 2016

@author: sonaje_a
'''
str = (input('Enter the String: ')).lower()
letters = 0
digits = 0
for i in str:
    if (ord(i) >= 97 and ord(i) <= 122):
        letters += 1
    if (ord(i) >= 48 and ord(i) <= 57):
        digits += 1

print('Letters:',letters)
print('Digits:',digits)