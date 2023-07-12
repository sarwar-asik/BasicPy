# normal funtion
# def summu(a, b):
#     sum = a + b
#     print(sum)
#
#
# summu(10, 20)

# lamda function
summu2 = lambda a, b,c: a+b-c
print(summu2(30, 50,20))


# normal function with lamda
def myfunc(n):
    return lambda a: a*n


toDouble = myfunc(30)
print(toDouble(10))