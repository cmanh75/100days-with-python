from tkinter import *
from tkinter import messagebox
import random
import json
number_letters = random.randint(8, 10)
number_numbers = random.randint(2, 4)
number_symbols = random.randint(2, 4)
list_letters = [];
list_numbers = [];
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'];

for i in range(97, 123):
    list_letters.append(chr(i))

for i in range(65, 91):
    list_letters.append(chr(i))

for i in range(48, 58):
    list_numbers.append(chr(i))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    random_letters = [random.choice(list_letters) for _ in range(0, number_letters)]
    random_symbols = [random.choice(list_symbols) for _ in range(0, number_symbols)]
    random_numbers = [random.choice(list_numbers) for _ in range(0, number_numbers)]
    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    json_data = {
        website: {
            "email":email,
            "password":password,   
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("day29-30/data.json", mode="r") as file:
                    old_data = json.load(file)
            except FileNotFoundError:
                with open("day29-30/data.json", mode="w") as file:
                    json.dump(json_data, file, indent=4)
            else:
                old_data.update(json_data)
                with open("day29-30/data.json", mode="w") as file:
                    json.dump(old_data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search_password():
    website = website_entry.get()
    try:
        with open("day29-30/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas()
logo_img = PhotoImage(file="day29-30/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "npcm752004t2k29@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()