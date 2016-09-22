'''
Created on Sep 21, 2016

@author: sonaje_a
'''

class InsufficientBalanceError(BaseException):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return '**** '+ str(self.message) + ' ****'
    
class Account:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return '\n\tAccount no. : '+str(self.accno) + '\n\tAccount holder\'s name : ' + str(self.name) + '\n\tAccount balance : ' + str(self.balance)
    
    def __lt__(self,other):
        if(self.balance < other.balance):
            return True
        else:
            return False
    
    def deposit(self, amount=0):
        self.balance = self.balance + amount
        return self.balance
        
    def withdraw(self, amount=0):
        if(self.balance > amount):
            self.balance = self.balance - amount
            return self.balance
        else:
            raise InsufficientBalanceError('Insufficient Balance amount by '+str(amount - self.balance)+' Rs.') 
           
acc = Account(1, 'Tom', 10000)
print('Account Details: ' + str(acc))
try:
    print('Current balance after withdraw : ', str(acc.withdraw(15000)))
except InsufficientBalanceError as ibe:
    print("Error : "+str(ibe))
    











        
        