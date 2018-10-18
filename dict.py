# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:03:58 2018

@author: tyagi
"""

n= int(input())
xx={}
xxSet=[]
for x in range(n):
    input_str =input().split(" ")
    xx[input_str[0]]= input_str[1]
    xxSet.append(input_str[0])


while(True):
    input_str1 =input()
    if input_str1 in xxSet:
        print(input_str1 + "=" + xx[input_str1])
    else:
        print("Not found")

