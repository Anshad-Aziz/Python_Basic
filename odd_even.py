lis=list(range(1,25))

odd=[]
even=[]

for items in lis:
    if items%2==0:
        even.append(items)
    else:
        odd.append(items)
print(f'{odd} This is Odd Number between 1-25')
print(f'{even} This is even Number between 1 -25')