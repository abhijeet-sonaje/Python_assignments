'''
Created on Sep 22, 2016

@author: sonaje_a

Question 
3)    Write a program to write 2 account objects into file & read them back. Use pickle module.
'''
import q3rd,pickle

def pickle_file():
    f = open('Account.dat', 'ba')
    acc_obj_1 = q3rd.Account(1, 'Tom', 10000)
    acc_obj_2 = q3rd.Account(2, 'Jerry', 20000)
    pickle.dump(acc_obj_1, f)
    pickle.dump(acc_obj_2, f)
    print('pickled Account Objects')
    
def unpickle_file():
    f = open('Account.dat', 'br')
    obj_1 = pickle.load(f)
    obj_2 = pickle.load(f)
    print('type of my_company_list: ', type(obj_1),type(obj_2))
    print('Object 1:',obj_1)
    print('Object 2:',obj_2)

pickle_file()
unpickle_file()   