import random

integer = random.randint(0,1)
guess = eval(input("Enter your guess for head and tail: "))

if guess == integer:
    print("Your guess is correct")
else:
    print("Your guess is not correct")

print("Computer chooses ",integer)
