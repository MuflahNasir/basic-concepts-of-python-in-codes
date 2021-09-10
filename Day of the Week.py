year = eval(input("Enter a year e.g. (2000) : "))
m = eval(input("Enter month 1-12: "))
q = eval(input("Enter day of the month 1-31: "))

def switch(h) :
    return {
        0 : "Saturday",
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
        }[h]

if m == 1:
    m = 13
    year = year -1

elif m == 2:
    m = 14
    year = year - 1

j = year // 100
k = year % 100

h = q + ( ((26 * (m + 1)) //10) // 1) + k + ((k // 4) // 1) + ((j // 4) // 1) + 5 * j
h = h % 7

print("The day is",switch(h))
