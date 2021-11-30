# class Person[name, family, age, nationality] -> Constructor дава стойности на полетата, method print,
# имена и националност, обекти инстанции, за тях print

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age: int = int(age)
        self.nationality = nationality

    def print(self):
        print(self.name)
        print(self.family)
        print(self.nationality)
        print()


# class Student[student_id, student_name], add property student_class, def -> извеждане на цялото свойство и техните
# стойности в класа Student

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def set_class(self, student_class):
        self.student_class = student_class

    def print(self):
        print(str.format("{} - {}: {}", self.student_id,self.student_name, self.student_class))
        print()
