import random

integer = random.randint(0, 100)

guess = eval(input("Enter your guess between 1 to 100: "))

while guess != integer:

    if guess > integer:
         guess = eval(input("Your guess is high, Try again: "))

    else:
        guess = eval(input("Your guess is low, Try again: "))

print("Your got it!!!!! you guessed the number")
