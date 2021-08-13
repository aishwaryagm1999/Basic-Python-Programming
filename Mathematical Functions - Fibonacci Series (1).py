#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibo(num):
    a = 0
    b = 1
    sums = 0
    if num <0:
        print("cannot print sequence for negative value")
    if num == 1:
        print(a)
    for i in range(0,num):
        print(a)
        c = a+b
        a = b
        b = c
fibo(int(input()))

