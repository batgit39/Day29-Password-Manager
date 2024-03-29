from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project From day 5
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data(): 
    website = website_entry.get()
    email = email_entry.get()
    password =  password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title = "Error", message = "Please don't leave any fields empty.")
    else:
        checker = messagebox.askokcancel(title = website, message = f"These are the details:\nEmail: {email}\n"
                               f"Password: {password}\nPress Ok to save")
        
        if checker:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            with open("my_pwd.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50, bg = "white")

canvas = Canvas(width = 200, height = 200, highlightthickness = 0, bg = "white")
pass_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = pass_img)
canvas.grid(column = 1, row = 0)

label_website = Label(text = "Website :", bg = "white")
label_website.grid(column = 0, row = 1)

label_email = Label(text = "Email/Uesrname :", bg = "white")
label_email.grid(column = 0, row = 2)

label_password = Label(text = "Password :", bg = "white")
label_password.grid(column = 0, row = 3)


website_entry = Entry(width = 41)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()

email_entry = Entry(width = 41)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0, "mitresh@gmail.com")

password_entry = Entry(width = 24)
password_entry.grid(column = 1, row = 3)

generate_password_button = Button(text = "Generate Password", width = 13, bg = "white", command = password_generator)
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width = 36, bg = "white", command = save_data)
add_button.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()
