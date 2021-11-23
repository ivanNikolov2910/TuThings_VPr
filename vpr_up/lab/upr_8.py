import math, random, sys


# 1 напишете функция, проверяваща, дали число е палиндром, ф(х) получава число, връща 1 ако е палиндром и 0 ако не е

def is_palindrome(number):
    if number <= 9:
        return 0

    string, flag = list(str(number)), 0
    for i in range(len(string)):
        if string[i] == string[len(string) - i - 1]:
            flag += 1
    if flag == len(string):
        return 1
    else:
        return 0


num = int(input("Enter number: "))
print(is_palindrome(num))


# # 2 да се реализира калкулатор за цели числа --> + - * /

def my_sum(a, b):
    return a + b


def my_sub(a, b):
    return a - b


def my_multi(a, b):
    return a * b


def my_div(a, b):
    return a / b


while True:
    operator = input("Enter operator (+,-,*,/): ")
    if operator == '':
        break
    num1, num2 = int(input("Num1: ")), int(input("Num2: "))
    if operator == '+':
        print(my_sum(num1, num2))
    elif operator == '-':
        print(my_sub(num1, num2))
    elif operator == '*':
        print(my_multi(num1, num2))
    elif operator == '/':
        print(round(my_div(num1, num2), 2))



# 3  на функция се подават 2 аргумента - лист нъм и чусло. Променете всички ел от списъка със стойност > число на 0

def change_vales(array, number):
    for i in range(len(array)):
        if array[i] > number:
            array[i] = 0

    return array


print(change_vales([1, 2, 3, 4, 5, 6], 3))


# 4	Напишете програма с функция с произволен брой числови аргументи, която връща като резултат списък от три елемента:
# средноаритметичната, максималната и минималната стойност на аргументите.

def n_arg_func(*args):
    list = args
    return [sum(list) / len(list), max(list), min(list)]


print(n_arg_func(1, 2, 3))
