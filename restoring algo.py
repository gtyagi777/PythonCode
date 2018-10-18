# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:41:21 2018

@author: tyagi
"""
def add(x,y):
    carry = 0
    c=[]
    x= x.reverse()
    y= y.reverse()
    for i in range(len(x)):
        c.append((x[i] + y[i] + carry) % 2)
        carry = (x[i] + y[i] + carry)/2
    return c.reverse()
        

def comp(a):
    list_one = [0,0,0,0,0,0,0,1]
    for i in range(len(a)) :
        if a[i] == 0 :
            a[i]=1
        else:
            a[i]=1
    return add(a, list_one)

def left_shift(x,y):
    for i in range(len(x)-1):
        x[i] = x[i + 1]
    x[7]= y[0]
    for i in range(len(y)-1):
        y[i] = y[i + 1]
    y[7]=0
    return (x,y)

def Handle_list(a):
    for i in range(len(a)):
        a[i] = str(a[i])
    return (a)

def display(a,b,c):
    print("".join(Handle_list(a)))
    print("\t")
    print("".join(Handle_list(b)))
    print("\t")
    print("".join(Handle_list(c)))
    print("\t")
    
def dec_to_bin(x):
    return list(bin(x)[2:])
 
def divide(a,b):
    acc = [0,0,0,0,0,0,0,0]
    m=a
    q=b
    n=[0,0,0,0,0,0,0,0]
    count = 8;
    display(acc, q, m)
    for i in range(count):
        for d in range(len(acc)):
            n[d] = m[d]
        acc,q = left_shift(acc,q)
        display(acc,q,m)
        print("shift\n")
        z = comp(n)
        print(z)
        acc = add(acc,z)
        display(acc, q, m)
        print("Subtract\n")
        if(acc[0] == 1):
            q[7] = 0
            acc = add(acc,m)
            display(acc, q, m)
            print("Restore\n")
        else:
            q[7]=1
            display(acc, q, m);
            print("Set Q0=1\n");


divide ([0,0,0,0,0,1,0,0] , [0,0,0,0,0,0,1,0])



