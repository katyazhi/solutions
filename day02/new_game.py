import random
print("Hello! You will need to guess a randomly generated number from 1 to 20.")
game = input("Are you ready for the new game? Type yes or no: ")
while game.lower() == ("yes"):
    answer = random.randint(1, 20)
    number = None
    count = 0
    while answer != number:
        number = int(input("Guess the number: "))
        count += 1
        if answer < number:
            print("No, it is too big.")
        if answer > number:
            print("No, it is too small.")
    print(f"You are right! It took you {count} attempts to win the game.")
    game = input("Are you ready for the new game? Type yes or no: ")
else: print("See you next time!")
