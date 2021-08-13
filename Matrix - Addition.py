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
    
mat1= []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    print()
    mat1.append(a)
    
for i in range(r):
    for j in range(c):
        print(mat[i][j],end = " ")
    print()
print()
for i in range(r):
    for j in range(c):
        print(mat1[i][j],end = " ")
    print()
    
    
res = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(0)
    print()
    res.append(a)

for i in range(r):
    for j in range(c):
        res[i][j] = mat[i][j]+mat1[i][j]
for i in range(r):
    for j in range(c):
        print(res[i][j],end = " ")
    print()

