import datetime

# #1
# year = input("Input a year: ")
# month = input("Input a month [1-12]: ")
# day = input("Input a day [1-31]: ")
# today = str.format("{0} {1} {2}", year, month, day)
#
# next_day = datetime.datetime.strptime(today, '%Y %m %d') + datetime.timedelta(days=1)
# print("The next date is [yyyy-mm-dd] " + str(next_day.date()) + ".")

# # 2.1
# class Travel:
#     def __init__(self, id, dest: str, flight, price: float):
#         self.id = id
#         self.dest = dest
#         self.flight = flight
#         self.price = price
#
#     def reduce(self):
#         if self.price > 200:
#             self.price = round(self.price - self.price * 10 / 100, 2)
#
#     def print(self):
#         print(str.format("ID {} - {}\n Flight: {}\n Price: {} \n", self.id, self.dest, self.flight, self.price))
#
#
# tr_list = [Travel("12B31", "Hamburg", "2:33", 176), Travel("41C7V", "Milan", "1:47", 88), Travel("77ZS2D", "New York", "4:18", 215)]
#
# for tr in tr_list:
#     tr.reduce()
#
# for tr in tr_list:
#     tr.print()
#
#
# # 2.2
# class Travel:
#     def __init__(self, id, dest: str, flight:bool, price: float):
#         self.id = id
#         self.dest = dest
#         self.flight = flight
#         self.price = price
#
#     def reduce(self):
#         if self.price > 200:
#             self.price = round(self.price - self.price * 10 / 100, 2)
#
#     def print(self):
#         print(str.format("ID {} - {}\n Flight: {}\n Price: {} \n", self.id, self.dest, self.flight, self.price))
#
#
# tr_list = [Travel("12B31", "Hamburg", True, 176), Travel("41C7V", "Milan", False, 88), Travel("77ZS2D", "New York", True, 215)]
#
# for tr in tr_list:
#     tr.reduce()
#
# for tr in tr_list:
#     tr.print()


# # 1
# n = int(input())
# odd_li, even_li = list(),list()
# for i in range(n):
#     num = int(input())
#     if num % 2 == 0:
#         even_li.append(num)
#     elif num % 3 == 0 and num % 2 != 0:
#         odd_li.append(num)
#
# min_odd, max_odd = min(odd_li), max(odd_li)
# sum_even, avg_even = sum(even_li), sum(even_li)/len(even_li)


# 2
import json, constants.pr_constants as pr_constants


class GSM:
    def __init__(self, quantity, price, y_dev, brand, model):
        self.quantity = quantity
        self.price = price
        self.y_dev = y_dev
        self.brand = brand
        self.model = model


def sort_gsm(gsm_li):
    return sorted(gsm_li, key=lambda gsm: gsm.quantity)


def to_json(gsm_li):
    for gsm in gsm_li:
        if gsm.brand == "Samsung":
            json_file = "brand_S.json"
            with open(pr_constants.RESOURCES_PATH + json_file, 'a') as file:
                json_data = json.dumps(gsm.__dict__)
                file.write(json_data)
        if gsm.brand == "Apple":
            json_file = "brand_A.json"
            with open(pr_constants.RESOURCES_PATH + json_file, 'a') as file:
                json_data = json.dumps(gsm.__dict__)
                file.write(json_data)


my_gsms = [GSM(12, 500, 2018, "Samsung", "1"), GSM(18, 600, 2019, "Apple", "1"), GSM(4, 689, 2020, "Samsung", "2")]
to_json(sort_gsm(my_gsms))
