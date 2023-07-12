import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1, 6))
    PlayAgain = input("DO WANNA ROLL AGAIN Y/N")
    if PlayAgain == "y":
        continue
    else:
        break

