weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

KILO = 0.45359237
METER = 0.0254

WEIGHT = weight * KILO
HEIGHT = height * METER

BMI = WEIGHT / (HEIGHT ** 2)

print("BMI: ", BMI)

if BMI <= 18.5:

    print("You are underweight")

elif BMI > 18.5 and BMI <= 24.9:

    print("You are normal")

elif BMI >= 25.0 and BMI <= 29.9:

    print("You are overwight")

else:

    print("You are obese")
