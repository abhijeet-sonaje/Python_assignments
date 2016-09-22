'''
Created on Sep 20, 2016

@author: sonaje_a
'''
l = [int(x,2) for x in input().split(',')]
for i in l:
    if i%5==0:
        print (bin(i)[2:])