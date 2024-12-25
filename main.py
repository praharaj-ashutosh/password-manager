import tkinter
from tkinter import END
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:"
                                   f"\nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt",'a') as pw_file:
            pw_file.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
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
generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(row=3,column=2,sticky="W",padx=10)
add_button = tkinter.Button(text="Add",width=29,command=save_data)
add_button.grid(row=4,column=1,columnspan=2,sticky="W")

window.mainloop()