def area(name, a=None, b=None, h=None):
    if name == "squ":
        return a ** 2
    elif name == "rec":
        return a * b
    elif name == "tri":
        if h is None:
            return a * b / 2
    elif name == "para" or name == "rhombus":
        return a * h
    else:
        return "unknown figure"


class Figure:

    def __init__(self, name, side_a=None, side_b=None, height=None):
        self.name = name
        self.a = side_a
        self.b = side_b
        self.h = height
        self.area = area(name, side_a, side_b, height)

    def __str__(self):
        return str("side a: {0}, side b: {1}, height h: {2}".format(self.a, self.b, self.h))

# squ = Figure(5, 5)
# tri = Figure(5, 5, 2)
#
# print(tri)
# print(squ)
