# def income() - id, price, quantity: search_id && set_discount(10%) else id=0000 print("zaredi produkta"), calc arg,
# max_price

class product:
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str.format("{} {} {}", self.id, self.price, self.quantity)


def search_id(searched_id, product_list: list):
    for pr in product_list:
        if pr.id == searched_id:
            pr.price = int(pr.price) - int(pr.price) * 10 / 100
            break
    else:
        product_list.append(product(0000, 0, 0))
        print("Зареди продукта")


def calc_avr(product_list: list):
    total = 0
    for pr in product_list:
        total += float(pr.price) * int(pr.quantity)
    return round((total / len(product_list)), 2)


def max_price(product_list: list):
    return sorted(product_list, key=lambda pr: pr.price * pr.quantity, reverse=True)[0]


my_pr_list = [product(121213, 5.89, 142), product(121541, 7.20, 45), product(252827, 8.69, 2)]
search_id(121213, my_pr_list)
search_id(121345, my_pr_list)

print(calc_avr(my_pr_list))
print(max_price(my_pr_list))
