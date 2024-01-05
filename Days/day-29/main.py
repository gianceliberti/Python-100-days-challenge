from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle

# ---------------------------- 
# PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters)) ##this is repalced with password_letters

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)  ##this is repalced with password_symbols

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)  ##this is repalced with password_numbers

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website_text.get()
    email = username_text.get()
    pw = password_text.get()


  
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, "data.txt") #with this the txt is inside the folder

    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Error", message="You need to enter a website and a Password!")
    else:
        is_ok = messagebox.askokcancel(title="Check", message=f"These are the details entered: \nEmail: {email} \nPassword: {pw} \nIs it ok to save?")
        if is_ok:
            with open(file_path, "a") as data_file:
                data_file.write(f"{web} | {email} | {pw}\n")
                website_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
script_directory = os.path.dirname(os.path.realpath(__file__))
logo_img = PhotoImage(file=os.path.join(script_directory, "logo.png"))
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)




#Widgets

#----------Labels----------
mypass_logo = Label()

website = Label(text="Website: ")
website.grid(column=0, row= 1)

username = Label(text="Email/Username: ")
username.grid(column=0, row= 2)

mypassword = Label(text="Password: ")
mypassword.grid(column=0, row= 3)

#-----Entries-----
website_text = Entry(width=35)
website_text.grid(column=1, row= 1,columnspan=2, sticky= "w")
website_text.focus()

username_text = Entry(width=35)
username_text.grid(column=1, row= 2,columnspan=2, sticky= "w")

password_text = Entry(width=35)
password_text.grid(column=1, row= 3, sticky= "w")


#-----Buttons-------

generate_password_button =Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row= 3, column=2, sticky="w", padx=(10, 0))

add_password = Button(text="Add",width=36, command =save)
add_password.grid(row=4, column=1, columnspan=2, sticky ="w", pady=(10, 0))



window.mainloop()

