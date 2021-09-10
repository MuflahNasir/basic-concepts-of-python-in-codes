import math

a, b, c = eval(input("Enter values of a, b and c: "))

dis = (b ** 2) - (4 * a *c)

if dis > 0:

    r1 = (- b + math.sqrt(dis)) / 2 * a
    r2 = (- b - math.sqrt(dis)) / 2 * a

    print("The roots are ",r1," and ",r2)

elif dis == 0:

    r1 = (- b + math.sqrt(dis)) / 2 * a

    print("The root is ",r1)

else:

    print("The equation has no real roots")
