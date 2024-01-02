rows=int(input("Enter the rows :"))

for i in range(1,rows+1):
    for space in range(1,rows-i+1):
        print(end=" ")
    
    for i in range(1,i+1):
        print("*",end=" ")
    print('') 