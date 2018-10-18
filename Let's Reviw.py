# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:57:43 2018

@author: tyagi
"""

input_str = list(input())
a=""
b=""
for i in len(input_str):
    if(i%2==0):
        a += input_str[i]
    else:
        b += input_str[i]
print(a)
print(b)
