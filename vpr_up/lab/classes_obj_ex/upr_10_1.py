# class, който представя студентите в групата, метод, който по име добавя студенти, които не са в списъка,
# метод remove при слаб успех, метод за среден успех на групата

# part 2 метод за намиране на min/max grade - 2methods и метод който връща данните за студентите с еднакъв успех

# 2 метода: данни във файл. чете и създава списък на студентите. Метод, който връща данни а студент с четен и нечетен
# фак. нум

# name: A..., method to upper_case, write_to_file_json, sort_id

import constants.pr_constants as pr_constants
import json


class Student():
    def __init__(self, f_num, name, family, grade):
        self.f_num = f_num
        self.name = name
        self.f_name = family
        self.grade = grade

    def __str__(self):
        return str.format('{} {}: {}', self.f_num, self.name, self.grade)


class Group:
    def __init__(self, st_list: list):
        self.st_list: list = st_list

    def present(self):
        for st in self.st_list:
            print(str.format("{} {} -> f_num: {}", st.name, st.f_name, st.f_num))
        print()

    def add_new(self, new_st: Student):
        for st in self.st_list:
            if st.f_num == new_st.f_num:
                print('This student is already in the group!!')
                return
        else:
            self.st_list.append(new_st)
            print("Done")

    def remove(self):
        for i in self.st_list:
            if i.grade < 3:
                self.st_list.remove(i)

    def avg_grade(self):
        grades = [st.grade for st in self.st_list]
        return round(sum(grades) / len(self.st_list), 2)

    def get_min_grade(self):
        sr_list = sorted(self.st_list, key=lambda student: student.grade)
        return sr_list[0]

    def get_max_grade(self):
        sr_list = sorted(self.st_list, key=lambda student: student.grade, reverse=True)
        return sr_list[0]

    def get_equal_grade(self, grade):
        new_set = set()
        for i in range(len(self.st_list)):
            if self.st_list[i].grade == grade:
                new_set.add(self.st_list[i])
        return new_set

    def create_new_list(self, file):
        for row in file:
            data_list = row.split(' ')
            self.st_list.append(Student(int(data_list[0]), data_list[1], data_list[2], float(data_list[3])))

    def get_even(self):
        for st in self.st_list:
            if st.f_num % 2 == 0:
                return st

    def get_odd(self):
        for st in self.st_list:
            if st.f_num % 2 != 0:
                return st

    def get_names_a(self):
        res_list = list()
        for i in self.st_list:
            if i.name[0] == 'A':
                res_list.append(i)
        return res_list

    def set_names_upper(self):
        for i in range(len(self.st_list)):
            self.st_list[i].name = self.st_list[i].name.upper()
            self.st_list[i].f_name = self.st_list[i].f_name.upper()

    def sort_id(self):
        return sorted(self.st_list, key=lambda st: st.f_num)

    def write_json(self):
        json_file = pr_constants.RESOURCES_PATH + "students_json.json"
        with open(json_file, "a") as file:
            for st in self.st_list:
                data = {"id": st.f_num, "name": st.name, "family": st.f_name, "grade": st.grade}
                json_data = json.dumps(data)
                file.write(json_data)


gr43a = Group([Student(121221146, 'Aleksandar', 'Shopov', 4.60), Student(121221144, 'Aysel', 'Kazalieva', 4.60),
               Student(121221178, 'Miroslav', 'Dilov', 5.60), Student(121221000, 'Nqkoi', 'Nepoznat', 2.60),
               Student(121221096, 'Vasil', 'Alendarov', 5.60)])

# # gr43a.add_new(Student(121221096, 'Vasil', 'Alendarov', 5.60))
# gr43a.add_new(Student(121221010, 'Ívan', 'Nikolov', 5.60))
# gr43a.present()
#
# # print по успех
# print(gr43a.avg_grade())
# print(gr43a.get_min_grade())
# print(gr43a.get_max_grade())
#
# # метод който връща данните за студентите с еднакъв успех
# gr_stud_list = gr43a.get_equal_grade(5.60)
# for i in gr_stud_list:
#     print(i, end="  ")
#
# gr43a.remove()

# file = open(str(pr_constants.RESOURCES_PATH + 'students.txt'), 'r')
# gr43a.create_new_list(file)
# for st in gr43a.st_list:
#     print(st)
#
# print("\n\n")
# print(gr43a.get_even())
# print(gr43a.get_odd())

for st in gr43a.get_names_a():
    print(st)
print()
gr43a.set_names_upper()
for st in gr43a.st_list:
    print(st)
print()

for st in gr43a.sort_id():
    print(st)

gr43a.write_json()

