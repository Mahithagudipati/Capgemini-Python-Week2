# •	9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `Airplane`.
#  Handle potential conflicts in the `move()` method.
class Car:
    def move(self):
        print("I can drive")
class Airplane:
    def move(self):
        print("I can fly")

class FlyingCar(Car,Airplane):
    def move(self, Move):
        if(Move == 'drive'):
            super().move()
        else:
            Airplane.move(self)

f=FlyingCar()
f.move("drive")
f.move("fly")