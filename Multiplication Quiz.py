import random

i1 = random.randint(0, 99)
i2 = random.randint(0, 99)

answer = eval(input("What is " + str(i1) + " * " + str(i2) + " ? "))

print("Your answer of ",i1," * ",i2," = ",answer," is ",i1 * i2 == answer)
