import math
import sys

"""usl.: Програма, която изчислява стипендията на студенти.
Студента  трябва да въведе своя успех и максималната стипендия в този университет.
Ако студента има успех > =5.50- получава максимална стипендия
Ако студента има успех > = 5.00 и < 5.50 получава 70% от макс. стипендия
Ако студента има успех  >=  4.50 и  <5.00 получава 50% от макс. стипендия
Ако студента има успех под 4.50 не получава стипендия."""
"""
max_scolarship = float(input("Enter scolarship: "))
grade = float(input("Enter grade: "))
scolarship = 0

if grade >= 5.50:
    scolarship = max_scolarship
elif 5.50 > grade >= 5.00:
    scolarship = max_scolarship * 70 / 100
elif 5.00 > grade >= 4.50:
    scolarship = max_scolarship * 50 / 100
else:
    scolarship = None

print(scolarship)

"""

"""usl.: Напишете програма, която изчислява лицето S и обиколката P на геометрична фигура,
 като първо се избира вида на фигурата: квадрат, правоъгълник, правоъгълен триъгълник,
 след което въвеждате стойности за страните на фигурата."""
"""
shape = input("Enter shape: square/rectangle/right-angled triangle =>")
s, p = 0, 0
if shape == "square":
    side = int(input("Enter side: "))
    s = side ** 2
    p = 4 * side
elif shape == "rectangle":
    side = int(input("Enter side a: "))
    side2 = int(input("Enter side b: "))
    s = side * side2
    p = 2 * (side + side2)
elif shape == "right-angled triangle":
    side = int(input("Enter side a: "))
    side2 = int(input("Enter side b: "))
    side3 = math.sqrt(side2**2 + side**2)
    if side + side2 <= side3 or side3 + side2 <= side or side3 + side <= side2:
        print("this cannot be triangle")
        sys.exit()
    p = side + side2 + side3
    s = math.sqrt(p / 2 * (p / 2 - side) * (p / 2 - side2) * (p / 2 - side3))
else:
    print("unknown shape")
print("S = ",s)
print("P = ",p)
"""

"""usl.: Напишете програма, която намира средноаритметичното на числата , 
които се делят на 3 в интервала от  7 до 70."""
'''
sum, count = 0,0
for i in range(7, 70+1):
    if i % 3 == 0:
        sum += i
        count += 1
print(sum/count)
'''

"""usl.: Напишете програма, която по въведено от потребителя число определя :
Цифрата на единиците дели ли се на 5, а цифрата на десетиците четно число ли е"""
'''
num = int(input("Enter number: "))
if (math.floor(num / 10)) % 2 == 0:
    print("last digit is even")
else:
    print("last num is odd")
if (num % 10) % 5 == 0:
    print("is dividable by 5")
else:
    print("is not dividable by 5")
'''

"""usl.: Напишете програма, която по зададен брой дни (n), извежда кой ден от седмицата ще бъде. 
Днешният ден и броят на дните се въвеждат от потребителя. 
Да се изведе на екрана  n-тия ден след днешния кой ден от седмицата е. 
Броенето на дните започва от едно т.е 1- понеделник , 2- вторник, 3- сряда, 4- четвъртък , 5- петък , 6- събота и 7-неделя.

Примерен вход: 1  3
Примерен изход:  четвъртък"""
"""
this_day = int(input("Current day: "))
searched_day = int(input("Searched day: "))
day, count = 0, 0
for i in range(this_day, searched_day+1):
    day = i
    if i%7 == 0:
        count += 1
    if i > 7*count:
        day -= 7*count

day += 1
if day == 1:
    print("понеделник")
elif day == 2:
    print("вторник")
elif day == 3:
    print("сряда")
elif day == 4:
    print("четвъртък")
elif day == 5:
    print("петък")
elif day == 6:
    print("събота")
elif day == 7:
    print("неделя")
"""
