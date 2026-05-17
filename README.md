# Car Dealer Management System

## Project Description
This is a collaborative Python project for a car dealer system.  
The system allows users to add cars, remove cars, show available cars, save and load data, record sales, and calculate total sales.

## Main Features
- Add car
- Remove car
- Show cars
- Save data to JSON
- Save sales to CSV
- Calculate total inventory value
- Calculate total sales
- Use iterator
- Use regex validation
- Use decorators
- Use unit tests

## Technologies Used
- Python
- JSON
- CSV
- Regex
- unittest
- OOP

## OOP Concepts
### Encapsulation
Private attributes are used in the Product class.

### Inheritance
SpecialProduct inherits from Product.

### Polymorphism
display_info() method is overridden.

### Association
InventoryManager manages Product objects.

## Functional Programming
The project uses:
- lambda
- map
- filter

## Decorator
A custom decorator @log_action is used to log system actions.

## Iterator and Generator
The project includes ProductIterator and expensive_products generator.

## File Handling
- products.json stores product/car data
- sales.csv stores sales data

## Team Members

### Student 1: Logic and OOP Lead
Responsible for:
- OOP classes
- Encapsulation
- Inheritance
- Polymorphism
- Regex validation
- Decorator
- Unit tests

### Student 2: Data Storage and UI Lead
Responsible for:
- CSV and JSON file handling
- CLI menu
- Main integration
- Iterator and generator

## How to Run
```bash
python main.py