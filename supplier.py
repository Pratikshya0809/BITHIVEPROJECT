from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

from PIL import Image, ImageTk  # pip install pillow

class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title('Inventory Management System | Developed by Pratikshya')
        self.root.config(bg="white")
        self.root.focus_force()
        #======All variables=====
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_description = StringVar()

        #=====search frame=====
        title = Label(self.root, text="Supplier Details", font=('goudy old style', 20), bg='#0f4d7d', fg='white')
        title.place(x=0, y=0, relwidt=1)

        SearchFrame = LabelFrame(self.root, text=" Search Supplier", font=('goudy old style', 12, 'bold'), bg="white", fg="blue")
        SearchFrame.place(x=500, y=50, width=600, height=70)

        #======option===
        lbl_search = Label(SearchFrame, text="Invoice No.", font=('goudy old style', 15), bg='white')
        lbl_search.place(x=10, y=10)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=('goudy old style', 15), bg='lightyellow')
        txt_search.place(x=110, y=10, width=150)

        btn_search = Button(SearchFrame, text='Search', command=self.search, font=('goudy old style', 15), bg='#4caf50', fg='white', cursor='hand2')
        btn_search.place(x=280, y=10, width=160, height=30)

        #======content=======
        lbl_invoice = Label(self.root, text="Invoice No.", font=('goudy old style', 15), bg='white')
        lbl_invoice.place(x=50, y=150)
        txt_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=('goudy old style', 15), bg='lightyellow')
        txt_invoice.place(x=180, y=150, width=180)

        lbl_name = Label(self.root, text="Name", font=('goudy old style', 15), bg='white')
        lbl_name.place(x=50, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, font=('goudy old style', 15), bg='lightyellow')
        txt_name.place(x=180, y=190, width=180)

        lbl_contact = Label(self.root, text="Contact", font=('goudy old style', 15), bg='white')
        lbl_contact.place(x=50, y=230)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=('goudy old style', 15), bg='lightyellow')
        txt_contact.place(x=180, y=230, width=180)

        lbl_description = Label(self.root, text="Description", font=('goudy old style', 15), bg='white')
        lbl_description.place(x=50, y=270)
        txt_description = Entry(self.root, textvariable=self.var_description, font=('goudy old style', 15), bg='lightyellow')
        txt_description.place(x=180, y=270, width=300,height=90)

        #======buttons=======
        btn_add = Button(self.root, text='Save', command=self.add, font=('goudy old style', 15), bg='#2196f3', fg='white', cursor='hand2')
        btn_add.place(x=50, y=400, width=110, height=40)
        btn_update = Button(self.root, text='Update', command=self.update, font=('goudy old style', 15), bg='#4caf50', fg='white', cursor='hand2')
        btn_update.place(x=170, y=400, width=110, height=40)
        btn_delete = Button(self.root, text='Delete', command=self.delete, font=('goudy old style', 15), bg='#f44336', fg='white', cursor='hand2')
        btn_delete.place(x=290, y=400, width=110, height=40)
        btn_clear = Button(self.root, text='Clear', command=self.clear, font=('goudy old style', 15), bg='#607d8b', fg='white', cursor='hand2')
        btn_clear.place(x=410, y=400, width=110, height=40)

        #=======Supplier Details=======
        supplier_Frame = Frame(self.root, bd=3, relief=RIDGE)
        supplier_Frame.place(x=600, y=150, width=470, height=300)

        scrolly = Scrollbar(supplier_Frame, orient=VERTICAL)
        scrollx = Scrollbar(supplier_Frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(supplier_Frame, columns=('invoice', 'name', 'contact', 'description'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading('invoice', text='Invoice No.')
        self.supplierTable.heading('name', text='Name')
        self.supplierTable.heading('contact', text='Contact')
        self.supplierTable.heading('description', text='Description')

        self.supplierTable['show'] = 'headings'

        self.supplierTable.column('invoice', width=100)
        self.supplierTable.column('name', width=100)
        self.supplierTable.column('contact', width=100)
        self.supplierTable.column('description', width=150)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    #======Functions========
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Invoice No. already exists, try different", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, description) values(?, ?, ?, ?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_description.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, description=? WHERE invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_description.get(),
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.var_description.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice LIKE ?", ('%' + self.var_searchtxt.get() + '%',))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = self.supplierTable.item(f)
        row = content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_description.set(row[3])

if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()