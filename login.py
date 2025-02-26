from tkinter import *
from PIL import Image, ImageTk 

from tkinter import messagebox
from tkinter import ttk
from sqlite3 import *

import time

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1350x700+0+0")
        Label(self.root, text="Welcome to Inventory Management System", font=("Arial", 30)).pack()

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System of Inventory Management System") 
        self.root.geometry("1350x700+0+0")
        
        self.username = StringVar()
        self.password = StringVar()
        
        self.laptop_image = PhotoImage(file="C:/Users/ASUS/OneDrive/Documents/python03/PRESENTATION/ultra.png")
        Label(self.root, image=self.laptop_image, bd=0).place(x=300, y=100, width=520, height=500)
        
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=700, y=150, width=220, height=350)
        
        Label(login_frame, text="Login System", font=("Elephant", 20, "bold"), bg="white").place(x=0, y=20, relwidth=1)
        Label(login_frame, text="Username", font=("Andalus", 12), bg="white", fg="#767171").place(x=18, y=70)
        Entry(login_frame, textvariable=self.username, font=("times new roman", 11), bg="#ECECEC").place(x=22, y=95, width=170)
        
        Label(login_frame, text="Password", font=("Andalus", 12), bg="white", fg="#767171").place(x=19, y=135)
        Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 11), bg="#ECECEC").place(x=22, y=160, width=170)
        

        Button(login_frame, command=self.login, text="Log In", font=("Arial Rounded MT Bold", 15), bg="#00B0F0", fg="white", cursor="hand2").place(x=22, y=218, width=170, height=30)
        
    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get() != "aditya" or self.password.get() != "12345":
            messagebox.showerror("Error", "Invalid Username or Password\nTry again", parent=self.root)
        else:
            self.root.destroy()
            root = Tk()
            IMS(root)
            root.mainloop()


