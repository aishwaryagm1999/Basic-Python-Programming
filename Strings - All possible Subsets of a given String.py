#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[16]:


from itertools import combinations #predefined library function to find subsets/combinations of a string's characters
  
str1 = str(input("Enter input string: "))
leng = len(str1) #string length
ls1 = []
subsets= [] #list to hold all possible subsets

for i in range(1,leng+1):                #finding subsets of each combination among the letters of the string
    temp = combinations(str1, i)         #combinations are printed as list of tuples
    ls1.append(list(temp))
for j in ls1:                            #tuples are converted to list form
        for k in j:
            subsets.append(''.join(k))
print("The subsets of String "+str1+": "+subsets)


# In[ ]:




