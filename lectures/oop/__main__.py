import lec15_Student

st1 = lec15_Student.Student(121221010, "Ivan", 4.76)
st2 = lec15_Student.Student(121221123, "Petar", 5.61)
st3 = lec15_Student.Student(121221047, "Georgi", 3.44)
print(st1.__str__())
print()
print()

st_group = lec15_Student.StGroup()

print(st_group)
st_group.add_student(st1)
st_group.add_student(st2)
st_group.add_student(st3)
print(st_group)

st_group.remove_student(st3)
print(st_group)

print(st_group.avg_mark())

