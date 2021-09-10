number = 0
sum = 0

while number <= 20:
    number += 1
    sum += number
    if sum >= 100:
        break

print("Number is ", number)
print("Sum is ", sum)
