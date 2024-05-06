import random
print("Hello! You will need to guess a randomly generated number from 1 to 20.")
while True:
    game = input("Are you ready for the new game? Type yes or no: ")
    if game.lower() != "yes":
        print("See you next time!")
        break
    answer = random.randint(1, 20)
    count = 0
    while True:
        number = int(input("Guess the number: "))
        count += 1
        if answer < number:
            print("No, it is too big.")
        if answer > number:
            print("No, it is too small.")
        if answer == number:
            print(f"You are right! It took you {count} attempts to win the game.")
            break