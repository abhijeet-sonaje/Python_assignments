'''
Created on Sep 21, 2016

@author: sonaje_a
'''
class Employee:
    def __init__(self, empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary
        
    def getsalary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, empno, name, salary, incentive):
        super().__init__(empno, name, salary)
        self.incentive = incentive
    
    def getsalary(self):
        return self.salary+self.incentive
    
class Labor(Employee):
    def __init__(self, empno, name, salary, overtime):
        super().__init__(empno, name, salary)
        self.overtime = overtime
        
    def getsalary(self):
        return self.salary+self.overtime

manager1 = Manager(12,'Jerry',65000,5000)
labor1 = Labor(500,'Tommy',12500,500)
print(manager1.getsalary())
print(labor1.getsalary())