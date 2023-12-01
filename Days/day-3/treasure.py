print("Welcome to the Treasure Island.\n Your mission is to find the treasure.")
left_right = input("left or right?\n")
if left_right == "left":
    swim_wait = input("swim or wait?\n")
    if swim_wait == "wait":
        color = input("Which door?\n")
        if color == "yellow":
            print("You win!")
        elif color == "red":
            print("Burned by fire. \n Game Over.")
        elif color == "blue":
            print("Eaten by beasts. \n Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. \n Game Over.")
else:
    print("Fall into a hole \n Game Over.")