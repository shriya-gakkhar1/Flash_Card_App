from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Load and clean data
data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")



current_card = {}

def next_card():
   
    global current_card
    current_card = random.choice(to_learn)
    print("current card:",current_card)

  

    if "French" in current_card:
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_bg, image=card_front_img)  
        window.after(3000, flip_card)
    else:
        print("Error: 'French' key missing in current_card!")

def flip_card():
    """Flips the card and shows the English translation."""
    global current_card

    print("Flipping Card:", current_card)  # Debugging print

    if not current_card or "English" not in current_card:
        print("Error: 'English' key not found in current_card")
        return  # Prevent crash

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)  # Switch to back image


# UI Setup
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")  

card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=next_card)
known_button.grid(row=1, column=1)

# Call next_card() at the start
next_card()

window.mainloop()
