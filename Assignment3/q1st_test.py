'''
Created on Sep 20, 2016

@author: sonaje_a
'''
#!/usr/bin/python
from calc import standard,scientific

num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))
print("Addition : "+str(standard.add(num1,num2)))
print("Subtraction : "+str(standard.sub(num1,num2)))
print("Multiplication : "+str(standard.mul(num1,num2)))
print("Division : "+str(standard.div(num1,num2)))

degree = int(input('Enter angle in degree to perform sin,cos: '))

print("Sin : "+str(scientific.sin(degree)))
print("Cos : "+str(scientific.cos(degree)))

num = int(input('Enter any number: '))

print("Square : "+str(scientific.square(num)))
print("Square root : "+str(scientific.squareroot(num)))
