import random
import tkinter as tk
from tkinter import messagebox

secret_number = None
count = 0

def show_answer():
    messagebox.showinfo("Secret number", f"The answer is {secret_number}.")

def new_game():
    global secret_number, count
    secret_number = random.randint(1, 20)
    result_text.set("A new game has started. Good luck!")
    entry.pack()
    submit_button.pack()
    show_answer_button.pack()

def check_answer(guess):
    global count
    count += 1
    if int(secret_number) < int(guess):
        result_text.set("No, it is too big.")
    elif int(secret_number) > int(guess):
        result_text.set("No, it is too small.")
    else:
        result_text.set(f"You are right! It took you {count} attempts to win the game. Start a new game to continue.")     

def exit_game():
    result_text.set("See you next time!")
    app.destroy()

# GUI setup
app = tk.Tk()
app.title("Number Guessing Game")

label = tk.Label(app, text="Hello! You will need to guess a randomly generated number from 1 to 20.", font=("Arial", 14), fg="#1c3f4a")
label.pack()

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

new_game_button = tk.Button(button_frame, text="New Game", command=new_game, bg="#ce84b6", fg="#38014a", font=("Arial", 12), width=12)
new_game_button.pack(side=tk.LEFT, padx=5)

game_exit = tk.Button(button_frame, text="Exit the game", command=exit_game, bg="#ce84b6", fg="#38014a", font=("Arial", 12), width=12)
game_exit.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(app, width=30)
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 12), fg="#1c3f4a")
result_label.pack(pady=10)

submit_button = tk.Button(app, text="Submit", command=lambda: check_answer(entry.get()), bg="#44abbb", fg="#1c3f4a", font=("Arial", 12), width=12)
show_answer_button = tk.Button(app, text="Show Answer", command=show_answer, bg="#44abbb", fg="#1c3f4a", font=("Arial", 12), width=12)

app.mainloop()
