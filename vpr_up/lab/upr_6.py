# zad 1 Въвежда текст и създава речник с клюя - буквите и стойност - колко пъти се срещат
string = input("Add string: ")
my_dict = dict()

for letter in string:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


# zad 2: Въвежда се цяло число => списък с числата от 1 до n => list(1,2,3,4) => dict s keys 1,2,3,4 val = 4,3,2,1
num = int(input("Enter a number:"))
keys = list(i for i in range(1, num + 1))
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = keys[len(keys) - i - 1]

print(my_dict)
