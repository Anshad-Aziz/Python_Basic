row=int(input("Enter the Number of Rows: "))

for i in range(row,0,-1):
    for space in range(1,row-i+1):
        print(end=" ")
    for star in range (1,i+1):
        print('*',end=' ')
    print('')   
    
for j in range(1,row+1):
    for space in range(1,row-j+1):
        print(end=' ')
    for star in range(1,j+1):
        print('*',end=' ')
    print('') 