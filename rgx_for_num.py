# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:59:34 2016

@author: pengcheng
"""

import regex

numlist=[]
file=open('sample_data.txt')
for line in file:
    line=line.rstrip()
    numbers=regex.findall(('[0-9]+'),line)
    for numer in numbers:
        numlist.append(float(numer))


 
summ = 0
for number in numlist:
	summ += number