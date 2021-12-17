# 5 Напишете програма меню със следните опции:
# -добавяне на студент
# -търсене на студент по език
# - извеждане на информация за всички студенти
# - изход
# За целта създайте клас Student със полета: номер на студент, име на студент и
# език за програмиране. Дефинирайте и методи: get_id(self),  get_name(self), get_language(self) , които връщат
# стойностите на полетата. Информацията за студентите се пази в текстов файл. Дефинирайте функция Add_student(
# student),която се използва за добавяне на информация за нов студент в текстов файл. Дефинирайте функция Search(
# language) за търсене на  студент по език . Дефинирайте функция Display() за принтиране на информация за всички
# студенти .

import constants.pr_constants as pr_constants

RESOURCES_PATH = pr_constants.RESOURCES_PATH


class Student:
    def __init__(self, id, name, language):
        self.id = id
        self.name = name
        self.language = language

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_language(self):
        return self.language


def add_student():
    students_file = open(RESOURCES_PATH + "students.txt", "a")
    st = Student(input("ID: "), input("name: "), input("language: "))
    students_file.write(str.format("{} {} - {}\n", st.get_id(), st.get_name(), st.get_language()))


def search_language(lang):
    sts = list()
    with open(RESOURCES_PATH + "students.txt", "r") as students_file:
        for st in students_file:
            student = st.split(" ")
            sts.append(Student(student[0], student[1], student[2]))
    for st in sts:
        if st.get_language() == lang:
            return st


def display():
    with open(RESOURCES_PATH + "students.txt", "r") as students_file:
        for st in students_file:
            print(st)


# add_student()
# add_student()
print(search_language("a"))
# display()
