class baba:
    car = "BMW"
    money = '200 core'
    home = "2 flat"


class kaka(baba):
    mobile = 'Redmi'
    sim = "Airtel"


b = baba()
print(b.car)

k = kaka()
print(k.car)


# for multiple inheritance >>>>

class kaka2:
    smartPhone= "Apple"
    ac= "Walton"

class mama:
    laptop="HP"
    camera="Studio"


class brother(mama,kaka2,kaka,baba):
    book= "bangabondhu"
    airbuds= "M10"

vai = brother()
print(vai.laptop,vai.car)

# multi-label inheritance >>>>>>>>


class primarySchool:
    one = "one"
    five = "five"


class high(primarySchool):
    six = 'six'
    ten = "ten"


class college(high):
    inter = "first"
    final = "hsc"


class university(college):
    faculty = "BSc"
    department = "Physics"


student1 = university()
print(student1.one,student1.five,student1.department)

# hierarchical inheritance >>>>
print("hierarchical inheritence")

