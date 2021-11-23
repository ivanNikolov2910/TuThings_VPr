k = (7, 5, 3, 6, 1)

print(k[0])
print(k[2:3])
print(7 in k)
print(k * 3)
top = k + (2, 4)
print(top)

tup = (7, 5, 3, 5, 6, 1)
print(tup.index(1))
print(k.count(5))

for i in tup:
    print(i, end=" ")
print()

d = dict()
d1 = dict(name='Ivan', last_name="Nikolov")
d3 = dict([('name', 'polina'), ('lastname', 'koleva')])
print(d1)
print(d3)
d = {}
d['name'] = 'petyr'
d['l_name'] = 'kolev'
print(d)
d = {'name': 'ivan', 'last_name': 'ivanov'}
print(d)
print(d['name'])
print('name' in d)
print('ivan' in d)

d['s_name'] = 'petrov'

keys = list(d.keys())
keys.sort()
for key in keys:
    print('{} -> {}'.format(key, d[key]), end='  ')
print()
s = set([1, 2, 3, 1])
print(s)
s = set('hello')
print(s)
for i in s:
    print(i, end=' ')
print()

s1 = set([1,2,3])
s2 = set([2,4,5])
s3 = s1 | s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s2 - s1
print(s3)

# zad 1
num = int(input())

string = str(num)
tup1 = tuple()
for s in string:
    tup1 += (int(s),)

rev_number = 0
while num > 0:
    remainder = num % 10
    rev_number = (rev_number * 10) + remainder
    num = num // 10

string = str(rev_number)
tup2 = tuple()
for s in string:
    tup2 += (int(s),)

print(tup1)
print(tup2)


# zad 2
# напишете програма, в която се създава числов списък, той се запълва със случйни числа,
# след това между всяка двойка елементи в този списък се вмъква нов елемент равен на сумата на стойностите от предходните два
import random
random.seed()
list = [random.randint(10, 20) for i in range(16)]
print(list)

for i in range(0, 22, 3):
    list.insert(i+2, list[i]+list[i+1])

print(list)
