integer = eval(input("Enter an integer: "))

if integer % 5 == 0 and integer % 6 == 0:
    print("The number ",integer," is both divisible by 5 and 6?",integer % 5 == 0 and integer % 6 == 0)
elif integer % 6 == 0 or integer % 5 == 0:
    print("The number ",integer," is divisible by 5 or 6?", integer % 6 == 0 or integer % 5 == 0)
elif (integer % 6 == 0 or integer % 5 == 0) and not (integer % 5 == 0 and integer % 6 == 0):
    print("The number ",integer," is divisible by 5 or 6 but not both? ",(integer % 6 == 0 or integer % 5 == 0) and not (integer % 5 == 0 and integer % 6 == 0))
else:
    print("Invalid number")
    
