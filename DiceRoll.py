import random


print("Press any key to roll the dice")
input()
num = random.randint(1, 6)
if num == 1:
    print("|---------|")
    print("|         |")
    print("|    o    |")
    print("|         |")
    print("|---------|")
    print("You rolled a 1!")
if num == 2:
    print("|---------|")
    print("|         |")
    print("|  o   o  |")
    print("|         |")
    print("|---------|")
    print("You rolled a 2!")
if num == 3:
    print("|---------|")
    print("|         |")
    print("|  o o o  |")
    print("|         |")
    print("|---------|")
    print("You rolled a 3!")
if num == 4:
    print("|---------|")
    print("|   o  o  |")
    print("|         |")
    print("|   o  o  |")
    print("|---------|")
    print("You rolled a 4!")
if num == 5:
    print("|---------|")
    print("|  o   o  |")
    print("|    o    |")
    print("|  o   o  |")
    print("|---------|")
    print("You rolled a 5!")
if num == 6:
    print("|---------|")
    print("|  o   o  |")
    print("|  o   o  |")
    print("|  o   o  |")
    print("|---------|")
    print("You rolled a 6!")
