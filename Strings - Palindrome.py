#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def palin(str1): #method 1
    str2 = str1[::-1]
    if str2 == str1:
        return "palindrome"
    else:
        return "not palindrome"
    

def palin2(str1): #method 2
    str2 = ""
    for i in range(len(str1)-1,-1,-1):
        str2=str2+str1[i]
    
    if str2 == str1:
        return "palindrome"
    else:
        return "not palindrome"
      
        
print(palin(str(input())))
print(palin2(str(input())))

