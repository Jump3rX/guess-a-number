import random

print("Guess the number")
top_range = input("Type a number: ")
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <=0:
        print("Type number greater than 0!")
        quit()
else:
    print("Please enter a number!")
    quit()

random_num = random.randint(1,top_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter number!")
        continue
    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess >random_num:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in",guesses,"tries")