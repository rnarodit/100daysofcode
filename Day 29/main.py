from tkinter import *
from tkinter import messagebox # messagebox isn't actually a class that's y it isn't imported in the previous line, it is a module
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_list += [random.choice(letters) for n in range(0,nr_letters)  ]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for n in range(0,nr_symbols)  ]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for n in range(0,nr_numbers)  ]
    random.shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_pass():
    website= website_entry.get()
    email= email_entry.get()
    password = password_entry.get()
    if(website=="" or password=="" or email == ""):
        messagebox.showerror(title="oops", message="Don't leave any empty fields")
    else:
        is_ok= messagebox.askokcancel(title= website, message=f"These are the details entered:\n{email}\n{password}\nIs it ok to save?")# this methods returns boolean , true for ok false for cancel
        if (is_ok):
            f = open ("Day 29/passwords.txt", mode = "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200 , height=200, highlightthickness=0)
logo_img=PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column= 1, row=0)

website_label = Label(text="Website:")
website_label.grid(column = 0, row= 1 )


email_label = Label(text="Email/Username:")
email_label.grid(column = 0, row= 2 )

password_label = Label(text="Password:")
password_label.grid(column = 0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column= 1, row =1 , columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column= 1, row =2 ,  columnspan=2)
email_entry.insert(0, "pavlinx1@gmail.com")


password_entry = Entry(width=21)
password_entry.grid(column= 1, row =3)

password_button= Button(text= "Generate Password", command = generate_password)
password_button.grid(column= 2, row =3)


add_button= Button(text= "Add", width=36, command= write_pass)
add_button.grid(column= 1, row =4 , columnspan=2)

window.mainloop()
