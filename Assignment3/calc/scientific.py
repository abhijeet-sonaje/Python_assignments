'''
Created on Sep 21, 2016

@author: sonaje_a
'''

import math

def sin(d):
    return math.sin(d)

def cos(d):
    return math.cos(d)

def square(d):
    return d*d

def squareroot(d):
    try:
        result = math.sqrt(d)
        return result
    except ArithmeticError as ae:
        print('Error : '+ae)
    
