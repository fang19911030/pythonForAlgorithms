# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:31:24 2016

@author: fang2
"""
import timeit
import random
import time
from datetime import timedelta
def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2
                   
                   ):
        R.append(A[q
                   +j+1])
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    k=p
    while k<=r:
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
        k=k+1
    

def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        

def main():    
    n=[10,1000,100000,1000000]
    for elem in n:
        test=[]
        for i in range(elem):
            test.append(random.randint(0,10000000))
        start_time=time.monotonic()
        merge_sort(test,0,len(test)-1)
        end_time=time.monotonic()
        print (timedelta(seconds=end_time-start_time))
        
if __name__=='__main__':
    main()