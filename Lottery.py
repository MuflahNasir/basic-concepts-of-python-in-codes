import random

number = random.randint(0, 99)

guess = eval(input("Enter you lottery guess of two digit number: "))

digit1 = guess % 10
digit2 = guess //10

number1 = number % 10
number2 = number // 10

print("Lotter number is ",number)

if guess == number:

    print("You win $10,000")

elif (digit1 == number1 or digit2 == number1) and (digit1 == number2 or digit2 == number2):

    print("You win $3000")

elif (digit1 == number1 or digit2 == number1) or (digit1 == number2 or digit2 == number2):

    print("You win $1000")

else:

    print("Incorrect guess!!")
