import tkinter
from tkinter import END
from tkinter import messagebox
import random
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    with open("data.json") as data_file:
        data = json.load(data_file)

        try:
            search = website_entry.get()
            search_result = data[search]
            search_email = search_result['email']
            search_pw = search_result['password']
            messagebox.showinfo(title=f"{search}", message=f"Email:{search_email}\nPassword:{search_pw}:\n")
        except KeyError:
            messagebox.showinfo(title="Information", message=f"{search} does not exist")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters_needed = 10
    symbols_needed = 5
    numbers_needed = 5
    symbols = "!@#$^&*()_-+=|;:<>,./?"
    numbers = "0123456789"
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = letters + letters.upper()
    password = []
    for pword in range(letters_needed):
        password.append(random.choice(letters))
    for pword in range(symbols_needed):
        password.append(random.choice(symbols))
    for pword in range(numbers_needed):
        password.append(random.choice(numbers))
    
    random.shuffle(password)
    randomized_pw = "".join(password)

    password_entry.delete(0, END)
    password_entry.insert(0,randomized_pw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_data(website,email,password):
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        return False
    if '@' not in email:
        return False
    return True

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {    
                website : {
                    "email":email,
                    "password":password,
                    }
                }

    if validate_data(website,email,password):
        with open("data.json",'r') as pw_file:
            #Read the old data
            data = json.load(pw_file)

            #Update the old data with new data
            data.update(new_data)

        with open("data.json",'w') as pw_file:
            #Save the updated Data
            json.dump(data,pw_file,indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Information", message="Invalid Data cannot be saved")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = tkinter.Canvas(width=200,height=200)
pm_logo = tkinter.PhotoImage(file="images/logo.png")
canvas.create_image(100,100,image=pm_logo) #at x=100,y=100
canvas.grid(column=1,row=0)

#Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
#sticky="W" forces left alignemnt of the widgets regardless of the width
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2,sticky="W")
website_entry.focus() #focus cursor here
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky="W")
email_entry.insert(0,'email@gmail.com')
password_entry = tkinter.Entry(width=35)
password_entry.grid(row=3,column=1,sticky="W")

#Buttons
search_button = tkinter.Button(text="Search",width=15,command=search_password)
search_button.grid(row=1,column=2,sticky="W",padx=10)
generate_password_button = tkinter.Button(text="Generate Password",width=15,command=password_generator)
generate_password_button.grid(row=3,column=2,sticky="W",padx=10)
add_button = tkinter.Button(text="Add",width=29,command=save_data)
add_button.grid(row=4,column=1,columnspan=2,sticky="W")

window.mainloop()