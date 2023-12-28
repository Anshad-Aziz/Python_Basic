terms=int(input("Enter the Number to find the terms:"))

n1,n2=0,1
if terms<=0:
    print("Please Enter Positive Values")
elif terms==1:
    print(f'{n1} is the fibnoccai sequences')
else:
    for term in range (terms):
        print(f'{n1}',end=' ')
        n=n1+n2
        n1=n2
        n2=n
        