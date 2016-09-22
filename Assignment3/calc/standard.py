'''
Created on Sep 21, 2016

@author: sonaje_a
'''

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    try:
        result = num1/num2
        return result
    except ArithmeticError as ae:
        print('Error : '+ae)