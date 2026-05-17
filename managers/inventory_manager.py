import json

from models.product import Product
from models.special_product import SpecialProduct
from utils.decorators import log_action


class InventoryManager:

    def __init__(self):
        self.products = []

    @log_action
    def add_product(self, product):
        self.products.append(product)

    @log_action
    def remove_product(self, product_id):

        self.products = [
            p for p in self.products
            if p.get_id() != product_id
        ]

    def show_products(self):

        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):

        return sum(
            map(lambda p: p.total_value(), self.products)
        )

    def filter_expensive_products(self, limit):

        return list(
            filter(lambda p: p.get_price() > limit, self.products)
        )

    def save_to_json(self, filename):

        data = []

        for p in self.products:

            data.append({
                "id": p.get_id(),
                "name": p.get_name(),
                "price": p.get_price(),
                "quantity": p.get_quantity()
            })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename):

        try:

            with open(filename, "r") as file:

                data = json.load(file)

                for item in data:

                    product = Product(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["quantity"]
                    )

                    self.products.append(product)

        except FileNotFoundError:
            print("JSON file not found.")