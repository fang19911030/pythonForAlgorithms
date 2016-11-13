# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:42:31 2016

@author: fang2
"""

def counting_sort(A,B,k):
    c=[0]*k
    for j in range(len(A)):
        c[A[j]]=c[A[j]]+1
    for i in range(k):
        c[i]=c[i]+c[i-1]

    for j in reversed(range(len(A))):
        B[c[A[j]]-1]=A[j]
        c[A[j]]-=1



A=[1,2,3,5,6,1,2,8,8,6,7,7,2,3,1]
B=[0]*len(A)
counting_sort(A,B,10)
