'''
Created on Sep 23, 2016

@author: sonaje_a

Question
1)    Suppose there is a water tank with capacity 100 liters. There is one inlet & one outlet to the tank. Inlet pours water inside the tank whereas outlet gets it out from the tank. Inlet speed is double than outlet speed. Write a program to maintain water level around 80 liters.
'''
import threading
from threading import Thread
import time
import random

class Inlet(Thread):
    def __init__(self, amount,condition,current_water):
        Thread.__init__(self)
        self.amount = amount
        self.condition = condition
        self.capacity = 100
        self.current_water = current_water

    def run(self):
        while True:
            #print('Inlet acquired lock')
            self.condition.acquire()
            while True:
                self.current_water['level'] += 2*self.amount
                #print('Pouring water inside tank',self.amount,'liters')
                print('Inlet open Current water',self.current_water['level'],'liters')
                if self.current_water['level'] >= 80 :
                    break
            self.condition.notify()
            #print('Inlet released lock')
            self.condition.release()
            #time.sleep(1)
            
class Outlet(Thread):
    def __init__(self, amount, condition,current_water):
        Thread.__init__(self)
        self.amount = amount
        self.condition = condition
        self.capacity = 100
        self.current_water = current_water
        
    def run(self):
        while True:
            #print('\tOutlet acquired lock')
            self.condition.acquire()
            while True:
                self.current_water['level'] -= self.amount
                #print('\tGetting out water from tank',self.amount,'liters')
                print('\tOutlet Open Current water',self.current_water['level'],'liters')
                if self.current_water['level'] <= 80 :
                    break
            #print('\tOutlet released lock')
            self.condition.wait()
            self.condition.release()

def main():
    current_water = {'level':0}
    condition = threading.Condition()
    inletThread = Inlet(3, condition,current_water)
    outletThread = Outlet(3, condition,current_water)
    inletThread.start()
    outletThread.start()
    inletThread.join()
    outletThread.join()
    print('Exiting app!!')
        
if __name__ == '__main__':
    main()