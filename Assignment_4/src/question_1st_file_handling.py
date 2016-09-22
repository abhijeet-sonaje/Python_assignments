'''
Created on Sep 22, 2016

@author: sonaje_a

Question: 

1)    Write a program to handle file system with following options:
Options:
a)    Overwrite text to an existing file
b)    Append text to an existing file
c)    Read contents of the file
    Please enter your option:

'''
def op_file_w():
    f = open('abc.txt', 'w')
    z = input(' op_file_w File content to write : ')
    #print(f)
    f.write(z)
    f.close()
    
def op_file_a():
    f = open('abc.txt', 'a')
    z = input(' op_file_a File content to write : ')
    #print(f)
    f.write(z)
    f.close()
    
def op_file_r():
    f = open('abc.txt', 'r')
    print(' op_file_r File contents: ' + f.read())
    #print(f)
    f.close()
    

s = 'Enter -1 to exit'
print(s)
while True:
    print('Please enter your option: ')
    print('\ta) Overwrite text to an existing file')
    print('\tb) Append text to an existing file')
    print('\tc) Read contents of the file')
    input_op = input()
    if input_op == '-1':
        break
    else:
        if input_op == 'a':
            op_file_w()
        if input_op == 'b':
            op_file_a()
        if input_op == 'c':
            op_file_r()
        
            


