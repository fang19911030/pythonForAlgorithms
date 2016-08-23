# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:49:13 2016

@author: pengcheng
"""

class HashTable:
    
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
        
    def put(self,key,data):
        hashvalue=self.hashfunction(key,len(self.slots))
        
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data         #replace
                
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot]!=None and \
                self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot,len(self.slots))
                    
                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data      #replace
                    
    def hashfunction(self,key,size):
        return key%size
        
    def rehashfunction(self,oldhash,size):
        return (oldhash+1)%size
        
        
    def get(self,key):
        starslot=self.hashfunction(key,len(self.slots))
        
        data=None
        stop=False
        found=False
        position=starslot
        
        while self.slots[position] !=None and \
        not found and not stop:
            if self.slots[position]==key:
                found=True
                data=self.data[position]
            else:
                position=self.rehashfunction(position,len(self.slots))
                if position==starslot:
                    stop=True
                    
        return data
        
    def __getitem__(self,key):
        return self.get(key)
        
    def __setitem__(self,key,data):
        self.put(key,data)
                    
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
print (H.data)