MySet = {1, False, 'string', 'string'}
print(MySet, type(MySet))
numSet = {1, 3, 2, 6, 4, 8, 5}

# Access a set
for i in numSet:
    print(i)

print(3 in numSet)

# addd item in set or add multiple set

numSet.add(10)
print(numSet)

newList = {'100', '200'}
numSet.update(newList)
print('updated set', numSet)

### remove item from set ###
numSet.remove(2)
R
print('removed set', numSet)

