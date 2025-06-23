from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

#------------FIND PASSWORD--------------------
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data Found")
    else:
        if website in data:
            user = data[website]["user"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {user}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    user = username_input.get()
    password = password_input.get()

    if user == "" or password == "" or website == "":

        messagebox.showwarning(title="Warning", message="Please fill all the blank spaces.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady= 50, padx= 50)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=32)
website_input.grid(row=1, column=1)
website_input.focus()
username_input = Entry(width=50)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "tolgayilmaz1377@gmail.com")
password_input = Entry(width=32)
password_input.grid(row=3, column=1)

generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

window.mainloop()

