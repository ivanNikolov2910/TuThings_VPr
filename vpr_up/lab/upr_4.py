import random

s = [1, 3, 5, 7]
print(s[1])

s[1] = 11
print(s)

s = list()
s1 = list("Python")
print(s1)

s = ['P', 'y', 't', 'h', 'o', 'n', 3]
print(s)
s = []
s.append(5)
s.append(10)
s.append(20)
# print(s[3]) IndexError: list index out of range

s = [1, 2, 3, 4, 5, 6]
print(s[::-1])
print(s[:-1])
print(s[1:])
print(s[0:2])
print(s[-1:])

s1 = [10, 11]
s2 = s + s1
print(s2)

s = [[1, 2, 3, 4, 5], ['a', 'b', 'c'], [10, 20]]
print(s[0][3])
print(s[2][0])

s = [2, 1, 4, 1, 6, 1, 21]

for i in range(len(s)):
    print(s[i], end='')
print()
for i in s:
    print(i, end='')
print()

print(4 in s)
print(s.count(1))
# print(s.index(3))
print(max(s), ' ', min(s))

s.append(22)
s += [44, 88]
print(s)
s.insert(0, 80)
print(s)
print(s.pop())
print(s)
print(s.pop(5))
print(s)
s.remove(1)
print(s)
del s[2]
print()

s = [2, 4, 6, 8, 2]
random.shuffle(s)
print(s)
print(random.choice(s))
s.reverse()
print(s)
s.sort()
print(s)

s.sort(reverse=True)
print(s)
s1 = list("PyTHon")
print(s1)
s1.sort(key=str.lower)
s1.sort()
print(s1)

k = (7, 5, 5, 3)
print(k)
tup = tuple([10,20,30])
tup1 = tuple("Python")
print(tup)
print(tup1)

