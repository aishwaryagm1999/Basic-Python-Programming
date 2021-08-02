#!/usr/bin/env python
# coding: utf-8

# # PYTHON COMMON CHARACTERS OF TWO STRINGS IN ALPHABETICAL ORDER

# In[ ]:





# In[13]:


str1 = str(input("Enter the String to be Reversed: "))
print("\n")

#method 1 - for loop

leng = len(str1)
print("Reversed String (Method 1): ",end = "")
for i in range((leng-1),-1,-1):
    print(str1[i],end="")
print("\n")

#method 2 - slicing operation

print("Reversed String (Method 2): "+str1[::-1],end="")


# In[ ]:




