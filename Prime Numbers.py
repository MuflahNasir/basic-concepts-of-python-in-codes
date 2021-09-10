TOTAL_NUMBERS = 50
number = 2
divisor = 2
count = 0
NUMBER_PER_LINE = 10

print("Number of primes")

while count < TOTAL_NUMBERS:
    isPrime = True

    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1

    if isPrime:
        count += 1

        print(format(number, '5d'), end = " ")
        if count % NUMBER_PER_LINE == 0:
            print()

    number += 1
