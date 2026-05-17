
from models.product import Product
from models.special_product import SpecialProduct

from managers.inventory_manager import InventoryManager
from managers.sales_manager import SalesManager

from utils.validators import validate_product_name
from utils.generators import ProductIterator


def menu():

    inventory = InventoryManager()
    sales = SalesManager()

    while True:

        print("\n===== INVENTORY SYSTEM =====")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Remove Product")
        print("4. Save Products")
        print("5. Load Products")
        print("6. Add Sale")
        print("7. Total Sales")
        print("8. Total Inventory Value")
        print("9. Iterator Demo")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":

            try:

                product_id = int(input("Enter ID: "))
                name = input("Enter name: ")

                if not validate_product_name(name):
                    print("Invalid product name.")
                    continue

                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))

                product = Product(
                    product_id,
                    name,
                    price,
                    quantity
                )

                inventory.add_product(product)

                print("Product added successfully.")

            except ValueError:
                print("Invalid input.")

        elif choice == "2":

            inventory.show_products()

        elif choice == "3":

            product_id = int(
                input("Enter product ID to remove: ")
            )

            inventory.remove_product(product_id)

            print("Product removed.")

        elif choice == "4":

            inventory.save_to_json(
                "data/products.json"
            )

            print("Products saved.")

        elif choice == "5":

            inventory.load_from_json(
                "data/products.json"
            )

            print("Products loaded.")

        elif choice == "6":

            name = input("Product name: ")
            quantity = int(input("Quantity sold: "))
            total = float(input("Total price: "))

            sales.add_sale(name, quantity, total)

            sales.save_sales_csv(
                "data/sales.csv"
            )

            print("Sale recorded.")

        elif choice == "7":

            print(
                f"Total sales: ${sales.total_sales()}"
            )

        elif choice == "8":

            print(
                f"Inventory value: ${inventory.total_inventory_value()}"
            )

        elif choice == "9":

            iterator = ProductIterator(
                inventory.products
            )

            for item in iterator:
                print(item.display_info())

        elif choice == "0":

            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()