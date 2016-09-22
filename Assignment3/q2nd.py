'''
Created on Sep 21, 2016

@author: sonaje_a
'''
from datetime import datetime

class InvalidDayError(BaseException):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return '**** '+ str(self.message) + ' ****'
        
class Date():
    def __init__(self, d=25,m=4,y=2010):
        self.d = d
        self.m = m
        self.y = y
    
    def __str__(self):
        return str(self.d) + '-'+ str(self.m) + '-'+ str(self.y)
    
    def __lt__(self,other):
        if self.y < other.y:
            return True
        elif self.y == other.y and self.m < other.m:
            return True
        elif self.y == other.y and self.m == other.m and self.d < other.d:
            return True
        else:
            return False
    def setDay(self,d):
        if(d<=31 and d>=1):
            self.d = d
        else:
            raise InvalidDayError(str(d)+' Day is Invalid')
        
newdate = Date(12,5,2015)
try:
    newdate.setDay(35)
except InvalidDayError as ie:
    print("Error :" + str(ie))