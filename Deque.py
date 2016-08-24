# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 17:20:27 2016

@author: pengcheng
"""

class Deque:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
        
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
        
    def removeRear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
        
def palchecker(aString):
    chardeque=Deque()
    
    for ch in aString:
        chardeque.addRear(ch)
        
    stillEqual=True
    
    while chardeque.size()>1 and stillEqual:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first != last:
            stillEqual=False
            
    return stillEqual
    
print (palchecker("lsdkjfskr"))
print (palchecker("radar"))        