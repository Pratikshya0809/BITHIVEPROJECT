from tkinter import *
from PIL import Image, ImageTk 
import time


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System/ Developed by Bithive")
        self.root.config(bg="white")
        
        #===title===
        # Load and resize the image
        self.icon = Image.open(r'C:\Users\ASUS\OneDrive\Documents\python03\PRESENTATION\inventory.png')
        self.icon = self.icon.resize((50, 50), Image.LANCZOS)
        self.icon = ImageTk.PhotoImage(self.icon)

        self.im1 = Image.open('C:\Users\ASUS\OneDrive\Documents\python03\PRESENTATION\dash.jpg')
        self.im1 = self.im1.resize((1200, 800), Image.LANCZOS)
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50, y=100)

        title = Label(self.root, text="Inventory Management System", image=self.icon, compound=LEFT, font=("times new roman", 30, "bold"), bg="black", fg="white", bd=10, relief=GROOVE,anchor="w")
        title.place(x=0, y=0, relwidth=1)
        
        #button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor='hand2')
        btn_logout.place(x=1100, y=10, width=120, height=50)
        
        # left menu
        self.Menulogo = Image.open(r"C:\Users\ASUS\OneDrive\Documents\python03\PRESENTATION\menu.png")
        self.Menulogo = self.Menulogo.resize((200, 200), Image.LANCZOS)
        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)
        
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=570)
        
        lbl_menu = Label(LeftMenu, image=self.Menulogo)
        lbl_menu.pack(side=TOP, fill=X)
        
        self.icon_side = Image.open(r"C:\Users\ASUS\OneDrive\Documents\python03\PRESENTATION\click.png")
        self.icon_side = self.icon_side.resize((20, 20), Image.LANCZOS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)
        
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="blue").pack(side=TOP, fill=X)
       
        def change_bg(color):
            self.root.config(bg=color)

        self.btn_Employee = Button(LeftMenu, text="Employee",  command=self.employee,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", cursor='hand2')
        self.btn_Employee.pack(side=TOP, fill=X)
        self.btn_Supplier = Button(LeftMenu, text="Supplier", command= self.supplier,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", cursor='hand2')
        self.btn_Supplier.pack(side=TOP, fill=X)
        self.btn_Category = Button(LeftMenu, text="Category", command=self.Category ,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", cursor='hand2')
        self.btn_Category.pack(side=TOP, fill=X)
        self.btn_Product = Button(LeftMenu, text="Products", command=self.product,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", cursor='hand2')
        self.btn_Product.pack(side=TOP, fill=X)
        
         
        #welcome
        self.lbl_welcome = Label(self.root, text="Welcome to Inventory Management System", font=("times new roman", 20, "bold"), bg="white", fg="green")
        self.lbl_welcome.place(x=0, y=60, relwidth=1)
        
        #footer 
        def update_clock():
            now = time.strftime("%H:%M:%S")
            lbl_clock.config(text=f"Date: {time.strftime('%d/%m/%Y')}\t\t Time: {now}")
            lbl_clock.after(1000, update_clock)

        lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="gray", fg="white")
        lbl_clock.pack(side=BOTTOM, fill=X)
        update_clock()
        
        
    
    def logout(self):
        self.root.destroy()
        root = Tk()
        root.mainloop()


    


     

if __name__ == "__main__":     
    root = Tk()
    obj = IMS(root)
    root.mainloop()

