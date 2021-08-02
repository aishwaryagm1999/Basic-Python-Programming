str1 = str(input("Enter Main String: "))
ch1 = str(input("Enter value of ch1: "))
ch2 = str(input("Enter value of ch2: "))
str2 = "" #string variable to have final string

for i in range(len(str1)): 
    if str1[i] == ch2:        #replacing ch2 with ch1 from str1 and adding to final string
        str2 = str2+ch1
        
    elif str1[i] == ch1:      #replacing ch1 with ch2 from str1 and adding to final string
        str2 = str2+ch2
        
    else:
        str2 = str2+str1[i]   #adding remaining characters to final string
        
print(str2)
