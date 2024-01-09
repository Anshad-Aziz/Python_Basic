s=input("Enter the String:  ")

start=0
end=len(s)-1
flag=True

while start<end:
    if s[start]!=s[end]:
        flag=False
    start+=1
    end-=1
    
if flag:
    print("Palindrome")
else:
    print("Not A Palindrome")
    
    