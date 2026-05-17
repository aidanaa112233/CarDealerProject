# Car Dealer Management System

## Project Overview

This project is a Car Dealer Management System written in Python.
The system allows users to manage cars/products, add and remove items, save and load data from files, record sold cars, and calculate total inventory and sales values.

The project follows a modular architecture. Each part of the system is divided into separate packages and files.

## Main Features

- Add new cars/products
- Show all cars/products
- Remove cars/products by ID
- Save products to JSON file
- Load products from JSON file
- Record sold cars
- Save sales data to CSV file
- Calculate total sales
- Calculate total inventory value
- Validate product names using Regex
- Use decorators to log actions
- Use iterator/generator for product processing
- Test the system using unittest

## Project Structure

```text
CarDealerProject/

├── data/
│   ├── products.json
│   └── sales.csv
│
├── managers/
│   ├── __init__.py
│   ├── inventory_manager.py
│   └── sales_manager.py
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   └── special_product.py
│
├── tests/
│   ├── __init__.py
│   └── test_system.py
│
├── utils/
│   ├── __init__.py
│   ├── decorators.py
│   ├── generators.py
│   └── validators.py
│
├── main.py
├── README.md
└── requirements.txt
```

## Class Hierarchy

### Product

`Product` is the base class of the system.
It stores basic information about a car/product:

- product ID
- name
- price
- quantity

It also uses encapsulation with private attributes and getter methods.

### SpecialProduct

`SpecialProduct` inherits from `Product`.
It represents a product with a discount.

This demonstrates inheritance and polymorphism because `SpecialProduct` overrides the `display_info()` method.

### InventoryManager

`InventoryManager` manages the list of products.

Functions:

- add products
- remove products
- show products
- calculate total inventory value
- filter expensive products
- save products to JSON
- load products from JSON

### SalesManager

`SalesManager` manages sold cars/products.

Functions:

- add sales
- calculate total sales
- save sales to CSV

## Functional Programming

The project uses functional programming tools:

- lambda
- map
- filter

They are used for calculating inventory value and filtering expensive products.

## File Handling

The project uses:

- JSON for saving and loading product data
- CSV for saving sales data

Files are stored in the `data/` folder.

## Decorator

The project includes a custom decorator called `log_action`.

It logs important actions such as adding products, removing products, and adding sales.

## Regex Validation

The project uses the `re` module to validate product names.

Example:

```python
validate_product_name("Toyota Camry")
```

This helps prevent invalid input.

## Iterator and Generator

The project includes:

- `ProductIterator`
- `expensive_products()` generator

They are used to process product lists efficiently.

## Testing

The project includes unit tests using the `unittest` module.

There are 5 tests:

- product name test
- total value test
- add product test
- validation true test
- validation false test

All tests pass successfully.

## How to Run the Project

Run this command:

```bash
python main.py
```

Then choose an option from the menu:

```text
1. Add Product
2. Show Products
3. Remove Product
4. Save Products
5. Load Products
6. Add Sale
7. Total Sales
8. Total Inventory Value
9. Iterator Demo
0. Exit
```

## How to Run Tests

Run this command:

```bash
python -m unittest tests/test_system.py
```

Expected result:

```text
Ran 5 tests

OK
```

## Group Members and Responsibilities

### Student 1: Lead of Core Logic & OOP

Student 1 was responsible for the main logic and object-oriented structure of the system.

Responsibilities:

- Created the base `Product` class
- Created the inherited `SpecialProduct` class
- Used encapsulation with private attributes
- Implemented inheritance and polymorphism
- Added product calculation logic
- Used lambda, map, and filter
- Created Regex validation
- Created the custom decorator
- Wrote 5 unit tests

### Student 2: Lead of Data Storage & UI

Student 2 was responsible for file handling, user interface, and system integration.

Responsibilities:

- Created JSON file saving and loading
- Created CSV file saving for sales
- Created the menu system in `main.py`
- Used while loop for the CLI menu
- Added options for adding, removing, saving, loading, and calculating
- Created iterator/generator logic
- Integrated all modules into `main.py`
- Checked that the project runs correctly

## Quality Assurance

The project follows basic PEP8 style rules.
The code is divided into modules and packages.
Error handling is used for invalid input and missing files.
Unit tests passed successfully.

## Conclusion

This Car Dealer Management System demonstrates Python programming concepts such as OOP, file handling, collections, functional programming, decorators, regex, iterators, generators, modular structure, and testing.
