number = eval(input("Enter decimal number (0 to 15): "))

h = hex(number).lstrip("0x")

print(h)
