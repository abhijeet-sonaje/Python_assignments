'''
Created on Sep 20, 2016

@author: sonaje_a
'''
error =''
def ispass(password):
    global error
    error=''
    if len(password) >12:
        error += 'Password is too LONG it must be between 6 and 12 characters\n'
    elif len(password) <6:
        error += 'Password is too SHORT it must be between 6 and 12 characters\n'
    elif (password.lower()== password):
        error += 'Password need to contain at least 1 letter between [A-Z]\n'
    elif (password.upper()==password):
        error += 'Password need to contain at least 1 letter between [a-z]\n'
    elif (password.isalnum()==password):
        error += 'Password need to contain at least 1 number between [0-9]\n'
    elif password.find('$') == -1 and password.find('#') == -1 and password.find('@') == -1:
        error += 'Password need to contain at least 1 character from [$#@]\n'
    else:
        error = 'True'
    return error

str = [x for x in input().split(',')]

for x in str:
    if(ispass(x) == 'True'):
        print(x,end=",")