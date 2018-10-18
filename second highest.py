# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:54:41 2018

@author: tyagi
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    xx = sorted(arr, reverse=True)
    x = xx[0]
    for i in xx:
        if i < x:
            print(i)
            break

