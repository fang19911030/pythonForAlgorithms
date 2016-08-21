# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 09:12:59 2016

@author: pengcheng
"""

class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
        
    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next
        
    def setData(self,newdata):
        self.data=newdata
        
    def setNext(self,newnext):
        self.next=newnext
        
class UnorderedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head==None
        
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
        
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
            
        return count
        
    def search(self,item):
        current=self.head
        found=False
        while current != None and  not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
                
        return found
   
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous = current 
                current = current.getNext()
                
        if previous==None:
            self.head==current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def append(self,item):
        current=self.head
        temp=Node(item)
        
        if current == None:
            self.head=temp
        else:
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(temp)
            
    def index(self,item):
        current=self.head
        count=0
        found=False
        if current==None:
            return RuntimeError
        else:
            while current!=None and not found:
                if current.getData() == item:
                    found=True
                else:
                    current=current.getNext()
                    count+=1        
        if found:
            return count
        else:
            return None
            
    def insert(self,pos,item):
        current=self.head
        item=Node(item)
        if pos>self.size()-1:
            return RuntimeError
        else:
            for i in range(pos):
                current=current.getNext()
            item.setNext(current.getNext())
            current.setNext(item)
            
    def getItem(self,index):
        current=self.head
        if index>self.size()-1:
            return RuntimeError
        else:
            for i in range(index):
                current=current.getNext()
            return current.getData()
            
    def pop(self,index):
        self.remove(self.getItem(index))
        
            
        
            
            

            
a=UnorderedList()
a.append(1)
a.append(2)
a.append(3)
print (a.search(2))
#a.remove(2)
print (a.search(2))
#a.remove(3)
print (a.index(1))
a.insert(0,4)
print (a.index(4))
print (a.getItem(1))
                
                
        
         