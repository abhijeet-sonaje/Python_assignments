'''
Created on Sep 20, 2016

@author: sonaje_a
'''
l = []
i = 2002
while True:
    if i>=3200:
        break
    if i%5 != 0:
        l.append(i)
    i = i + 7
 
print (l)        