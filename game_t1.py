import random
from random import randint


print()
print("             * * * * * * * * * * * * * *")
print("             *      Guess a number     *")
print("             *         between         *")
print("             *        1 and 1000       *")
print("             * * * * * * * * * * * * * *")
print()

level = input("choose level. Enter a number( 1:easy - 2:medium - 3:hard ) : ")

if level == "1" :
    n =15
elif level == "2" :
    n = 10
elif level == "3" :
    n = 5
else:
    print("invalid Data : Restart the program.")
    exit()
    
print()
print("             * * * * * * * * * * * * * *")
print("             *       You have :",n,"   *")
print("             *         Chances         *")
print("             * * * * * * * * * * * * * *")
print()
  
number = randint(1, 1000)

for i in range(n,0,-1):
    guess_number = int(input("             Enter your guess : "))
    print()
    if guess_number == number:
        print("             Congratulations You Win ! :)")
        exit()
    elif guess_number < number:
        print("             My number is greater than " ,guess_number," !  You have ",i-1,"other chances")
    else:
        print("             My number is lower than ",guess_number," !  You have ",i-1,"other chances")
        
print("             You Lose ! :(")
print("             My Number is ",number)
