str1 = str(input("Enter String to Rotate: ")) # string input
k = int(input("Enter number of times string is Rotated to the right: ")) #number of times string is rotated to the right
ls = []
for i in range(len(str1)): #code for converting string to list
    ls.append(str1[i])

ls1 = len(ls)
for i in range(k): #code for rotation of string to the right
    
    ls.insert((ls1),ls[0])
    del ls[0]
    
finalstr = ""
for i in range(0,len(ls)):
      finalstr = finalstr+ls[i]
print("Rotated String: "+finalstr)
