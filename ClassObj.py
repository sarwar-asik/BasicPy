# every class have __init__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Jhon", 54)

print(person1)

print("class with str")


# class with __str__ function
class Person2:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years"


p1 = Person("John", 36)

print(p1)
