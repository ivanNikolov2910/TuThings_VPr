class MyClass:
    i = 1234  # static int i = 1234 -> Java based

    # def __init__(self):  # constructor
    #     self.data = []  # List<> data -> field -> Java based

    # Only 1 constructor
    def __init__(self, data):
        self.data = data

    def f(self):
        return 'Hello OOP!'

    def add_data(self, data):
        self.data += data


# obj1 = MyClass()
data = [1, 2, 3, 4, 5, 6]
obj2 = MyClass(data)

# print(obj1.i, obj1.f(), obj1.f)
# print(obj1.data)
obj2.add_data([1, 2, 3, 4, 5, 6])
print(obj2.data)
