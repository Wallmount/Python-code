# A simple GUI program created with tkinter, that stores and creates the users passwords locally.

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# Fill in the users email address. It will be filled in by default in the entry field.
MY_EMAIL = ""

# Password generator
def generate_password():
    '''Creates an 10 to 13 digits long password that consists of random letter, numbers and 
    special characters. The password shows in an entry field in the GUI and 
    is automatically copied into the clipboard.'''
    entry3.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)

# Saving the password
def save_password():
    '''Gets the password, username and password that the user has typed into the GUI. 
    Provides a warning messagebox if the user seems to have forgotten to fill in any blanks.
    Saves and stores the passwords in json format. Clears the entry fields.'''
    website = entry1.get().lower()
    username = entry2.get()
    password = entry3.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)

# Searhing for saved passwords
def search_password():
    '''Searches through the json file storing saved passwords. 
    Provides a warning messagebox if nothing was found. 
    Shows the user the required password details in a message box.'''
    website = entry1.get().lower()

    try:      
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="There is no data file.")
    
    else:
        if website in data:
            saved_password = data[website]["password"]
            saved_username = data[website]["username"]
            messagebox.showinfo(title=f"{website}", message=f"Username: {saved_username}\nPassword: {saved_password}")
        else:
            messagebox.showinfo(title="Oops!", message="That website is not saved.")  
            

# UI setup
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=2, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=3, column=0)

label3 = Label(text="Password:")
label3.grid(row=4, column=0)

entry1 = Entry(width=23)
entry1.grid(row=2, column=1)
entry1.focus()

entry2 = Entry(width=41)
entry2.grid(row=3, column=1, columnspan=2)
entry2.insert(0, MY_EMAIL)

entry3 = Entry(width=23)
entry3.grid(row=4, column=1)

button_gen = Button(text="Generate Password", command=generate_password)
button_gen.grid(row=4, column=2)

button_search = Button(text="Search", width= 14, command=search_password)
button_search.grid(row=2, column=2)

button_add = Button(text="Add", width=25, command=save_password)
button_add.grid(row=5, column=1, columnspan=2)

window.mainloop()
