#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
count = 0
for i in range(2,n):
    if n%i == 0:
        count=1
        break
if count == 1:
    print("no")
else:
    print("yes")

