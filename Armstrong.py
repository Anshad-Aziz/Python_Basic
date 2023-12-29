num=int(input("Enter the 3 digit number:"))
n=int(input("Enter the power :"))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
    
if sum==num:
    print(f'{num} is Armstrong Number')
else:
    print(f"{num} is not a Armstrong Number")