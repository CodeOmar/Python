import random

print("Welcome to RPS!")
player = input("Rock (r), Paper (p) or scissors (s)")
if player != 'r' and player != 'p' and player != 's':
    print("Invalid! Please restart!")
    exit()
else:
    print(player, 'vs', end=' ')

chosen = random.randint(1, 3)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'
print(computer)

if player == computer:
    print("DRAW")
elif player == 'r' and computer == 's':
    print("Player wins!")
elif player == 'r' and computer == 'p':
    print("Computer wins!")
elif player == 'p' and computer == 'r':
    print("Computer wins!")
elif player == 'p' and computer == 's':
    print("computer wins!")
elif player == 's' and computer == 'r':
    print("Computer wins!")
elif player == 's' and computer == 'p':
    print("Player wins!")
