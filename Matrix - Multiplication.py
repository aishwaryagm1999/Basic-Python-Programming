#!/usr/bin/env python
# coding: utf-8

# In[ ]:


p = int(input("rows: ")) #p*n for mat and n*q for mat1 (n is same for both mats, also res will have p*q rows/cols)
n = int(input("cols: "))
q = int(input("col2: "))

mat= []
for i in range(p):
    a = []
    for j in range(n):
        a.append(int(input()))
    print()
    mat.append(a)
    
mat1= []
for i in range(n):
    a = []
    for j in range(q):
        a.append(int(input()))
    print()
    mat1.append(a)
    
    
    
for i in range(p):
    for j in range(n):
        print(mat[i][j],end = " ")
    print()
print()
for i in range(n):
    for j in range(q):
        print(mat1[i][j],end = " ")
    print()

    
    
    
res = []
for i in range(p):
    a = []
    for j in range(q):
        a.append(0)
    print()
    res.append(a)

    
    
for i in range(p):
    for j in range(q):
        for k in range(n):
            res[i][j] = res[i][j]+mat[i][k]*mat1[k][j]

            
for i in range(p):
    for j in range(q):
        print(res[i][j],end = " ")
    print()

