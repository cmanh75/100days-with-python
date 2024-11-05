from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("day31/data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("day31/data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer != None:
        window.after_cancel(flip_timer)
    card = random.choice(data_dict)
    current_card = card
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=card["French"], fill="black")
    flip_timer = window.after(3000, func=filp_card)

def filp_card():
    global current_card
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    next_card()
    if len(current_card) != 0:
        data_dict.remove(current_card)
        new_data = pandas.DataFrame(data_dict)
        new_data.to_csv("day31/data/word_to_learn.csv", index=False)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height= 526)
card_front_img = PhotoImage(file="day31/images/card_front.png")
card_back_img = PhotoImage(file="day31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="day31/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="day31/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

window.mainloop()