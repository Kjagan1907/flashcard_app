import tkinter as tk
import random
import pandas as pd
import csv

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FLASHCARD LOGIC ------------------------------- #
try:
    data = pd.read_csv("unknown_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("frequent_germanwords.csv")
    dictionary = original_data.to_dict(orient="records")
else:
    dictionary = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_front, image=card_back_img)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(german_card, text=flashcard["English"], fill="white")



def card():
    global flashcard, timer
    window.after_cancel(timer)
    flashcard = random.choice(dictionary)
    canvas.itemconfig(card_front, image=card_front_img)
    canvas.itemconfig(lang, text="German", fill="black")
    canvas.itemconfig(german_card, text=flashcard["German"], fill="black")
    timer = window.after(3000, flip_card)

def known_word():
    dictionary.remove(flashcard)
    print(len(dictionary))
    new_data = pd.DataFrame(dictionary)
    new_data.to_csv("unknown_words.csv", index=False)
    card()    


# ---------------------------- GUI -------------------------------- #
window = tk.Tk()
window.title("German Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="card_front.png")   
card_back_img = tk.PhotoImage(file="card_back.png")
card_front = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
lang = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
german_card = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



right_image = tk.PhotoImage(file="right.png")
wrong_image = tk.PhotoImage(file="wrong.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=card)
wrong_button.grid(row=1, column=0)

window.mainloop()