from tkinter import *
import json
import pandas

import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    DATA = pandas.read_csv("Day 31/data/to_learn.csv")
except FileNotFoundError:
    DATA=pandas.read_csv("Day 31/data/french_words.csv")
finally:
    word_dict= DATA.to_dict("index") # actually can use the orient parameter , orient="records"

timer=None
word={}

def card_known():
    global word
    global word_dict
    word_list =list(word_dict.values())
    word_list.remove(word)
    print (word in word_list)
    df= pandas.DataFrame(word_list, columns=['French','English'])
    df.to_csv("Day 31/data/to_learn.csv",index=False)
    word_dict= df.to_dict("index")
    print(word_dict)
    print(df)
    next_card()

def next_card():
    global timer
    window.after_cancel(timer)
    #new_data = DATA.set_index("French").T
    global word
    word= random.choice(word_dict)
   # print(random.choice(word_dict))
    canvas.itemconfig(canvas_img, image=flash_card_img)
    canvas.itemconfig(title_text, text="french", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    timer= window.after(3000, flip)

def flip():
    canvas.itemconfig(canvas_img, image=flash_card_english_image)
    canvas.itemconfig(title_text, text="english",fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    window.after_cancel(timer)




window=Tk()
window.title("Flashy")
window.config(padx=50 , pady=50 , bg= BACKGROUND_COLOR)
timer=window.after(3000, flip) 

canvas = Canvas(width=800, height=526, highlightthickness=0)
flash_card_img=PhotoImage(file="Day 31/images/card_front.png")
flash_card_english_image= PhotoImage(file="Day 31/images/card_back.png")
canvas_img=canvas.create_image(400,263,image=flash_card_img)

canvas.config(bg=BACKGROUND_COLOR)
title_text= canvas.create_text(400,150,text="Title", font= ("Arial", 40, "italic"))
word_text= canvas.create_text(400,263,text="Word", font= ("Arial", 60, "bold"))
canvas.grid(column=0 , row=0 , columnspan=2)

wrong_img = PhotoImage(file="Day 31/images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0,command=next_card)
button_wrong.grid(column=1, row=1)

right_img = PhotoImage(file="Day 31/images/right.png" )
button_right = Button(image=right_img, highlightthickness=0,command=card_known )
button_right.grid(column=0, row=1)
next_card()
window.mainloop()

