a, b, c, d, e, f = eval(input("Enter values of a, b, c, d, e and f: "))

e1 = a*d - b*c
e2 = e*d - b*f
e3 = a*f - e*c

if e1 == 0:

    print("Equation has no solution")

else:

    x = e2 / e1
    y = e3 / e1

    print("The value of x is ",x," and y is ",y)
    
