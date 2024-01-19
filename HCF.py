num1=int(input('Enter the first number'))
num2=int(input('Enter THe second number'))

if num1<num2:
    num1,num2=num2,num1

while(num2!=0):
    num1,num2=num2,num1%num2

print(f'HCF of the number is {num1}')    