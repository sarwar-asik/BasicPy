print('interators>>>>>')

MyList = [1, 2, 3, 4, "Zinku", 'Tinku', 'ponku']

# for i MyList:
#    print(i)

x = iter(MyList)
print(x.__next__())
print(x.__next__())
print(x.__next__())
# or
print(next(x))
print(next(x))
print(next(x))





