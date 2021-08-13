#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ls = list(map(int,input().split(" ")))
lslen = len(ls)
key = int(input("key: "))

def binsearch(ls,l,r,key):
    mid = l+(r-l)//2
    if key == arr[mid]:
        return mid
    elif key<arr[mid]:
        return binsearch(ls,l,mid-1,key)
    elif key>aarr[mid]:
        return binsearch(ls,mid+1,r,key)
    else:
        return -1
v = binsearch(ls,0,lslen-1,key)
if v == -1:
    print("element not found")
else:
    print("element found at index: ", v)

