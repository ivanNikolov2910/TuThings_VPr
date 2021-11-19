import math, random, sys


# 1 Напишете програма, в която е описана функция , която проверява дали едно цяло число е просто,
# числото се предава като аргумент на функцията.
# Функцията връща резултат 1 ако числото е просто и 0 ако числото не е просто.
# Да се принтират всички прости числа в интервала от 2 до това число.


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return int(False)
    return int(True)


def print_prime_range(num):
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end=" ")
    print()


check_num = int(input("Enter num: "))

print(is_prime(check_num))
print_prime_range(check_num)


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

# 3 Напишете програма, която отпечатва перфектните числа от даден списък с цели числа.
# Програмата включва функция, която получава като аргумент число и принтира числото ,ако то е перфектно.

def perf_nums(num):
    del_list = []
    for j in range(1, num):
        if num % j == 0:
            del_list.append(j)

    del_sum = sum(del_list)
    if del_sum == num:
        print(num, end="; ")


input_list = [random.randint(0, 100) for i in range(100)]
# input_list = [6, 78, 28]
for input in input_list:
    perf_nums(input)


# 4 Напишете функция,  която получава като аргумент числов списък.
# Елементите с четни индекси се сортират по възходящ ред, а елементите с нечетни индекси  се сортират в низходящ ред.
# Функцията връща като резултат променения списък.

def new_list(list):
    list_even = [list[i] for i in range(len(list)) if i % 2 == 0]
    print("list_even: ", list_even)
    list_odd = [list[i] for i in range(len(list)) if i % 2 != 0]
    print("list_odd: ", list_odd)
    list_even.sort()
    list_odd.sort(reverse=True)

    res = []
    try:
        for i in range(len(list)):
            res.append(list_even[i])
            res.append(list_odd[i])
    except:
        pass
    return res


# size = int(input("List size:"))
list = [11, 20, 19, 4, 1, 8, 4]
print(list)

print("Result:", new_list(list))


# 5 Напишете програма, в която е описана функция, която намира НОК на две числа.
# Числата се подават като аргументи на функцията.

def calc_lcm(num1, num2):
    if num1 > num2:
        gr_num = num1
    else:
        gr_num = num2

    while (True):
        if gr_num % num1 == 0 and gr_num % num2 == 0:
            lcm = gr_num
            break
        gr_num += 1

    return lcm


num1, num2 = int(input("Enter num1: ")), int(input("Enter num2: "))
print("LCM:", calc_lcm(num1, num2))
