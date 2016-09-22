'''
Created on Sep 20, 2016

@author: sonaje_a
'''
for n in range(1000,3001):
    i=n
    count = 0
    while True:
        temp = int(i%10)
        #print('temp',temp)
        if(temp%2 == 0):
            count += 1
        i = int(i/10)
        if(i == 0):
            break;
    
    if count == 4:
        print(n)
    