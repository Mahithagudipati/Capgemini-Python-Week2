# •	7. Create a multi-level class structure with `Person` → `Employee` → `Manager`,
#  where `Manager` has an additional method `approve_leave()`.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,experience):
        super().__init__(name,age)
        self.experience=experience
class Manager(Employee):
    def __init__(self,name,age, experience,type):
        super().__init__(name,age,experience)
        self.type=type
        print(f"name : {self.name}, age : {self.age} , experience : {self.experience}, type : {self.type}")
    def approve_leave(self):
        print("Your leave is approved")

m=Manager("harika",21,"1 month","intern")
m.approve_leave()
        
