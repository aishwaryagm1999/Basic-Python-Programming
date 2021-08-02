#!/usr/bin/env python
# coding: utf-8

# # PYTHON STRING ROTATION (LEFT)

# In[ ]:





# In[5]:


str1 = str(input("Enter String to Rotate: ")) # string input
k = int(input("Enter number of times string is Rotated to the left: ")) #number of times string is rotated to the left
ls = []
for i in range(len(str1)): #code for converting string to list
    ls.append(str1[i])

ls1 = len(ls)
for i in range(k): #code for rotation of string to the left
    
    ls.insert(0,ls[ls1-1])
    del ls[-1]
    
finalstr = ""
for i in range(0,len(ls)):
      finalstr = finalstr+ls[i]
print("Rotated String: "+finalstr)


# In[ ]:




