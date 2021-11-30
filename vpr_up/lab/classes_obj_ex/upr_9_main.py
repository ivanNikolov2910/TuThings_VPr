from upr_9 import Person, Student


def __main__():
    p1, p2 = Person("Kostadin", "Kostadinow", 21, "bulgarian"), Person("Nikolai", "Nikolow", 18, "bulgarian")
    p1.print()
    p2.print()

    s1, s2 = Student(12, "Kalvin"), Student(15, "Genadi")
    s1.set_class("12a")
    s2.set_class("12a")

    s1.print()
    s2.print()


if __name__ == '__main__':
    __main__()
