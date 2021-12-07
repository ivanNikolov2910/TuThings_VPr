# class, който представя студентите в групата, метод, който по име добавя студенти, които не са в списъка,
# метод remove при слаб успех, метод за среден успех на групата

class Student():
    def __init__(self, f_num, name, family, grade):
        self.f_num = f_num
        self.name = name
        self.f_name = family
        self.grade = grade


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
            if i.grade <= 2:
                self.st_list.remove(i)

    def avg_grade(self):
        grades = [st.grade for st in self.st_list]
        return round(sum(grades) / len(self.st_list), 2)


gr43a = Group([Student(121221146, 'Aleksandyr', 'Shopov', 5.60), Student(121221144, 'Aysel', 'Kazalieva', 5.60),
               Student(121221178, 'Miroslav', 'Dilov', 5.60), Student(121221067, 'Svetlin', 'Vatev', 5.60),
               Student(121221096, 'Vasil', 'Alendarov', 5.60)])


gr43a.add_new(Student(121221096, 'Vasil', 'Alendarov', 5.60))
gr43a.add_new(Student(121221010, 'Ívan', 'Nikolov', 5.60))
print(gr43a.avg_grade())
gr43a.remove()
gr43a.present()

