from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password_en.delete(0, END)
    password = "".join(password_list)
    password_en.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website = website_en.get()
    user = user_en.get()
    password = password_en.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Website and Password are required and can not be empty")
    else:
        is_ok = messagebox.askokcancel(message=f"These are the details entered\nEmail: {user}\n"
                                               f"Password: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                website_en.delete(0, END)
                password_en.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# Labels
website_lb = Label(text="Website:")
website_lb.grid(row=1, column=0)
user_lb = Label(text="Email/Username:")
user_lb.grid(row=2, column=0)
password_lb = Label(text="Password:")
password_lb.grid(row=3, column=0)

# Entries
website_en = Entry(width=35)
website_en.focus()
website_en.grid(row=1, column=1, columnspan=2)
user_en = Entry(width=35)
user_en.grid(row=2, column=1, columnspan=2)
user_en.insert(0, "davidqum@gmail.com")
password_en = Entry(width=21)
password_en.grid(row=3, column=1)

# Buttons
generate_bt = Button(text="Generate Password", command=generate_password)
generate_bt.grid(row=3, column=2)
add_bt = Button(text="Add", width=36, command=save_entry)
add_bt.grid(row=4, column=1, columnspan=2)

window.mainloop()
