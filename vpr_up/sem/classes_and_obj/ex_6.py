# 1 Напишете програма, в която е дефиниран клас със следните характеристики: Класът има конструктор, на който се
# предават две стойности.Тези стойности се присвояват на полетата на обекта от дадения клас. В класа трябва да бъде
# описан метод, при извикването на който се показват стойностите на полетата на класа. Проверете функционалността на
# класа , като създадете на негова основа няколко обекта.


class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def print_info(self):
        print("Name:", self.title, "--> pages: ", self.pages)
        print()


b1 = Book("Imeto na knigata", 156)
b2 = Book("Chast 2", 371)

b1.print_info()
b2.print_info()


# 2 Напишете програма, в която е описан клас. Обектите на класа трябва да имат поле, представляващо числов списък.
# Този списък се формира на основата на списък, предаден като аргумент на конструктора. При това от списъка аргумент
# в списъка поле се включват само числовите елементи(  елементите от други типове се игнорират). Също така трябва да
# се дефинират два метода :Първият метод показва съдържанието на полето списък, а вторият метод изчислява средната
# стойност на елементите на полето списък.

def only_ints(inp_list):
    int_list = list()
    for i in inp_list:
        if type(i) is int:
            int_list.append(i)
    return int_list


class my_class:

    def __init__(self, new_list):
        self.new_list = [i for i in new_list if type(i) is int]         #only_ints(new_list)

    def print(self):
        print(self.new_list)

    def get_avg(self):
        return sum(self.new_list) / len(self.new_list)


obj = my_class(['a', 1, 2, 3, 'sd', 4])
obj.print()
print(obj.get_avg())


# 3 Напишете програма, в която е описан клас  и функция , предназначена за създаване на списък от обекти. Обектите на
# класа трябва да имат поле (   предназначено за записване на целочислена стойност). При извикване на функцията се
# предава като аргумент цяло число, определящо броя на обектите  в списъка. Полетата на обектите се запълват с цели
# нечетни числа.

import random


class Number:
    def __init__(self, num):
        self.num = num


def obj_gen(count):
    obj_list = list()
    for i in range(count):
        obj_list.append(Number((random.randint(1, 100) * 2 + 1)))
    return obj_list


l1 = obj_gen(5)
print(l1)


# 4 Напишете програма, в която е описана функция. На функцията се предават като аргументи два обекта от един и същи
# клас. Всеки обект има поле представляващо списък от цели числа. Функцията връща като резултат обект от същия клас.
# Полето списък на този обект се получава посредством сумирането на съответните елементи от полетата списъци на
# обектите , предадени като агументи на функцията. Ако в тези обекти списъците са с различна дължина,
# то недостигащите елементи в списъка се запълват с нули.


class Data:
    def __init__(self, new_list):
        self.new_list = new_list


obj1 = Data([1])
obj2 = Data([1, 2, 3, 4])


# obj1 = Data([1, 2, 3, 4])
# obj2 = Data([1])


def get_obj_sum(a: Data, b: Data):
    list_a = a.new_list
    list_b = b.new_list
    diff = len(list_a) - len(list_b)

    if diff > 0:
        for i in range(diff):
            list_b.append(0)
        length = len(list_a)
    else:
        for i in range(abs(diff)):
            list_a.append(0)
        length = len(list_b)

    list_res = list()

    for i in range(length):
        list_res.append(list_a[i] + list_b[i])
    return Data(list_res)


print(get_obj_sum(obj1, obj2).new_list)
