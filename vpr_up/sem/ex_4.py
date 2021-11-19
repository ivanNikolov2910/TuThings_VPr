# 1
# Напишете програма, в която се създава  функция.
# Функцията получава като аргумент числов списък и връща като резултат друг списък,
# в който са включени само нечетните числа от списъка аргумент.

import random

list_in = [random.randint(0, 100) for i in range(10)]


def get_odds(list_in):
    list_odd = []
    for i in list_in:
        if i % 2 != 0:
            list_odd.append(i)
    return list_odd


list_odd = get_odds(list_in)
print(list_in)
print(list_odd)

# 2 Напишете функция, която проверява дали два стринга въведени от потребителя са анаграма.
# Функцията получава като аргументи два стринга,връща като резултат 1 ако са анаграма и 0 ако не са.

word_1 = input("String 1: ")
word_2 = input("String 2: ")


def is_anagr(str1, str2):
    s1 = sorted(list(str1))
    s2 = sorted(list(str2))

    return int(s1 == s2)


print(is_anagr(word_1, word_2))


# 3 Напишете програма,в която е описана функция,връщаща като резултат второто по големина число в списъка,
# предаден като аргумент на функцията.

def ret_second_max(new_list):
    new_list.sort()
    return new_list[len(new_list) - 2]


my_list = [random.randint(0, 100) for i in range(10)]

print(ret_second_max(my_list))
my_list.sort()
print(my_list)


# 4 Напишете програма , в която се създава функция с два аргумента, които са числови списъци. Резултатът от функцията
# е число, равно на сумата от двойките произведения на елементите на списъците. Ако в един от списъците елементите са
# по-малко от другия, то недостигащите елементи се получават посредством циклично повторение на съдържанието на
# списъка.


def get_sum(list1, list2):
    l1_size = len(list1)
    l2_size = len(list2)

    if l1_size > l2_size:
        difr = l1_size - l2_size
        for i in range(difr):
            list2.append(list2[i])
    elif l1_size < l2_size:
        difr = l2_size - l1_size
        for i in range(difr):
            list1.append(list1[i])

    sum = 0
    for i in range(0, max(l2_size, l1_size)):
        sum += (list1[i] * list2[i])

    return sum


list1 = [random.randint(0, 5) for i in range(3)]
print(list1)
list2 = [random.randint(0, 5) for i in range(14)]
print(list2)

print(get_sum(list1, list2))


# 5 Програма, която включва две функции. Първата функция създава матрица с числа и я запълва със стойности,
# приема като аргумент броя редове и броя колони на матрицата , връща като резултат запълнената матрица.  Втората
# функция получава като аргумент матрицата и я принтира под формата на таблица.


def make_matrix(rows, cols):
    return [[random.randint(0, 10) for j in range(cols)] for i in range(rows)]


def print_matrix(matr):
    for i in matr:
        for j in i:
            print(j, end=" ")
        print()


''' [[3 2 5]
     [5 6 6]]'''


def print_sum_cols(matr):
    for i in range(len(matr[0])):
        sum = 0
        for j in range(len(matr)):
            sum += matr[j][i]
        print(sum)


rows = int(input("Rows: "))
cols = int(input("Cols: "))

new_matrix = make_matrix(rows, cols)
print_matrix(new_matrix)
print_sum_cols(new_matrix)
