from tkinter import *
import pandas
import random

LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
PALE_GREEN = "#b1ddc6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = pandas.DataFrame.to_dict(original_data, orient="records")
else:
    to_learn = pandas.DataFrame.to_dict(data, orient="records")


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=front_img)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    new_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=PALE_GREEN)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=PALE_GREEN, highlightthickness=0)
lang_text = canvas.create_text(400, 150, text="", fill="black", font=LANG_FONT)
word_text = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=PALE_GREEN, command=is_known)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=PALE_GREEN, command=new_card)
wrong_button.grid(column=0, row=1)

new_card()

window.mainloop()
