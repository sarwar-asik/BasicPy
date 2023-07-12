import random

RandomNumber = random.randrange(1, 200)
userInput = int(input("Guess the Number :"))


print("randomNumber",RandomNumber)
if userInput > RandomNumber:

    print("the number is too high")
elif RandomNumber> userInput:
    print("The number is too low")
else:
    print("Yes ! You matched the number .")
