# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:57:43 2018

@author: tyagi
"""
n= int(input())
for x in range(n):
    input_str =list(input())
    a=""
    b=""
    for xx in range(len(input_str)):
        if(xx%2!=0):
            a= a + input_str[xx]
        else:
             b = b + input_str[xx]
    print(b + " " + a)