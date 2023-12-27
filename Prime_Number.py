num=int(input("Enter the Number : "))

if num<1:
    print("Number is Not Prime Number")
elif num>1:
    for i in range (2,num):
        if num%i==0:
            print(f'{num} is not Prime Number')
            break
    else:
        print(f'{num} is Prime NUmber')