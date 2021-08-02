#!/usr/bin/env python
# coding: utf-8

# # PYTHON COMMON CHARACTERS OF TWO STRINGS IN ALPHABETICAL ORDER

# In[ ]:





# In[8]:


s0 = str(input("Enter String 1 : "))
s1 = str(input("Enter String 2 : "))
s3 = [] #list variable to contain common characters
s4 = "" #string variable to contain final common characters

for i in range(len(s0)): 
    if s0[i] in s1:                   #checking whether string 1 (s0) characters are in string 2 (s1)
        s3.append(s0[i])              #adding common character values to list s3
        
s3.sort()                             #sorting common characters in alphabetical order

for i in range(len(s3)):              #converting list to string
    s4 = s4+s3[i]
    
print(" The Common Characters in Alphabetical Order : "+s4)


# In[ ]:




