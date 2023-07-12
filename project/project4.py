answer = input("do wanna to play the game ? [yes/no]")

if answer == 'yes':
    print("welcome to the game")
    answer = input("wanna jungle/cave")
    if answer == "jungle":
        print('you see the hungry tiger')
    elif answer == "cave":
        print("you can see a bear")
        answer = input("will you fight against the bear[fight/run]")
        if answer == "fight":
            print('bear is too strong . You lose the game')
        else:
            print("wow! You will alive.")

else:
    print("the game closed")