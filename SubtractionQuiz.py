import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:

    number1, number2 = number2, number1

answer = eval(input("What is " + str(number1) + "-" + str(number2) + "? "))

if number1 - number2 == answer:

    print("Your answer is correct")

else:

    print("Your answer is wrong.\n" , number1, "-", number2, "=", number1 - number2, ".")
        
