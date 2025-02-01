# •	4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. 
# Write a method to return student details.

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def display(self):
        print(f"Student's name is : {self.name}\n Student's Roll number is : {self.roll_number}")

s=Student("haran",22)
s.display()
