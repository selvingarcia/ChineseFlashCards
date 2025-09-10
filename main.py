
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import PhotoImage
import pyperclip

BACKGROUND_COLOR = "#B1DDC6"

word = None
save = []
meaning = None
save_meaning = []

def next_word():
    canvas.itemconfig(image_container, image=tk_img)
    global word
    word = df["word"].sample(1).iloc[0]
    pinyin_word = df.loc[df["word"] == word, "pinyin"].iloc[0]
    canvas.itemconfig(word_id, text=word)
    canvas.itemconfig(pinyin_id, text=pinyin_word, font=("Arial", 60, "bold"))
    pyperclip.copy(word)
    master.after(2500, card_flip)

def card_flip():
    global meaning
    canvas.itemconfig(image_container, image=tk_img_flip)
    list_words = df.loc[df["word"] == word, "meaning"].iloc[0]
    result = list_words.strip("[]")
    result2 = result.split(", ")
    meaning = result2[0]
    fonty = 40
    first_word = result2[0][1:-1]
    try:
        last_word = result2[1][1:-1]
    except IndexError:
        last_word = result2[0][1:-1]
    if len(first_word) > 15 or len(last_word) > 15:
        fonty = 20

    canvas.itemconfig(word_id, text=first_word, font=("Arial", fonty, "italic"))
    canvas.itemconfig(pinyin_id, text=last_word, font=("Arial", fonty, "bold"))


def forgot_word():
    global word
    save.append(word)
    save_meaning.append(meaning)
    next_word()

def save_info():
    word_series = pd.Series(save)
    meaning_series = pd.Series(save_meaning)
    data = {
        "Word": word_series,
        "Meaning": meaning_series
    }

    df_save = pd.concat(data, axis=1)
    df_save.to_csv("study_words.csv", index=False)

df = pd.read_csv("data.csv")


master = tk.Tk()
master.title("Flash Cards")
master.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

img = Image.open("card_front.png")
tk_img = ImageTk.PhotoImage(img)
img_flip = Image.open("card_back.png")
tk_img_flip = ImageTk.PhotoImage(img_flip)
wrong_img = PhotoImage(file="wrong.png")
right_img = PhotoImage(file="right.png")
save_img = PhotoImage(file="diskette.png")

canvas = tk.Canvas(master, width=800, height=526, bg=BACKGROUND_COLOR, borderwidth=0, relief="flat", highlightthickness=0)
image_container = canvas.create_image(0, 0, image=tk_img, anchor="nw")
canvas.grid( row=0, column=0, columnspan=3)

word_id = canvas.create_text(400,150, text="謝謝大家的支持😃", font=("Arial", 40, "italic"))
pinyin_id = canvas.create_text(400,263, text="Xièxiè dàjiā de zhīchí 😃" , font=("Arial", 40, "bold"))

button_fail = tk.Button(master, image= wrong_img, highlightthickness=0, borderwidth=0, relief="flat", command=forgot_word)
button_fail.grid(row=1, column=0)

button_right = tk.Button(master, image = right_img, highlightthickness=0, borderwidth=0, relief="flat", command=next_word)
button_right.grid(row=1, column=2)

button_save = tk.Button(master,image= save_img, highlightthickness=0, borderwidth=0, relief="flat", command=save_info)
button_save.grid(row=1, column=1)
master.mainloop()