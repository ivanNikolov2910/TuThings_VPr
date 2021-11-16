# Напишете програма която намира лицето на геометрична фигура, като първо се въвежда вида на фигурата:
# 1 квадрад - 2 правочфълник - 3 пр. триъгл. - 4 усп. - 5 ромб с деф

# from upr_7_fig import Figure
#
# while True:
#     index = int(input("Лице на: 1 квадрат; 2 правоъгълник; 3 проъгълен триъглъгалник; 4 успоредник; 5 ромб"))
#     if index == 1:
#         fig = Figure("squ", int(input("side a: ")))
#         print(fig.area())
#     elif index == 2:
#         fig = Figure("rec", int(input("side a: ")), int(input("side b: ")))
#         print(fig.area)
#     elif index == 3:
#         fig = Figure("tri", int(input("side a: ")), int(input("side b: ")))
#         print(fig.area)
#     elif index == 4:
#         fig = Figure("para", (input("side a: ")), int(input("side b: ")), int(input("side h: ")))
#         print(fig.area)
#     elif index == 5:
#         fig = Figure("rhombus", int(input("side a: ")), int(input("side b: ")), int(input("side h: ")))
#         print(fig.area)


def squ_area(a=None):
    return a ** 2

def rec_area(a=None, b=None):
    return a * b

def tri_area(a=None, b=None):
    return a * b / 2

def para_and_rh_area(a=None, h=None):
        return a * h

def unknown_fig():
    return "unknown figure"

while True:
    index = int(input("Лице на: 1 квадрат; 2 правоъгълник; 3 проъгълен триъглъгалник; 4 успоредник; 5 ромб:  "))
    if index == 1:
        print(squ_area(int(input("side a: "))))
    elif index == 2:
        print(rec_area(int(input("side a: ")), int(input("side b: "))))
    elif index == 3:
        print(tri_area(int(input("side a: ")), int(input("side b: "))))
    elif index == 4:
        print(para_and_rh_area(int(input("side a: ")), int(input("height h: "))))
    elif index == 5:
        print(para_and_rh_area(int(input("side a: ")), int(input("height h: "))))
    else:
        print(unknown_fig())