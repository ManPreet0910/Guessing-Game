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

    


# if guess == number:
#         print("Congrats YOU WON!")
# elif guess != number:
#         chance = chance - 1
#         print("Your guess was incorect try again, you have", str(chance),"more chance left")

# while chance < 5 :
#     if chance == 0:
#         print("YOU LOSE!!! the number is", number)
        
        