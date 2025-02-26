import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    
    cur.execute("create table if not exists category(cid integer primary key autoincrement, name text)")
    con.commit()

    cur.execute("create table if not exists product(pid integer primary key autoincrement, category text, supplier text, name text, price text, quantity text, status text)")
    con.commit()

    cur.execute("create table if not exists supplier(invoice integer primary key autoincrement, name text, contact text, description text)")
    con.commit()

    cur.execute("create table if not exists sales(invoice integer primary key autoincrement, product text, quantity text, amount text, date text)")
    con.commit()

    cur.execute("create table if not exists employee(eid integer primary key autoincrement, name text, email text,contact text,gender text, dob text, doj text, pass text, utype text,address text,salary text)")
    con.commit()
create_db()    