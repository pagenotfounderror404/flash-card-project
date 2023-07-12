from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
cc = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    od = pandas.read_csv("data/french_words.csv")
    # print(od)
    to_learn = od.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global cc, ft
    w.after_cancel(ft)
    cc = random.choice(to_learn)
    c.itemconfig(card_title, text="French", fill="black")
    c.itemconfig(card_word, text=cc["French"], fill="black")
    c.itemconfig(card_background, image=card_front_img)
    ft = w.after(3000, func=flip_card)


def flip_card():
    c.itemconfig(card_title, text="English", fill="white")
    c.itemconfig(card_word, text=cc["English"], fill="white")
    c.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(cc)
    # print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


w = Tk()
w.title("Flashy")
w.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

ft = w.after(3000, func=flip_card)

c = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = c.create_image(400, 263, image=card_front_img)
card_title = c.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = c.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
c.config(bg=BACKGROUND_COLOR, highlightthickness=0)
c.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

w.mainloop()



