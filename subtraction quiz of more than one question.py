import random
import time

correctanswer = 0;
count = 0
totalquestion = 5

name = input("Please enter your name: ")

print("Hello",name,"!!!! You have to give answers of",totalquestion,"question ")

starttime = time.time();

while count < totalquestion:
 
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    if number1 < number2:

        number1, number2 = number2, number1

    result = eval(input("What is "+ str(number1) + " - " + str(number2) + " ? "))

    if number1 - number2 == result:

        print("Your answer is correct")
        correctanswer = correctanswer + 1

    else:

        print("Wrong answer.",number1, "-", number2,"=", number1 - number2)

    count = count + 1

endtime = time.time()

totaltime = int(endtime - starttime)

print("You gave",correctanswer,"answers of", totalquestion ,"questions in",totaltime,"seconds")

pause()
