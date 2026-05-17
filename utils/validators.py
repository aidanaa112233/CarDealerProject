import re


def validate_product_name(name):

    pattern = r"^[A-Za-z0-9 ]{2,30}$"

    return re.match(pattern, name) is not None