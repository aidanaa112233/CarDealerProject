import csv

from utils.decorators import log_action


class SalesManager:

    def __init__(self):
        self.sales = []

    @log_action
    def add_sale(self, product_name, quantity, total_price):

        sale = {
            "product": product_name,
            "quantity": quantity,
            "total": total_price
        }

        self.sales.append(sale)

    def total_sales(self):

        return sum(
            sale["total"]
            for sale in self.sales
        )

    def save_sales_csv(self, filename):

        with open(filename, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["product", "quantity", "total"]
            )

            writer.writeheader()

            for sale in self.sales:
                writer.writerow(sale)