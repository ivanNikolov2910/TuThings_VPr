# class Person[name, family, age, nationality] -> Constructor дава стойности на полетата, method print,
# имена и националност, обекти инстанции, за тях print, да се добави class Student(Person) с полента -> university &&
# year_of_study, да се предефинора print, да се дефинира class Lecturer(Person) с полета -> university && exp

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


class Student(Person):
    def __init__(self, name, family, age, nationality, university, year_of_study):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.year_of_study = year_of_study

    def print(self):
        print(
            str.format("{} {} - {} years old - {} : {} year:{}\n\n", self.name, self.family, self.age, self.nationality,
                       self.university, self.year_of_study))


class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, exp):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.exp = exp

    def print(self):
        print(
            str.format("{} {} - {} years old - {} : {} year:{}\n\n", self.name, self.family, self.age, self.nationality,
                       self.university, self.exp))



st1 = Student('Aleksandyr', 'Shopov', 19, 'bulgarian', 'TU', 1)
le1 = Lecturer('Ívan', 'Nikolov', 35, 'bulgarian', 'TU', 13)

le1.print()
st1.print()