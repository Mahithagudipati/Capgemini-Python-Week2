# Inheritance (Multiple, Multi-Level)
# •	6. Implement a multi-level inheritance example where `Vehicle` is a base class, 
# `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`

class Vehicle:
    def __init__(self,name,reg_num):
        self.name=name
        self.reg_num=reg_num
        print(f"The Name of the vehicle is : {self.name}\n Registration number is : {self.reg_num}\n ")
class Bike(Vehicle):
    def bikes(self,name,reg_num,cc,model):
        super().__init__(name,reg_num)
        self.cc=cc
        self.model=model
        print(f"The cc of the bike is : {self.cc}\n The model of the bike is : {self.model} \n")
class Car(Vehicle):
    def __init__(self,name,reg_num,gears):
        super().__init__(name,reg_num)
        self.gears=gears
    def c(self):
        print(f"Number of gears are : {self.gears}")
class ElectricCar(Car):
    def __init__(self,name,reg_num,gears,recharge):
        super().__init__(name,reg_num,gears)
        self.recharge=recharge
    def ec(self):
        Car.c(self)
        print(f"The time taken to recharge is : {self.recharge}")
ecar=ElectricCar("city",1234,4,122)
ecar.ec()