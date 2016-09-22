'''
Created on Sep 20, 2016

@author: sonaje_a
'''
import math
d = [int(x) for x in input().split(',')]

def calq(D,C=50,H=30):
    return math.sqrt((2*C*D)/H)
l = []
for i in d:
    l.append(round(calq(i)))

print(l)