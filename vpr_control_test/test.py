import datetime


# #1
# year = input("Input a year: ")
# month = input("Input a month [1-12]: ")
# day = input("Input a day [1-31]: ")
# today = str.format("{0} {1} {2}", year, month, day)
#
# next_day = datetime.datetime.strptime(today, '%Y %m %d') + datetime.timedelta(days=1)
# print("The next date is [yyyy-mm-dd] " + str(next_day.date()) + ".")

# 2.1
class Travel:
    def __init__(self, id, dest: str, flight, price: float):
        self.id = id
        self.dest = dest
        self.flight = flight
        self.price = price

    def reduce(self):
        if self.price > 200:
            self.price = round(self.price - self.price * 10 / 100, 2)

    def print(self):
        print(str.format("ID {} - {}\n Flight: {}\n Price: {} \n", self.id, self.dest, self.flight, self.price))


tr_list = [Travel("12B31", "Hamburg", "2:33", 176), Travel("41C7V", "Milan", "1:47", 88), Travel("77ZS2D", "New York", "4:18", 215)]

for tr in tr_list:
    tr.reduce()

for tr in tr_list:
    tr.print()


# 2.2
class Travel:
    def __init__(self, id, dest: str, flight:bool, price: float):
        self.id = id
        self.dest = dest
        self.flight = flight
        self.price = price

    def reduce(self):
        if self.price > 200:
            self.price = round(self.price - self.price * 10 / 100, 2)

    def print(self):
        print(str.format("ID {} - {}\n Flight: {}\n Price: {} \n", self.id, self.dest, self.flight, self.price))


tr_list = [Travel("12B31", "Hamburg", True, 176), Travel("41C7V", "Milan", False, 88), Travel("77ZS2D", "New York", True, 215)]

for tr in tr_list:
    tr.reduce()

for tr in tr_list:
    tr.print()