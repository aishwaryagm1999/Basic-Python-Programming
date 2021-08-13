#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import array
n = int(input("Array length: "))
ls = list(map(int,input().split(" ")))
arr = array.array('i',ls)

key = int(input("key: "))
for i in range(0,n):
    if arr[i] == key:
        co = i
        break;
    else:
          co = -1
if co !=-1:
    print("Search Successful, element found at index: ",co)
else:
    print("element not found")

