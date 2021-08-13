#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Enter array elements: ")
a = list(map(int,input().split(' ')))                 #reading input as list of integers using map
n = len(a)                                            #length of input list
q = int(input("Enter number of queries: "))           #number of queries
print("\n")
v = 0 
l1 = []                                               #list to contain elements of given range from input list
count = 0                                             #variable to contain final number of elements that divides all the elements of given range

for i in range(q):                                    #loop to run each query
    
    
    l = int(input("Enter value of L (Lower bound of range): "))
    r = int(input("Enter value of R (Upper bound of range): "))
    for j in range(l-1,r):                                        #loop to obtain list of elements from input list with elements of range (l to r)
        l1.append(a[j])
    
    
    for k in range(0,len(l1)):                                    #loop to access each element one by one
        for k1 in range(0,len(l1)):                               #loop to compare above element with each element of the new list
            
            if l1[k1]%l1[k]!=0:                                   #if element  k cant divide any element of list completely use variable v to keep track
                v +=1
                
        if v==0:                                                  #if the element k divides all the elements in list variable v is 0
            count+=1                                              #increment variable count by 1 as the element divides all elements of given range
            v=0
        
    print("Query Number: ",i)
    print("Total count of numbers that divide all elements: ",count)
    
    l1 = []                                                          #clear list for next query
    count = 0                                                        #clear count for next query
    print("\n")

