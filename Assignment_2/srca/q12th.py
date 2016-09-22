'''
Created on Sep 20, 2016

@author: sonaje_a
'''
str = (input('Enter the String: '))
uletters = 0
lletters = 0
for i in str:
    if (ord(i) >= 97 and ord(i) <= 122):
        lletters += 1
    if (ord(i) >=65  and ord(i) <= 90):
        uletters += 1

print('Upper Case Letters:',uletters)
print('Lower case Letters:',lletters)