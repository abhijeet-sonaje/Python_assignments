'''
Created on Sep 21, 2016

@author: sonaje_a
'''
class Node:
    def __init__(self,data):
        self.previous_node = None
        self.next_node = None
        self.data = data
    
    def __eq__(self,other):
        if(self.previous_node == other.previous_node and 
           self.next_node == other.next_node and 
           self.data == other.data):
            return True
        else:
            return False
        
class NodeList:
    
    def __init__(self):
        self.first = None 
        self.last = None   
    
    def addnode(self,value):
        newNode = Node(value)
        if self.first is None:
            newNode.previous_node  = None
            newNode.next_node = None
            self.first=self.last = newNode
            #print(str(newNode))
        else:
            newNode.next_node = None
            self.last.next_node = newNode
            newNode.previous_node = self.last
            self.last = newNode 
            #print(str(newNode))
            
n = NodeList()
n.addnode(15)
n.addnode(2)
#n.addnode(3)
        
                
        