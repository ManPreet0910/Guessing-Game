guess = (input("Enter your guess:"))
chance = 5
number = (9)

if guess == number:
    chance=chance-1
    guess=(input("Enter your guess:"))

while chance < 5:

    if guess == number:
        print("Congrats YOU WON!")
        break
    else:
        guess - 1
        


if not chance < 5:
    print("YOU LOSE!!! the number is", number)
    
    