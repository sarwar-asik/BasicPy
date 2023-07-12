list1 = [1, 2, 3]
print(list1)
# for in loop ###
for i in list1:
    i += 200
    print(i)

# list *****  append and insert
habu = ['alu', 'balu', 'tal', 'nlu']
# add in list
habu.append(10)
# habu.insert(2, 'inu')

# ********remove from list by remove ,pop,del,clear
# habu.clear()
habu.remove('balu')
habu.pop(2)

habu.pop()
del habu[1]
print(habu)

# ******** loop in an array
langList = ['bangle', 'english', 'purdu', 'turkey', 'hondu']
print('for  in loop """"')
for lang in langList:
    print(lang, ',')

print('for in loop with index>>>>')
for i in range(len(langList)):
    print(i)

print("while loop in list")
y = 0
while y < len(langList):
    print(langList[y])
    y = y + 1

print('list comprehension ----===')
numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in numbersList:
#     print(i*3)
Double = [i + 2 for i in numbersList]
print(Double)

print('sort a List>>>>>>>> ')
number1 = [20, 10, 30, 40, 80, 50, 60, 40]
# number1.sort()
# print(number1)
number1.sort(reverse=True)
print(number1)

print('Copy  A list >>>>>>>>>')
number2 = number1.copy()
print("copied number", number2)
print("Join 2 list ")
num1 = [1, 2, 3, 4, 5, 6]
num2 = [7, 8, 9, 10]
numJoined = num1 + num2
print(numJoined)
# ### or ####
num1.extend(num2)
print(num1)
