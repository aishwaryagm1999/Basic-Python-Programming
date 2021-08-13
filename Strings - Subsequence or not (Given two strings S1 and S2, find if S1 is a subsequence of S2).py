#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str1 = "bxc"
str2 = "bdbpycx"
str3 = ""
for i in range(len(str2)):
    if str2[i] in str1:
        if str2[i] not in str3:
            str3 = str3+str2[i]
if str1 == str3:
    print("yes")
else:
    print("no")

