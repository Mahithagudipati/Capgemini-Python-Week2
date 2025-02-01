# Class and Object
# •	1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.
# •	2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
# •	3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
# •	4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
# •	5. Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.

#1
while True:
    class Employee:
        def __init__(self,name,id,department):
            self.name=name
            self.id=id
            self.department=department
        def get_details(self):
            print(f"The employee details are :\n Name:{self.name}\n Id : {self.id}\n Department: {self.department}\n")
    name=input("Enter the name of the employee : ")
    id=input("Enter the Id of the employee : ")
    department=input("Enter the department of the employee : ")
    obj=Employee(name,id,department)
    obj.get_details()
