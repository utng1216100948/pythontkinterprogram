#Import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("C:\\Users\\Migue\\Desktop\\software manage store\\database\\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from Inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Add to the Database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400, y=0)

        #Labels for the window
        self.name_l = Label(master, text="Enter Product Name:", font=('arial 18 bold'))
        self.name_l.place(x=0, y=70)
        #--------------
        self.stock_l = Label(master, text="Enter Stoks:", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=120)
        #--------------
        self.cp_l = Label(master, text="Enter Cost Price:", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=170)
        #--------------
        self.sp_l = Label(master, text="Enter Selling Price:", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=220)
        #--------------
        self.vendor_l = Label(master, text="Enter Vendor Name:", font=('arial 18 bold'))
        self.vendor_l.place(x=0, y=270)
        #--------------
        self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number:", font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0, y=320)
        #--------------
        self.id_l = Label(master, text="Enter Product ID:", font=('arial 18 bold'))
        self.id_l.place(x=0, y=370)
        #--------------
        self.month_l = Label(master, text="Enter Product month:", font=('arial 18 bold'))
        self.month_l.place(x=0, y=420)

        #Entries for the labels
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=70)
        #--------------
        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=120)
        #--------------
        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=170)
        #--------------
        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=220)
        #--------------
        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=270)
        #--------------
        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=320)
        #--------------
        self.id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.id_e.place(x=380, y=370)
        #--------------
        self.month_e = Entry(master, width=25, font=('arial 18 bold'))
        self.month_e.place(x=380, y=420)

        #Botton to add to the database
        self.btn_add = Button(master, text="Add to Database", width=25, height=2, bg='steelblue', 
        fg='white', command=self.get_items)
        self.btn_add.place(x=520, y=470)
        #Botton to clear all the fields
        self.btn_clear = Button(master, text="Clear All Fields", width=18, height=2, bg='lightgreen', 
        fg='white', command=self.clear_all)
        self.btn_clear.place(x=350, y=470)
        #TextBox for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "ID has reched upto: " + str(id))
    
    def get_items(self, *args, **kwargs):
        #get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()
        self.month = self.month_e.get()

        #Dynamic entries
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)
        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '' or self.month == '':
            tkinter.messagebox.showinfo("Error", "Please fill all the entries!")
        else:
            #sql = "INSERT INTO Inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES (?,?,?,?,?,?,?,?,?)"
            #c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            sql = "INSERT INTO Inventory(stock, month) VALUES (?,?)"
            c.execute(sql, (self.stock, self.month))
            sql1 = "INSERT INTO product(name, cp, sp, totalcp, totalsp, assumed_profit)  VALUES (?,?,?,?,?,?)"
            c.execute(sql1, (self.name, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit))
            sql2 = "INSERT INTO vendor(name, phone_num)  VALUES (?,?)"
            c.execute(sql2, (self.vendor, self.vendor_phone))
            conn.commit()
            #textbox insert
            self.tBox.insert(END, "\n\nInserted " + str(self.name) + " into the database with code " + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Success", "Successfully added to the database!")
    
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        self.id_e.delete(0, END)
        self.month_e.delete(0, END)

root = Tk()
b = Database(root)
root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()
