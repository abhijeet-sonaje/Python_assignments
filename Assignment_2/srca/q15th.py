'''
Created on Sep 20, 2016

@author: sonaje_a
'''
from _overlapped import NULL
s = 'Enter input and Enter "-1 -1" to exit: '
print (s)
Money = 0
while True:
    a,b=input().split()
    if( a == '-1' or b== '-1'):
        break
    elif( a == 'D'):
        Money += int(b)
    elif( a == 'W'):
        if(Money > int(b)):
            Money -= int(b)
        else:
            print('Insuficient Balance');

print("Money in Account:",Money)