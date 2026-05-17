class Product:
    """Base product class"""

    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def total_value(self):
        return self.__price * self.__quantity

    def display_info(self):
        return f"ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price}, Quantity: {self.__quantity}"