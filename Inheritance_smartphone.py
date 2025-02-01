# •	10. Build a `SmartPhone` class inheriting from `MobileDevice`,
#  which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    def __init__(self,type):
        self.type=type
    def display(self):
        print("The type is ",self.type)
class MobileDevice(Electronics):
    def display(self):
        print("mobile device")
class SmartPhone(MobileDevice):
    def display(self):
       print("The smart phone",self.type)
e=Electronics("Washing machine")
m=MobileDevice("nokia")
s=SmartPhone("iphone")

s.display()