'''
Created on Sep 21, 2016

@author: sonaje_a
'''
import q3rd,q2nd,datetime

def sortlist(objlist):
    for i in range(0,len(objlist)):
        for j in range(i+1,len(objlist)):
            if objlist[j]< objlist[i]:
                temp = objlist[i]
                objlist[i] =objlist[j]
                objlist[j] = temp
    return objlist
    
dateslist =[q2nd.Date(23,9,2010), q2nd.Date(2,2,2010),q2nd.Date(15,2,2010),q2nd.Date(2,3,2010),q2nd.Date(2,2,2012)]
accountlist =[q3rd.Account(1, 'Tom', 10000),q3rd.Account(1, 'Tom', 9000),q3rd.Account(1, 'Tom', 8000),q3rd.Account(123, 'Dev', 234),q3rd.Account(123, 'Bob', 15000)]
print('Unsorted Account list') 
for i in accountlist:
    print(str(i))

print('sorted Account list')    
for i in sortlist(accountlist):
    print(str(i))

print('Unsorted Dates list') 
for i in dateslist:
    print(str(i))

print('sorted Dates list')    
for i in sortlist(dateslist):
    print(str(i))

