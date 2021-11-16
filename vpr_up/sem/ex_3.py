# 1#####################################################################################################################
size = int(input("Length: "))
list = []
for i in range(size):
    num = int(input("Number {}: ".format(i)))
    list.append(num)
print("list is full")

def get_max(list):
    max, pos = list[0], None
    for i in range(len(list)):
        if max < list[i]:
            max, pos = list[i], i
    return [max, pos]


max_pos = get_max(list)

print('list: ',list)
print('man and pos: ',max_pos)

# 2#####################################################################################################################
word = input("String: ")
new_dict = dict()
#asdaf
for i in range(len(word)):
    key = word[i]
    val = word.replace(key, '', 1)
    new_dict[key] = val
print(new_dict)

# 3#####################################################################################################################
string = input("Text: ")
tup = tuple(string)
tup_rev = tuple(reversed(string))
res = tuple()

for i in range(int(len(tup)/2)):
    res += (tup[i], tup_rev[i],)

print(tup)
print(tup_rev)
print()
print(res)

tup = tuple(string)
step = int(input("Step: "))
res = tuple()
# for i in range(0,len(tup), step):
#     res += (tup[i],)
res += tup[0::step]
print(res)

# 4######################################################################################################################
import random
size = int(input("List size:"))
list = [random.randint(0, 20) for i in range(size)]
print(list)
list_even = [list[i] for i in range(len(list)) if i % 2 == 0]
print("list_even: ", list_even)
list_odd = [list[i] for i in range(len(list)) if i % 2 != 0]
print("list_odd: ", list_odd)
list_even.sort()
list_odd.sort(reverse=True)

res = list_even + list_odd

print("Result:", res)
