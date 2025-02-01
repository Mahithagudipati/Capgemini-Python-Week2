#•	8. Design a system where a base class `Animal` 
#has a method `speak()`, and subclasses `Dog` and `Cat` override it.
class Animal:
    def speak(self):
        print("Barks,meows")

class Dog(Animal):
        def speak(self):
            print("woof woof")
class Cat(Animal):
        def speak (self):
            print("meow meow")

a=Animal()
d=Dog()
c=Cat()


d.speak()
c.speak()