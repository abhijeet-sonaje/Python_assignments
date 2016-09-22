'''
Created on Sep 20, 2016

@author: sonaje_a
'''
text = ''

blank = ''
while True:
    str = input()
    if(str == blank):
        break
    text += str.upper()+'\n'
print(text)