from tkinter import *
from tkinter import ttk, messagebox
import sqlite3



from PIL import Image, ImageTk  # pip install pillow

class productClass:
    def __init__(self, root):
        print("Initializing productClass")
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title('Inventory Management System | Developed by Pratikshya')
        self.root.config(bg="white")
        self.root.focus_force()
        #===================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_supplier = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_status = StringVar()

        product_Frame = Frame(self.root, bd=2, relief=RIDGE,bg='white')
        product_Frame.place(x=10, y=10, width=450, height=480)

        title = Label(product_Frame, text='Manage Product Details', font=('goudy old style', 20), bg='#184a45', fg='white')
        title.pack(side=TOP, fill=X)

        #======column1========

        lbl_category = Label(product_Frame, text='Category', font=('goudy old style', 18), bg='white')
        lbl_category.place(x=30, y=60)
        lbl_Supplier = Label(product_Frame, text='Supplier', font=('goudy old style', 18), bg='white')
        lbl_Supplier.place(x=30, y=110)
        lbl_Product = Label(product_Frame, text='Name', font=('goudy old style', 18), bg='white')
        lbl_Product.place(x=30, y=160)
        lbl_Price = Label(product_Frame, text='Price', font=('goudy old style', 18), bg='white')
        lbl_Price.place(x=30, y=210)
        lbl_Quantity = Label(product_Frame, text='Quantity', font=('goudy old style', 18), bg='white')
        lbl_Quantity.place(x=30, y=260)
        lbl_Status = Label(product_Frame, text='Status', font=('goudy old style', 18), bg='white')
        lbl_Status.place(x=30, y=310)

        
        #======column2========
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat,values=self.cat_list, font=('goudy old style', 15), state='readonly', justify=CENTER)
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_supplier = ttk.Combobox(product_Frame, textvariable=self.var_supplier,values=self.sup_list, font=('goudy old style', 15), state='readonly', justify=CENTER)
        cmb_supplier.place(x=150, y=110, width=200)
        cmb_supplier.current(0)

        txt_name= Entry(product_Frame, textvariable=self.var_name, font=('goudy old style', 15), bg='lightyellow')
        txt_name.place(x=150, y=160, width=200)

        txt_price= Entry(product_Frame, textvariable=self.var_price, font=('goudy old style', 15), bg='lightyellow')
        txt_price.place(x=150, y=210, width=200)

        txt_quantity= Entry(product_Frame, textvariable=self.var_quantity, font=('goudy old style', 15), bg='lightyellow')
        txt_quantity.place(x=150, y=260, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status,values=('Active', 'Inactive'), font=('goudy old style', 15), state='readonly', justify=CENTER)
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        #======Button========
        btn_add = Button(product_Frame, text='Save', command=self.add, font=('goudy old style', 15), bg='#2196f3', fg='white')
        btn_add.place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text='Update', command=self.update, font=('goudy old style', 15), bg='#4caf50', fg='white')
        btn_update.place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text='Delete', command=self.delete, font=('goudy old style', 15), bg='#f44336', fg='white')
        btn_delete.place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text='Clear', command=self.clear, font=('goudy old style', 15), bg='#607d8b', fg='white')
        btn_clear.place(x=340, y=400, width=100, height=40)


         #======search Frame========
        search_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        search_Frame.place(x=480, y=10, width=600, height=80)

        #======options========
        cmb_search = ttk.Combobox(search_Frame, textvariable=self.var_searchby, values=('Select', 'Category', 'Supplier', 'Name'), state='readonly', justify=CENTER)
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(search_Frame, textvariable=self.var_searchtxt, font=('goudy old style', 15), bg='lightyellow')
        txt_search.place(x=200, y=10, width=150)

        

        btn_search = Button(search_Frame, text='Search', command=self.search, font=('goudy old style', 15), bg='#4caf50', fg='white')
        btn_search.place(x=360, y=10, width=150, height=30)



        #=======Product Detials=======
        product_Frame = Frame(self.root, bd=3, relief=RIDGE)
        product_Frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(product_Frame, orient=VERTICAL)
        scrollx = Scrollbar(product_Frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(product_Frame, columns=('pid','Category','Supplier','name','price','quantity','status'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview) 

        self.productTable.heading('pid', text='P ID')
        self.productTable.heading('Category', text='Category')
        self.productTable.heading('Supplier', text='Supplier')
        self.productTable.heading('name', text='Name')
        self.productTable.heading('price', text='Price')
        self.productTable.heading('quantity', text='Quantity')
        self.productTable.heading('status', text='Status')

        self.productTable['show'] = 'headings'

        self.productTable.column('pid', width=100)
        self.productTable.column('Category', width=100)
        self.productTable.column('Supplier', width=100)
        self.productTable.column('name', width=100)
        self.productTable.column('price', width=100)
        self.productTable.column('quantity', width=100)
        self.productTable.column('status', width=100)

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()


        #======Functions========
    def fetch_cat_sup(self):
        self.cat_list.append('Empty')
        self.sup_list.append('Empty')
        
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat=cur.fetchall() 
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append('Select')
                for i in cat:
                   self.cat_list.append(i[0])

            cur.execute("SELECT name FROM supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append('Select')
            for i in sup:
                self.sup_list.append(i[0])
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get() == 'Select'or self.var_cat.get()=='Empty' or self.var_supplier.get() == 'Select' or self.var_name.get() == '' or self.var_price.get() == '' or self.var_quantity.get() == '' or self.var_status.get() == '':
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Product already exists,try different", parent=self.root)
                else:
                    cur.execute("INSERT INTO product (category, supplier, name, price, quantity, status) values(?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
       
                    
        

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get() == 'Select'or self.var_cat.get()=='Empty' or self.var_supplier.get() == 'Select' or self.var_name.get() == '' or self.var_price.get() == '' or self.var_quantity.get() == '' or self.var_status.get() == '':
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "invalid Product", parent=self.root)
                else:
                    cur.execute("UPDATE product SET category=?, supplier=?, name=?, price=?, quantity=?, status=? WHERE pid=?",(
                        self.var_cat.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get() == 'Select'or self.var_cat.get()=='Empty' or self.var_supplier.get() == 'Select' or self.var_name.get() == '' or self.var_price.get() == '' or self.var_quantity.get() == '' or self.var_status.get() == '':
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE  pid!=?", ( self.var_pid.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "invalid Product", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM product WHERE pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Product deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

      
       
    def clear(self):
        self.var_cat.set('select')
        self.var_supplier.set('select')
        self.var_name.set('')
        self.var_price.set('')
        self.var_quantity.set('')
        self.var_status.set('')
        self.var_pid.set('')
        self.var_searchtxt.set('')
        self.var_searchby.set('Select')
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == 'Select':
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchby.get() =="Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            else:
                cur.execute(f"SELECT * FROM product WHERE {self.var_searchby.get()} LIKE '%{self.var_searchtxt.get()}%'")
                rows = cur.fetchall()
                if len(rows) == 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('', END, values=row)
                  
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            

    def show(self):
      
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")       

    def get_data(self, ev):
       
        f = self.productTable.focus()
        content = self.productTable.item(f)
        row = content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_supplier.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6]) 

if __name__ == "__main__":
    print("Starting application")
    root = Tk()
    obj = productClass(root)
    root.mainloop()
    print("Application closed")