# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:20:15 2018

@author: tyagi
"""

def merge_the_tools(string, k):
    # your code goes here
    xx=[]
    
    for i in range(0,len(string),k):
        yy=[]
        for x in string[i:i+k]:
            if x not in yy:
                yy.append(x)
        print("".join(yy))
    
            

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)