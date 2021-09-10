import random

integer1 = random.randint(0, 99)
integer2 = random.randint(0, 99)

answer = eval(input("What is " + str(integer1) + " + " + str(integer2) + " ? "))

print("Your answer of ",integer1, " + ",integer2," = ",answer," is ",integer1 + integer2 == answer)
