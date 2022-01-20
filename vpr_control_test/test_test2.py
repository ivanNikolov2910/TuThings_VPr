import json


class GSM_Mobile_Devices:
    def __init__(self, quantity, price, year, make, model):
        self.quantity = quantity
        self.price = price
        self.year = year
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} model {self.model} price {self.price} and {self.quantity} quantity"


gsm = [GSM_Mobile_Devices(45, 100, 2010, 'Nokia', '3310'),
       GSM_Mobile_Devices(20, 400, 2012, 'iPhone', '11 Pro'),
       GSM_Mobile_Devices(30, 150, 2015, 'Nokia', '5310'),
       GSM_Mobile_Devices(15, 200, 2021, 'Nokia', "6300")]


def sort_gsm(gsm_list):
    gsm_list.sort(key=lambda x: x.quantity)

    for obj in gsm:
        print(obj)


def find_model(make, gsn_list):
    same_make = []
    for obj in gsn_list:
        if obj.make == make:
            same_make.append(obj)

    with open("file_phones.json", "a") as f:
        json_data = list()
        for obj in same_make:
            json_data.append(obj.__dict__)
        f.write(json.dumps(json_data))


print('\n---sorted---')
#sort_gsm(gsm)

print('\n---same manufacturer---')
find_model('Nokia', gsm)


f = open("file_phones.json", "r")
raw_data = f.read()
gsm_list = json.loads(raw_data)
print()