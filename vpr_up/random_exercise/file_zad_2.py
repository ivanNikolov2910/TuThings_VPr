# 1
# import random
# import string
# def set_size(rows, cols):
#     list = [[0 for i in range(cols)] for j in range(rows)]
#     return list
#

# rows = int(input("rows: "))
# cols = int(input("cols: "))
# list = set_size(rows, cols)
#
# random.seed()
# for i in range(0, rows):
#     for j in range(0, cols):
#         list[i][j] = random.choice(string.ascii_letters)
#
# for i in range(0, rows):
#     for j in range(0, cols):
#         print(list[i][j], " ", end="")
#     print()

# 2 ..................................


# 3
# import random
# import sys
#
# random.seed()
# rows, cols = random.randint(2,5), random.randint(2,5)
# list = [[random.randrange(-1000, 1000) for i in range(cols)] for j in range(rows)]
# print("Num rows", rows, "  ", "Num cols", cols)
# row, col = int(input("row: ")), int(input("col: "))
#
# if row > rows or col > cols:
#     print("invalid input")
#     sys.exit()
#
# for rows in list:
#     print(rows)
#
# del list[row]
# for rows in list:
#     del rows[col]
# print()
# print()
#
# for rows in list:
#     print(rows)

# 4 ..................................

# 5
# import random
#
# size = int(input("Length: "))
# list = [random.randint(-1000, 1000) for i in range(size)]
#
#
# def get_max(list):
#     max, pos = list[0], None
#     for i in range(len(list)):
#         if max < list[i]:
#             max, pos = list[i], i
#     return [max, pos]
#
#
# max_pos = get_max(list)
#
# print(list)
# print(max_pos)

# Inverse matrix
# import numpy as np
#
# A = np.array([[6, 1, 1, 3],
#               [4, -2, 5, 1],
#               [2, 8, 7, 6],
#               [3, 1, 9, 7]])
#
# print(np.linalg.inv(A))
