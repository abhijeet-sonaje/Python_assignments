'''
Created on Sep 20, 2016

@author: sonaje_a
'''
l = {x for x in input().split()}
l1 = list(l)
l1.sort()
for i in l1:
    print(i,end=" ")