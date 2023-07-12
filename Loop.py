print("Loop in Python ")

# there are 2 loop in python "for" and "while"

Cost = 0
while Cost < 10:
    print("cost is running",Cost)
    Cost = Cost+1

print("For in  loop ")
fruits =['apple', 'banana', 'potato', 'orange', 'jackFruit']
for fruit in fruits:
    print(fruit)


# loop with condition
print("loop and condition >>>>>>>>>>>")
for h in fruits:
    if h == 'potato':
        break
    print(h)