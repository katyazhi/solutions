import random


# some words for intro
def instructions():
    print("Hello! You will need to guess a randomly generated number from 1 to 20.")
    print("During the game you can use commands:")
    commands = [
        "x - exit the programm",
        "n - stop the current game",
        "s - show the answer",
    ]
    for item in commands:
        print(item)


# one function for all kind of inputs so that short_commands work at any time
def answers(secret_number):
    new_answer = input()
    if new_answer == "x" or new_answer == "n" or new_answer == "s":
        execute_short_commands(new_answer, secret_number)
        new_answer = "no_answer"
    return new_answer


# starting new game, designed that way so that if user accidentally types something else except of no/yes programm will ask them again.
# if user applies short commands at that point, they also work.
# Command s givew output that answer is not defined yet and that user should start the game.
def new_game(secret_number):
    print("Are you ready for the new game? Type yes or no: ")
    new_answer = answers(secret_number)
    if new_answer == "no":
        print("See you next time!")
        exit()
    elif new_answer == "yes":
        game(secret_number)


# loop for the game which takes into account that answer can be short command instead of number.
def game(secret_number):
    secret_number = random.randint(1, 20)
    count = 0
    while True:
        print("Guess the number: ")
        new_answer = answers(secret_number)
        if new_answer.isnumeric() == True:
            count += 1
            if secret_number < int(new_answer):
                print("No, it is too big.")
            if secret_number > int(new_answer):
                print("No, it is too small.")
            if secret_number == int(new_answer):
                print(f"You are right! It took you {count} attempts to win the game.")
                break


# separate function for short command execution
def execute_short_commands(letter, secret_number):
    if letter == "s":
        print(f"The answer is {secret_number}.")
    if letter == "x":
        print("See you next time!")
        exit()
    if letter == "n":
        new_game(secret_number)


# combined functions
def main():
    instructions()
    while True:
        secret_number = "not defined. Start a new game"
        new_game(secret_number)


main()
