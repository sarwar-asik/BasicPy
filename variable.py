# strings
myName = "Sarwar Hossain"
# integer
age = 24
print(myName, "is string ", age, 'is integer', type(myName))
# complex
print(type(112342j))
# boolean
married = False

# concat (only string)
print('my name is ' + "sarwar" )

#  condition //

classes = 16

age > classes
print("Your age is greater")

# ternary operator
print(f'my name is {myName} and my age {age}')


#  array or list //
x = ["apple", "banana", "cherry"]

print(type(x))

# range /

print(range(10, 100))

#  byte (immutable . can not change it )
classList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 00]

classList = bytes(classList)
# classList[3] = 340 cant revalue

print(type(classList), 'classLists')

# bytearray

a = bytearray(classList)
a[5] = 100
print("Bytearray are", a[5])

#  NoneType ;;

myJob = None
print(type(None))



# for loop
myData = [10, 20, 30]

for i in myData:
    print(i)