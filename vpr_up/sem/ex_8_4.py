# Дефинирайте  клас Pnone със следните полета : марка, модел, цена, количество. В класа е дефиниран и метод ,
# който принтира стойностите на полетата. Създайте функция, която връща списък с обекти от класа Pnone . Принтирайте
# информация за телефона с максимална цена. Намерете средноаритметичното от цените на всички телефони в списъка.
# Изведете списък на всички телефони от дадена марка ( въвежда се от клавиатурата ).

class Pnone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = int(price)
        self.quantity = int(quantity)

    def __str__(self):
        return str.format("{} {}: {}, Quantity: {}", self.brand, self.model, self.price, self.quantity)


def get_phones(size):
    res = list()
    for i in range(size):
        res.append(Pnone(input("Brand: "), input("Model: "), input("price: "), input("Quantity: ")))
    return res


def get_max_pr(ph_list: list):
    ph_list.sort(key=lambda el: el.price, reverse=True)
    return ph_list[0]


def get_arg_price(ph_list: list):
    count, total, = 0, 0
    for i in ph_list:
        count += i.quantity
        total += i.price * i.quantity
    return total / count


def get_brand(ph_list: list, brand):
    res = list()
    for i in ph_list:
        if i.brand == brand:
            res.append(i)
    return res


my_list = get_phones(2)
print(get_max_pr(my_list))
print(get_arg_price(my_list))
print(get_brand(my_list, input("Brand: ")))
