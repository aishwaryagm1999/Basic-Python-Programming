#!/usr/bin/env python
# coding: utf-8

# In[ ]:


stack = []
stacksize = 5
while(True):
    op = int(input("enter operation (1.push,2.pop,3.display,4.peek,5.exit): "))
    print("\n")
    if op == 1:
        if len(stack)<stacksize:
            ele = int(input("Enter ele to push: "))
            stack.append(ele)
            print("pushing element ",ele,"\n")
        else:
            print("stack overflow")
    elif op == 2:
        if len(stack)==0:
            print("stack underflow")
        else:
            print("popped element is: ",stack.pop(),"\n")
    elif op == 3:
        if len(stack)==0:
            print("stack is empty")
        else:
            print(stack,"\n")
    elif op ==4:
        if len(stack)==0:
            print("stack is empty")
        else:
            print(stack[len(stack)-1],"\n")
    elif op == 5:
        print("exiting")
        break
    else:
        print("enter proper option\n")

