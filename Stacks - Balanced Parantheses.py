#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def paran(str1):
    stack = []
    for i in range(0,len(str1)):
        if str1[i] in ['(','[','{']:
            stack.append(str1[i])
        else:
            if len(stack) != 0: 
                chk = stack.pop()
                if chk == '(' and str1[i] == ')':
                    c = 1
                elif chk == '{' and str1[i] == '}':
                    c = 1
                elif chk == '[' and str1[i] == ']':
                    c = 1
                else:
                    c = -1
                    return c
            else:
                return -1
final = paran("{}{}{}[[[[[]]]]])))))}}}}}")
if final == -1:
    print("not balanced")
else:
    print("balanced")

