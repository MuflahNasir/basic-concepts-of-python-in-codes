status = eval(input("\t\t FILING STATUS \n" +
                    "\t 0-> Single \n" +
                    "\t 1-> Married filing jointly \n" +
                    "\t 1-> Married filing separately \n" +
                    "\t 3-> Head of Household \n" +
                    "\nEnter your filing status: "))

income = eval(input("Enter your income: "))

tax = 0

if status == 0:

    if income <= 8350:

        tax = income * 0.10

    elif income >= 8351 and income <= 33950:

        tax = income * 0.15

    elif income > 33950 and income <= 82250:

        tax = income * 0.25

    elif income > 82250 and income <= 171550:

        tax = income * 0.28

    elif income > 171550 and income <= 372950:

        tax = income * 0.33

    else:

        tax = income * 0.35

elif status == 1:

    if income <= 16700:

        tax = income * 0.10

    elif income > 16700 and income <= 67900:

        tax = income * 0.15

    elif income > 67900 and income <= 137050:

        tax = income * 0.25

    elif income > 137050 and income <= 208850:

        tax = income * 0.28

    elif income > 208850 and income <= 372950:

        tax = income * 0.33

    else:

        tax = income * 0.35

elif status == 2:

    if income <= 8350:

        tax = income * 0.10

    elif income >= 8351 and income <= 33950:

        tax = income * 0.15

    elif income > 33950 and income <= 68525:

        tax = income * 0.25

    elif income > 68525 and income <= 104425:

        tax = income * 0.28

    elif income > 104425 and income <= 186475:

        tax = income * 0.33

    else:

        tax = income * 0.35

else:

    if income <= 11950:

        tax = income * 0.10

    elif income > 11950 and income <= 45500:

        tax = income * 0.15

    elif income > 45500 and income <= 117450:

        tax = income * 0.25

    elif income > 117450 and income <= 190200:

        tax = income * 0.28

    elif income > 190200 and income <= 372950:

        tax = income * 0.33

    else:

        tax = income * 0.35

print("Your tax is: ", tax)
