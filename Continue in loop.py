number = 0
sum = 0

while number <= 20:
    number += 1
    if number == 10 and number == 11:
        continue
    sum += number

print("Sum is ",sum)
