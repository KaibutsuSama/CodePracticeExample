class Animal:
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        super(Dog, self).__init__()

        print("Dog Craete")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof")


d = Dog()
d.whoAmI()
d.eat()
d.bark()
