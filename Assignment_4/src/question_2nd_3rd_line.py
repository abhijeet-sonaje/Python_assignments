'''
Created on Sep 22, 2016

@author: sonaje_a

Question:
2)    Write a program to read the third line of a file twice using tell() & seek() functions.
'''
def file_read():
    f = open('abc_2nd_q.txt', 'r')
    print('File 1st Line: \n' + f.readline())
    #print(f.tell())
    print('File 2nd Line: \n' + f.readline())
    #print(f.tell())
    index = f.tell()
    f.seek(index+1)
    print('File 3rd Line: \n' + f.read())
    f.seek(index+1)
    print('File 3rd Line: \n' + f.read())
    #print(f)
    f.close()
    
file_read()