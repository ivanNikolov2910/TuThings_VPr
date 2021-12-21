# read document.bin with rb mode, use read and print to print first 4 letters

import constants.pr_constants as pr_constants
import json

doc_file = pr_constants.RESOURCES_PATH + 'document.bin'

with open(doc_file, 'rb') as my_file:
    print(my_file.read(4))

# python to json
json_file = "ex_12_json.json"
my_dict = {"name": "Ivan", "family": "Nikolov", "age": 19}
with open((pr_constants.RESOURCES_PATH+json_file), "w") as file:
    json_data = json.dumps(my_dict)
    file.write(json_data)


# def income() - id, price, quantity: search_id && set_discount(10%) else id=0000 print("zaredi produkta"), calc arg, max_price
