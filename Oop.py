class ParentsInfo:
    def __init__(self, name, number):
        print(f"I am {name} and {number}")

    def YourName(self,age):
        self.age = age

    @classmethod
    def MyName(LMS):
        print('Hello Python')




p1 = ParentsInfo('Sarwar', 17233342)
p1.MyName()


print("Polymorphism >>>>>>>>>")


class Vehicle:
    def __init__(self, model, brand, component):
        self.__model = model
        # user __model for mutable
        self.brand = brand
        self.component = component


v = Vehicle("asdfc","AMW",'one compo')
# v.model =  "HMW"
print(v.brand)


class Plane(Vehicle):
    pass


a = Plane("as12", 'BMW', "all component")
a.model ="CHanged "
print(a.brand,a.model,a.component)