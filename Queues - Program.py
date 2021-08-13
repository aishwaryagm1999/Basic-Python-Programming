#!/usr/bin/env python
# coding: utf-8

# In[ ]:


queue = []
queuesize = 5


while(True):
    op = int(input("enter operation (1.enqueue,2.dequeue,3.display,4.front ele,5.rear ele,6.exit): "))
    print("\n")
    
    
    if op == 1:
        if len(queue)<queuesize:
            ele = int(input("Enter ele to add: "))
            queue.append(ele)
            print("pushing element ",ele,"\n")
        else:
            print("queue overflow")
            
            
            
    elif op == 2:
        if len(queue)==0:
            print("queue underflow")
        else:
            print("removed element is: ",queue.pop(0),"\n")
            
            
    elif op == 3:
        if len(queue)==0:
            print("queue is empty")
        else:
            print(queue,"\n")
            
            
            
    elif op == 4:
        if len(queue)==0:
            print("queue is empty")
        else:
            print(queue[0])
        
        
        
        
    elif op ==5:
        if len(queue)==0:
            print("queue is empty")
        else:
            print(queue[len(queue)-1],"\n")
            
            
            
    elif op == 6:
        print("exiting")
        break
        
        
    else:
        print("enter proper option\n")

