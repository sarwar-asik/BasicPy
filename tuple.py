myTuple = ('one', 2, 3, 5, 'seven', False, True)
# print(myTuple, type(myTuple))
# print(myTuple[4])
# print(myTuple[-2])
# # Range of index of Tuple >>>>>
# print(myTuple[1:4])

# change the tuple to list >>>
myTuple2 = ('one', 'two', 'three', 'four', 'five')
a = list(myTuple2)
a.append('newItem')
# print(type(a))
# print(a)

# unpack(distructure) and spreed operator a tuple >>>>

fruits = ('apple', 'banana', "cherry", 'orange')
print(fruits)
# (x,y,z,t) = fruits
# print(x,y)

(x, *y,) = fruits
print(x, y)

##tuple loop >>>>>>>
for i in fruits:
    print(i)

for x in range(len(fruits)):
    print(x)

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# join tuple
print("Join Tuple +++++===")

myJoined = myTuple + fruits

myJoined2 = myTuple * 3

print(myJoined)
print(myJoined2)
# count tuple number
count1 = myJoined2.count(2)
indexing = myJoined2.index('seven')
print(count1)
print(indexing)
