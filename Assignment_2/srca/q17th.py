'''
Created on Sep 20, 2016

@author: sonaje_a
'''
from operator import itemgetter
s = 'Press Enter to enter blank line to exit.\nEnter tuple: '
print(s)
l = []
while True:
    t = input()
    #print(t)
    if(t == ''):
        break;
    t = tuple(t.split(','))
    l.append(t)

print("List(Unsorted): ",l)
print("List(sorted): ",sorted(l, key = itemgetter(0,1, 2)))    

