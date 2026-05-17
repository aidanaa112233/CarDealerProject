import unittest

from models.product import Product
from managers.inventory_manager import InventoryManager
from utils.validators import validate_product_name


class TestInventorySystem(unittest.TestCase):
    """Unit tests for Car Dealer Management System."""

    def setUp(self):

        self.product = Product(
            1,
            "BMW X5",
            50000,
            2
        )

        self.inventory = InventoryManager()

    def test_product_name(self):

        self.assertEqual(
            self.product.get_name(),
            "BMW X5"
        )

    def test_total_value(self):

        self.assertEqual(
            self.product.total_value(),
            100000
        )

    def test_add_product(self):

        self.inventory.add_product(self.product)

        self.assertEqual(
            len(self.inventory.products),
            1
        )

    def test_validation_true(self):

        self.assertTrue(
            validate_product_name("Toyota Camry")
        )

    def test_validation_false(self):

        self.assertFalse(
            validate_product_name("@")
        )


if __name__ == "__main__":
    unittest.main()
