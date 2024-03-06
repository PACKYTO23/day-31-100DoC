from tkinter import *
import pandas
import random

TIMER = None

data = pandas.read_csv("data/french_words.csv")
data_frame = pandas.DataFrame.to_dict(data, orient="records")


def new_card():
    words_data = random.choice(data_frame)
    french_word = words_data["French"]
    english_word = words_data["English"]
    canvas.itemconfig(lang_text, text="French")
    canvas.itemconfig(word_text, text=french_word)

    window.after_cancel(TIMER)
    count_down()

    return english_word


def count_down(count=1):
    global TIMER
    TIMER = window.after(5000, count_down, count - 1)

    if count == 0:
        canvas.itemconfig(card_img, image=back_img)
        canvas.itemconfig(lang_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=new_card, fill="white")
        window.after_cancel(TIMER)


LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
PALE_GREEN = "#b1ddc6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=PALE_GREEN)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=PALE_GREEN, highlightthickness=0)
lang_text = canvas.create_text(400, 150, text="", fill="black", font=LANG_FONT)
word_text = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=PALE_GREEN, command=new_card)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=PALE_GREEN, command=new_card)
wrong_button.grid(column=1, row=1)

new_card()

window.mainloop()
