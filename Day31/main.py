from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
cur_card = {}
to_learn = {}

# <----------------------------------------is known functionality---------------------------------------------------->

def is_known():
    global cur_card
    to_learn.remove(cur_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")

    next_card()

# <----------------------------------------Card Flip Functionality---------------------------------------------------->
def flip_card():
    global cur_card

    canvas.itemconfig(flash_card_canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=cur_card['English'], fill="white")


# <----------------------------------------Choosing next word at random------------------------------------------------>
def next_card():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    cur_card = random.choice(to_learn)
    canvas.itemconfig(flash_card_canvas_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=cur_card['French'], fill="black")
    flip_timer = window.after(3000, flip_card)


# <-----------------------------------------------UI SETUP------------------------------------------------------------->
window = Tk()
window.title("Flashcard App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# setting up the French/English word lists
try:
    data = pandas.read_csv("data/words_to_learn.csv")

# convert the df to a dict
to_learn = data.to_dict(orient="records")

# setting up the outline of the flashcard
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
flash_card_canvas_img = canvas.create_image(400, 263, image=card_front_img, )
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# setting up wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# setting up correct button
right_img = PhotoImage(file="images/right.png")
correct_button = Button(image=right_img, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
