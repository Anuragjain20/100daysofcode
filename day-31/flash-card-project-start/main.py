from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WORD_CHANGE_SECONDS = 3
word_pair = {}


# ------------------ Word known --------------------
def is_known():
    to_learn.remove(word_pair)
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# ------------------ New random word ------------------
def new_card():
    global word_pair, flip_timer
    window.after_cancel(flip_timer)
    word_pair = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(language_text, fill="black")
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, fill="black")
    canvas.itemconfig(word_text, text=word_pair["French"])
    flip_timer = window.after(WORD_CHANGE_SECONDS * 1000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(language_text, fill="white")
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, fill="white")
    canvas.itemconfig(word_text, text=word_pair["English"])


# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(WORD_CHANGE_SECONDS * 1000, flip_card)

# Data set up
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# Image canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Image Buttons
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=0)
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=new_card)
unknown_button.grid(row=1, column=1)

new_card()

window.mainloop()
