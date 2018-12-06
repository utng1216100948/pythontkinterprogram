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
        self.heading = Label(master, text="Delete from the Database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400, y=0)

        #Entry for id
        self.id_le = Label(master, text="Enter Id:", font=('arial 18 bold'))
        self.id_le.place(x=0, y=70)
        self.id_leb = Entry(master, width=10, font=('arial 18 bold'))
        self.id_leb.place(x=380, y=70)
        #Button
        self.btn_search = Button(master, text="Search", width=15, height=2, bg='orange', command=self.search)
        self.btn_search.place(x=550, y=70)

        #Labels for the window
        self.name_l = Label(master, text="Product Name:", font=('arial 18 bold'))
        self.name_l.place(x=0, y=120)
        #--------------
        self.stock_l = Label(master, text="Stoks:", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=170)
        #--------------
        self.cp_l = Label(master, text="Cost Price:", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=220)
        #--------------
        self.sp_l = Label(master, text="Selling Price:", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=270)
        #--------------
        self.totalcp_l = Label(master, text="Total Cost Price:", font=('arial 18 bold'))
        self.totalcp_l.place(x=0, y=320)
        #--------------
        self.totalsp_l = Label(master, text="Total Selling Price:", font=('arial 18 bold'))
        self.totalsp_l.place(x=0, y=370)
        #--------------
        self.vendor_l = Label(master, text="Vendor Name:", font=('arial 18 bold'))
        self.vendor_l.place(x=0, y=420)
        #--------------
        self.vendor_phone_l = Label(master, text="Vendor Phone Number:", font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0, y=470)
        #--------------
        self.month_l = Label(master, text="Product month:", font=('arial 18 bold'))
        self.month_l.place(x=0, y=520)
        #--------------
        self.assumed_profit_l = Label(master, text="Assumed Profit:", font=('arial 18 bold'))
        self.assumed_profit_l.place(x=0, y=570)

        #Entries for the labels
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=120)
        #--------------
        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=170)
        #--------------
        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=220)
        #--------------
        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=270)
        #--------------
        self.totalcp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalcp_e.place(x=380, y=320)
        #--------------
        self.totalsp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalsp_e.place(x=380, y=370)
        #--------------
        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=420)
        #--------------
        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=470)
        #--------------
        self.month_e = Entry(master, width=25, font=('arial 18 bold'))
        self.month_e.place(x=380, y=520)
        #--------------
        self.assumed_profit_e = Entry(master, width=25, font=('arial 18 bold'))
        self.assumed_profit_e.place(x=380, y=570)

        #Botton to add to the database
        self.btn_add = Button(master, text="Delete from Database", width=25, height=2, bg='steelblue', 
        fg='white', command=self.delete_item)
        self.btn_add.place(x=520, y=620)
        #Botton to clear all the fields
        self.btn_clear = Button(master, text="Clear All Fields", width=18, height=2, bg='lightgreen', 
        fg='white', command=self.clear_all)
        self.btn_clear.place(x=350, y=620)
        #TextBox for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "ID has reched upto: " + str(id))

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM Inventory WHERE id=?"
        sql1 = "SELECT * FROM product WHERE id=?"
        sql2 = "SELECT * FROM vendor WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 = r[1]#stock
            self.n2 = r[2]#month
        result1 = c.execute(sql1, (self.id_leb.get(), ))
        for r in result1:
            self.n3 = r[1]#name
            self.n4 = r[2]#cp
            self.n5 = r[3]#sp
            self.n6 = r[4]#totalcp
            self.n7 = r[5]#totalsp
            self.n8 = r[6]#assumed_profit
        result2 = c.execute(sql2, (self.id_leb.get(), ))
        for r in result2:
            self.n9 = r[1]#name
            self.n10 = r[2]#phone_number
        #Insert into the entries to update
        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n1))
        self.month_e.delete(0, END)
        self.month_e.insert(0, str(self.n2))
        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n3))
        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n4))
        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n5))
        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n6))
        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n7))
        self.assumed_profit_e.delete(0, END)
        self.assumed_profit_e.insert(0, str(self.n8))
        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n9))
        self.vendor_phone_e.delete(0, END)
        self.vendor_phone_e.insert(0, str(self.n10))
        conn.commit()

    def delete_item(self, *args, **kwargs):
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_e.get()
        self.u9 = self.month_e.get()
        self.u10 = self.assumed_profit_e.get()
        sql = "DELETE FROM Inventory WHERE id=?"
        c.execute(sql, (self.id_leb.get()))
        sql1 = "DELETE FROM product WHERE id=?"
        c.execute(sql1, (self.id_leb.get()))
        sql2 = "DELETE FROM vendor WHERE id=?"
        c.execute(sql2, (self.id_leb.get()))
        conn.commit()
        #textbox insert
        self.tBox.insert(END, "\n\nDeleted " + str(self.u1) + " from the database!")
        tkinter.messagebox.showinfo("Success", "Successfully deleted from the database!")
    
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        self.month_e.delete(0, END)
        self.id_leb.delete(0, END)
        self.totalcp_e.delete(0, END)
        self.totalsp_e.delete(0, END)
        self.assumed_profit_e.delete(0, END)

root = Tk()
b = Database(root)
root.geometry("1366x768+0+0")
root.title("Delete from the database")
root.mainloop()