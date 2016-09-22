'''
Created on Sep 20, 2016

@author: sonaje_a
'''
l = [x for x in input().split(',')]
l.sort()
for i in l:
    print(i,end=",")