from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
# ----------------------------------- SEARCH ------------------------------------ #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            password_string = "password"
            email_string = "email"
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("File not found!")
    else:
        if website_input.get() in data:
            messagebox.showinfo(
                message=f"Website: {website_input.get()}\nUsername/Email:{data[website_input.get()][email_string]}\nPassword: {data[website_input.get()][password_string]}", title="Website/Password Combo Found")
        else:
            messagebox.showerror(message="No Matching Website/ or Password", title="Website/Password Combo NOT FOUND")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    password_input.delete(0, 'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def fields_check():
    if len(website_input.get()) < 1 or len(password_input.get()) < 1:
        return False
    else:
        return True


def save_info():
    website_name = website_input.get()
    email = email_UN_input.get()
    pw = password_input.get()
    new_data = {
        website_name: {
            "email": email,
            "password": pw
        }
    }

    """
    if messagebox.askokcancel(message=f"Is the following info correct?\n"
                           f"website: {website_name}\nmail: {email}\npassword: {pw}")\
            and fields_check():
        with open("pw_records.txt", "a") as file:
            file.write(f"{website_name} | {email} | {pw}\n")
    else:
        messagebox.showerror(message="email and or password was left blank!\nPlease try again!")
    """
    if len(website_name) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #read the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #update old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, 'end')
            email_UN_input.delete(0, 'end')
            password_input.delete(0, 'end')
            email_UN_input.insert(END, "johnnyAppleseed@aol.com")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.wm_minsize(500, 500)
window.config(padx=50, pady=50)

# create and position the logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# create and position the 'Website' Label
website_label = Label(text="Website:", font=(FONT_NAME, 12))
website_label.grid(column=0, row=1)

# create and position the 'Email/UN' Label
email_UN_label = Label(text="Email/Username:", font=(FONT_NAME, 12))
email_UN_label.grid(column=0, row=2)

# create and position the 'Password' Label
password_label = Label(text="Password:", font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)


# create and position the 'website' text box
website_input = Entry(width=29)
website_input.grid(column=1, row=1)
website_input.focus()

# create and position the 'Email/UN' text box
email_UN_input = Entry(width=47)
email_UN_input.grid(column=1, row=2, columnspan=2)
email_UN_input.insert(END, "johnnyAppleseed@aol.com")

# create and position the 'Password' text box
password_input = Entry(width=29)
password_input.grid(column=1, row=3)


# create and position the 'Generate Password' button
generate_pw = Button(text="Generate Password", command=generate_password)
generate_pw.grid(column=2, row=3)

# create and position the 'Add' button
add_but = Button(text="Add", width=40, command=save_info)
add_but.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=12)
search_button.grid(column=2, row=1)

window.mainloop()
