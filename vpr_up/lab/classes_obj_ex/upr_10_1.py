# class, който представя студентите в групата, метод, който по име добавя студенти, които не са в списъка,
# метод remove при слаб успех, метод за среден успех на групата

# part 2 метод за намиране на min/max grade - 2methods и метод който връща данните за студентите с еднакъв успех

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


gr43a = Group([Student(121221146, 'Aleksandar', 'Shopov', 4.60), Student(121221144, 'Aysel', 'Kazalieva', 4.60),
               Student(121221178, 'Miroslav', 'Dilov', 5.60), Student(121221000, 'Nqkoi', 'Nepoznat', 2.60),
               Student(121221096, 'Vasil', 'Alendarov', 5.60)])

# gr43a.add_new(Student(121221096, 'Vasil', 'Alendarov', 5.60))
gr43a.add_new(Student(121221010, 'Ívan', 'Nikolov', 5.60))
gr43a.present()

# print по успех
print(gr43a.avg_grade())
print(gr43a.get_min_grade())
print(gr43a.get_max_grade())

# метод който връща данните за студентите с еднакъв успех
gr_stud_list = gr43a.get_equal_grade(5.60)
for i in gr_stud_list:
    print(i, end="  ")

gr43a.remove()
