from itertools import product
from re import match

def  product_name_validator(product_name):
    if match(r"[a-zA-Z0-9-]",product_name):
        return product_name
    else:
        raise ValueError("Invalid product_name !!!")

