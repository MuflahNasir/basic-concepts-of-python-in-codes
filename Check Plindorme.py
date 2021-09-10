integer = eval(input("Enter three-digit integer: "))

digit1 = integer % 10
Rem_integer = integer // 10

digit2 = Rem_integer % 10
digit3 = Rem_integer //10

print("The integer is ",integer)

if digit1 == digit3:
    print("The integer is palindrome")

else:
    print("The integer is not palindrome")
    
