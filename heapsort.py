# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 12:56:06 2016

@author: fang2
"""

def parent(i):
    return i//2
    
def left(i):
    return 2*i+1
    
def right(i):
    return 2*i+2
    
def max_heapify(A,i,heap_size):
    l=left(i)
    r=right(i)
    print(l)
    if l <heap_size and A[l]>A[i]:
        largest=l
    else:
        largest=i
    if r<heap_size and A[r]>A[largest]:
        largest=r
    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest,heap_size)
        
def build_max_heap(A):
    heap_size=len(A)
    x=(heap_size//2)
    for i in reversed(range(x)):
        max_heapify(A,i,heap_size)
        
def heapsort(A):
    build_max_heap(A)
    heap_size=len(A)
    for i in reversed(range(1,len(A))):
        A[0],A[i]=A[i],A[0]
        heap_size=heap_size-1
        max_heapify(A,0,heap_size)
        
A=[2,3,1,4,6,5,8,7,9]
heapsort(A)
print (A)

        
    
    
