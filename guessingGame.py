import random

chance = 5
number = (random.randint(1,9))


while chance > 0:
    guess = int(input("enter your guess:"))
    if guess == number:
        print("congrats you got the number correct")
    elif guess != number:
        chance - 1
        print("you guessed worng, try again")
        break

if chance == 0:
    print("you lose")