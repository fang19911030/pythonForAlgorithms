# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:05:23 2016

@author: fang2
"""

def radixSortFixedString(array):
    fixedLength=len(array[0])
    oa=ord('A')
    oz=ord('Z')
    n=oz-oa+1
    buckets = [[] for i in range(0,n)]
    for position in reversed(range(0,fixedLength)):
        for string in array:
            buckets[ord(string[position])-oa].append(string)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]

    return array

A=['ABC','DEF','AFQ']
B=radixSortFixedString(A)