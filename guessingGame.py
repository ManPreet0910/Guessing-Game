import random

chance = 5
number = (random.randint(1,9))
guess = ""

while chance > 0:
    guess = (input("enter your guess:"))
    if guess == number:
        print("congrats you got the number correct")
    elif guess != number:
        chance - 1
        print("you lost")

if chance == 0:
        print("your lose the number was", number)

    
