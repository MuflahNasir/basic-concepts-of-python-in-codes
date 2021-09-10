import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)

answer = eval(input("What is " + str(digit1) + " + " + str(digit2) + " + " + str(digit3) + " ? "))

print("Your answer of ",digit1, " + ",digit2," + ",digit3," = ",answer," is ",digit1 + digit2 + digit3 == answer) 
