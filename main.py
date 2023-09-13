import tkinter as tk
from random import randint

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


def get_dict():
    try:
        df = pd.read_csv(r"data\words_to_learn.csv", header=0)
    except FileNotFoundError:
        df = pd.read_csv(r"data\french_words.csv", header=0)
    finally:
        words_list = df.to_dict(orient="records")
    return words_list


def get_word():
    global word_index
    word_index = randint(0, len(words_list) - 1)
    word_dict = words_list[word_index]
    french_word, english_word = word_dict.values()
    return french_word, english_word


def change_french_word():
    french_word, english_word = get_word()
    canvas.itemconfig(card, image=card_front_image)
    canvas.itemconfig(language_text_front, text="French", fill="black")
    canvas.itemconfig(word_text_front, text=french_word, fill="black")
    canvas.after(3000, change_to_english, english_word)
    return french_word, english_word


def change_to_english(english_word):
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(language_text_front, text="English", fill="white")
    canvas.itemconfig(word_text_front, text=english_word, fill="white")


def right_answer():
    del words_list[word_index]
    df = pd.DataFrame(words_list)
    df.to_csv(r"data\words_to_learn.csv", index=False)
    change_french_word()


words_list = get_dict()


window = tk.Tk()
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)


# Images
card_front_image = tk.PhotoImage(file=r"images\card_front.png")
card_back_image = tk.PhotoImage(file=r"images\card_back.png")
right_image = tk.PhotoImage(file=r"images\right.png")
wrong_image = tk.PhotoImage(file=r"images\wrong.png")


canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
canvas.pack(expand="y", fill="both")
card = canvas.create_image(10, 10, image=card_front_image, anchor="nw")
language_text_front = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text_front = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

change_french_word()

wrong_button = tk.Button(
    image=wrong_image,
    borderwidth=0,
    activebackground=BACKGROUND_COLOR,
    highlightthickness=0,
    command=change_french_word,
)
wrong_button.grid(column=0, row=1)

right_button = tk.Button(
    image=right_image,
    borderwidth=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    highlightthickness=0,
    command=right_answer,
)
right_button.grid(column=1, row=1)

window.mainloop()
