class Student:
    def __init__(self, fnum, name, mark):
        self.fnum = fnum
        self.name = name
        self.mark = mark

    def greet(self):
        print("Name:", self.name)
        print("Fac. Number:", self.fnum)
        print("Mark:", self.mark)

    def __str__(self):
        return "Name: {0} \nFac. Num: {1} \nMark: {2}".format(self.name, self.fnum, self.mark)


class StGroup:
    def __init__(self):
        self.group = []

    def add_student(self, student):
        self.group.append(student)

    def remove_student(self, student):
        self.group.remove(student)

    def avg_mark(self):
        sum = 0
        for st in self.group:
            sum += st.mark
        return round(sum/len(self.group), 2)

    def __str__(self):
        output = ""
        for student in self.group:
            output += str(student) + "\n\n"
        return output


# # st1 = Student(int(input("Fac. Num: ")), input("Name: "), float(input("Mark: ")))
# st1 = Student(121221010, "Ivan Nikolov", 4.76)
# st1.greet()
# st1.__str__()
