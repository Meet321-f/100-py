# super method :


class Car:
    def __init__(self , type):
        self.type = type

    @staticmethod
    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")

class Toyotacar(Car):
    def __init__(self , name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = Toyotacar("Toyota Camry", "petrol")
print(car1.type)  # Output: petrol

# class method ;

class Person:
    name = "John Doe"

    @classmethod
    def changename(cls , name):
        cls.name = name

p1 = Person()
p1.changename("chandu chempian")
print(p1.name)