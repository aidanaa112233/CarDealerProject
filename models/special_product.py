from models.product import Product


class SpecialProduct(Product):

    def __init__(self, product_id, name, price, quantity, discount):
        super().__init__(product_id, name, price, quantity)
        self.discount = discount

    def discounted_price(self):
        return self.get_price() * (1 - self.discount / 100)

    def display_info(self):
        return (
            f"{super().display_info()}, Discount: {self.discount}%"
        )