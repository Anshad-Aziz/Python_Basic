import random
num=random.randint(1,10)
guess=int(input("Guess The number from 1-10 :"))

while guess!=num:
    if(guess<num):
        print("Entered Number is Too Low")
    elif(guess>num):
        print("Entered Number is Too High")
    guess=int(input("Guess Again"))
print("Your Guess is Right**") 