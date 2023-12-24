s=input("Enter the  String: ")
d,l,o=0,0,0

for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        l+=1
    else:
        o+=1
        
print("The Number of Digit ",d)
print("The Number of Letter ",l)
print("The Number of Special Character ",o)