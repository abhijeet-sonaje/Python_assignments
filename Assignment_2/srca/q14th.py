'''
Created on Sep 20, 2016

@author: sonaje_a
'''
a = [int(x) for x in input('Enter the input: ').split(',')]

for i in a:
    if(i%2 !=0):
        print(i,end=",")