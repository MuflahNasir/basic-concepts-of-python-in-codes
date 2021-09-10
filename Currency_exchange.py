exchange_rate = eval(input("Enter Exchange rate from dollar to RMB: "))
convert = eval(input("Enter 0 to convert dollar to RMB and 1 for vice versa: "))

if convert == 0:
    amount = eval(input("Enter the dollar amount: "))
    RMB = amount * exchange_rate
    RMB = format(RMB, '.2f')
    print("$",amount," equals to ",RMB,"yuan")

elif convert == 1:
    amount = eval(input("Enter the RMB amount: "))
    dollar = amount / exchange_rate
    dollar = format(dollar, '.2f')
    print(amount," yuan equals to $ ",dollar)

else:
    print("Invalid Number")
