import pickle

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_Name(self):
        return self.name

    def get_Age(self):
        return self.age


person = Person('Ashe', 20)
print(person.get_Name())
print(person.get_Age())

with open('Ashe', 'wb') as f:
    pickle.dump(person, f)

with open('Ashe', 'rb') as f2:
    ashe = pickle.load(f2)

print(ashe.get_Name)
print(ashe.get_Age)

