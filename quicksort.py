# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 18:29:57 2016

@author: fang2
"""

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
    
def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
        
A=[4,3,8,10,2,6,1,12,5]
quicksort(A,0,len(A)-1)
print (A)
