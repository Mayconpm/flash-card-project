import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.configure(
    background=BACKGROUND_COLOR,
    padx=50,
    pady=50,
)

# Images
card_front_image = tk.PhotoImage(file=r"images\card_front.png")
card_back_image = tk.PhotoImage(file=r"images\card_back.png")
right_image = tk.PhotoImage(file=r"images\right.png")
wrong_image = tk.PhotoImage(file=r"images\wrong.png")


canvas = tk.Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, borderwidth=0, highlightbackground=BACKGROUND_COLOR
)
canvas.pack(expand="y", fill="both")
card = canvas.create_image(10, 10, image=card_front_image, anchor="nw")
language_text_front = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text_front = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# canvas.itemconfig(card, image=card_back_image)
# canvas.itemconfig(language_text_front, text="French")
# canvas.itemconfig(word_text_front, text="trouve")

wrong_button = tk.Button(image=wrong_image, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

right_button = tk.Button(image=right_image, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

window.mainloop()
