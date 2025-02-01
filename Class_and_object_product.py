# •	5. Create a `Product` class with attributes `name`, `price`, and `stock`. 
# Write a method `check_availability(quantity)` that returns whether the requested quantity is available.

class Product:
        def __init__(self,name,price,stock=30):
            self.name=name
            self.price=price
            self.stock=stock
        def check(self,quantity):
            self.quantity=quantity
            if(self.stock>=quantity):
                print(f"The quantity of {self.name} protien powder you have requested is available ")
                
            else:
                print("out of stock")

p=Product("mb",100,10)
p.check(10)
p.check(14)
                

   