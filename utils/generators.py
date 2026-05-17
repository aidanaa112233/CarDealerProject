class ProductIterator:

    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.products):
            result = self.products[self.index]
            self.index += 1
            return result

        raise StopIteration


def expensive_products(products, limit):

    for product in products:

        if product.get_price() > limit:
            yield product