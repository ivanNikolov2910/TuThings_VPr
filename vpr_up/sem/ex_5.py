import math, random, sys


# 1 Напишете програма, в която е описана функция , която проверява дали едно цяло число е просто,
# числото се предава като аргумент на функцията.
# Функцията връща резултат 1 ако числото е просто и 0 ако числото не е просто.
# Да се принтират всички прости числа в интервала от 2 до това число.


# def is_prime(num):
#     for i in range(2, int(math.sqrt(num) + 1)):
#         if num % i == 0:
#             return int(False)
#     return int(True)
#
#
# def print_prime_range(num):
#     for i in range(2, num + 1):
#         if is_prime(i):
#             print(i, end=" ")
#     print()
#
#
# check_num = int(input("Enter num: "))
#
# print(is_prime(check_num))
# print_prime_range(check_num)


# 2 Програма английско - български речник, запълнен речник със стойности.
# Потребителя прави своя избор , който може да е :
# - търсене на дума в речника
# - добавяне на дума
# -изтриване на дума
# -показване на всички думи в речника .
# Програмата продължава докато не се въведе  символа q- изход .
# За всяка една от опциите реализирайте отделни функции.

def add_to_dict(my_dict, key, val):
    my_dict[key] = val


def del_word(my_dict, key):
    del my_dict[key]


def search_word(my_dict, key):
    return my_dict[key]


def show_all(my_dict):
    print(my_dict)


my_dict = dict()

# preset data
my_dict['cat'] = 'котка'
my_dict['dog'] = 'куче'
my_dict['person'] = 'човек'

print("s - търсене на дума в речника\n"
      "a - добавяне на дума\n"
      "d - изтриване на дума\n"
      "all - показване на всички думи в речника\n"
      "q - изход")

while True:
    cmd = input("Command: ")
    if cmd == 'q':
        print("END")
        break
    elif cmd == 's':
        print(search_word(my_dict, input("Enter word: ")))
    elif cmd == 'a':
        add_to_dict(my_dict, input("Enter engl word: "), input("Enter bg meaning: "))
    elif cmd == 'd':
        del_word(my_dict, input("Enter word: "))
    elif cmd == 'all':
        show_all(my_dict)
    else:
        print("invalid Input")
