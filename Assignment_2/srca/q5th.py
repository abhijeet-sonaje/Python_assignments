'''
Created on Sep 20, 2016

@author: sonaje_a
'''
a = [int(x) for x in input().split(',')]
x = a[0]
y = a[1]
arr = [[0 for y in range(y)] for x in range(x)] 
for i in range(0,x):
    for j in range(0,y):
        arr[i][j] = i*j

print(arr)