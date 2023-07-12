print("Break and Continue Method")

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(len(myList)):
    if x == 5:
        break
    print(x)

print("Use of Continue")
for x in range(len(myList)):
    if x == 6:
        continue
    print(x)