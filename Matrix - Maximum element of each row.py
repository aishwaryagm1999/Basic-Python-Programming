#!/usr/bin/env python
# coding: utf-8

# In[ ]:


r = int(input("rows: "))
c = int(input("cols: "))
mat= []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    print()
    mat.append(a)
    
    
for i in range(r):
    for j in range(c):
        print(mat[i][j],end = " ")
    print("\n")
print()
for i in range(r):
    for j in range(c):
        max = mat[0][0]
        if mat[i][j]>max:
            max = mat[i][j]
    print("max of row ",i," : ",max)

