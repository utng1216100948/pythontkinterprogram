#Import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect("C:\\Users\\Migue\\Desktop\\software manage store\\database\\store.db")
c = conn.cursor()

#date
date = datetime.datetime.now().date()
#Temporary lists like sessions
products_list = []
products_price = []
products_quantity = []
products_id = []
#List for labels
labels_list = []
class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        #Frames
        self.left = Frame(master, width=700, height=768, bg='white')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=666, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)
        #Components
        self.heading = Label(self.left, text="UTNG'S COMMODITY STORE", font=('arial 36 bold'), bg='white')
        self.heading.place(x=0, y=0)
        self.date_l = Label(self.right, text="Today's Date: " + str(date), font=('arial 16 bold'), bg='lightblue', fg='white')
        self.date_l.place(x=0, y=0)
        #Table invoice
        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=60)
        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tquantity.place(x=300, y=60)
        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tamount.place(x=500, y=60)
        #Enter stuff
        self.enterid = Label(self.left, text="Enter Product's ID:", font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0, y=80)
        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=190, y=80)
        self.enteride.focus()
        #Button
        self.search_btn = Button(self.left, text="Search", width=22, height=2, bg='orange', command=self.ajax)
        self.search_btn.place(x=350, y=120)
        #Fill it later by the function ajax
        self.productname = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='steelblue')
        self.productname.place(x=0, y=250)
        self.price = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='steelblue')
        self.price.place(x=0, y=290)
        #Total label
        self.total_l = Label(self.right, text="dfd", font=('arial 40 bold'), bg='lightblue', fg='white')
        self.total_l.place(x=0, y=600)        
        
    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        #get the products info with that id and fill in the labels above
        sql = "SELECT * FROM Inventory WHERE id=?"
        sql1 = "SELECT * FROM product WHERE id=?"
        result = c.execute(sql, (self.get_id, ))
        for r in result:
            self.get_id = r[0]
            self.get_stock = r[1]#stock
        result1 = c.execute(sql1, (self.get_id, ))
        for r in result1:
            self.get_id = r[0]
            self.get_name = r[1]#name
            self.get_price = r[3]#sp
        self.productname.configure(text="Product's name: " + str(self.get_name))
        self.price.configure(text="Price: $" + str(self.get_price))
        #Create the quantity and discount label
        self.quantity_l = Label(self.left, text="Enter Quantity:", font=('arial 18 bold'), bg='white')
        self.quantity_l.place(x=0, y=370)
        self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()
        #Discount
        self.discount_l = Label(self.left, text="Enter Discount:", font=('arial 18 bold'), bg='white')
        self.discount_l.place(x=0, y=410)
        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)
        #Add to cart botton
        self.add_to__cart_btn = Button(self.left, text="Add to cart", width=22, height=2, bg='orange', 
        command=self.add_to_cart)
        self.add_to__cart_btn.place(x=350, y=450)
        #Generate bill and change
        self.change_l = Label(self.left, text="Given Amount", font=('arial 18 bold'), bg='white')
        self.change_l.place(x=0, y=550)
        self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.change_e.place(x=190, y=550)
        #Botton change
        self.change_btn = Button(self.left, text="Calculate Change", width=22, height=2, bg='orange',
        command=self.change_fun)
        self.change_btn.place(x=350, y=590)
        #Generate bill botton
        self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg='green', fg='white',
        command=self.generate_bill)
        self.bill_btn.place(x=0, y=640)

    def add_to_cart(self, *args, **kwargs):
        #get the quantity value from the database
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many products in our inventory.")
        else:
            #Calculate price
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
            products_list.append(self.get_name)
            products_price.append(self.final_price)
            products_quantity.append(self.quantity_value)
            products_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)
                self.tempqt = Label(self.right, text=str(products_quantity[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
                self.tempqt.place(x=300, y=self.y_index)
                labels_list.append(self.tempqt)
                self.tempprice = Label(self.right, text=str(products_price[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
                self.tempprice.place(x=500, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index += 40
                self.counter += 1
                #Total configure
                self.total_l.configure(text="Total: $" + str(sum(products_price)))
                #Delete
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.price.configure(text="")
                self.add_to__cart_btn.destroy()
                #autofocus to enter id
                self.enteride.focus()
                self.enteride.delete(0, END)

    def change_fun(self, *args, **kwargs):
        #get the amount given by the customer and generated by the computer
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(products_price))
        self.to_give = self.amount_given - self.our_total
        #Label change
        self.c_amount = Label(self.left, text="Change: $" + str(self.to_give), font=('arial 18 bold'), fg='red', bg='white')
        self.c_amount.place(x=0, y=600)

    def generate_bill(self, *args, **kwargs):
        #create the bill before updating to the database
        directory = "C:\\Users\\Migue\\Desktop\\software manage store\\invoice\\" + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        #TEMPLATES FOR THE BILL
        company = "\t\t\t\tUTNG University Edu. Mx.\n"
        address = "\tAv. Educación Tecnológica No.34, Dolores Hidalgo (México)\n"
        phone = "\t\t\t\t\t(418) 182 5500\n"
        sample = "\t\t\t\t\tInvoice\n"
        dt = "\t\t\t\t\t" + str(date)
        table_header = "\n\n\t\t\t-----------------------------------\n\t\t\tSN.\tProducts\t\tQty\t\tAmount\n\t\t\t-----------------------------------"
        final = company + address + phone + sample + dt + "\n" + table_header
        #Open a file to write it to
        file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
        f = open(file_name, 'w')
        f.write(final)
        #Fill dynamics
        r = 1
        i = 0
        for t in products_list:
            f.write("\n\t\t\t" + str(r) + "\t" + str(products_list[i] + "....")[:7] + "\t\t" + str(products_quantity[i]) + "\t\t" + str(products_price[i]))
            i += 1
            r += 1
        f.write("\n\n\t\t\tTotal: $ " + str(sum(products_price)))
        f.write("\n\t\t\tThanks for your visite! :D")
        #os.startfile(file_name, "print")
        f.close()
        #decrease the stock
        self.x = 0
        initial = "SELECT * FROM Inventory WHERE id=?"
        initial2 = "SELECT * FROM product WHERE id=?"
        result = c.execute(initial, (products_id[self.x], ))
        for i in products_list:
            for r in result:
                self.old_stock = r[1]
                self.new_stock = int(self.old_stock) - int(products_quantity[self.x])
        result2 = c.execute(initial2, (products_id[self.x], ))
        for i in products_list:
            for r in result2:
                self.name = r[1]
            #updating the stock
            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, products_id[self.x]))
            conn.commit()
            #Insert into transaction
            sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?,?,?,?)"
            c.execute(sql2, (products_list[self.x], products_quantity[self.x], products_price[self.x], date))
            conn.commit()
            self.x += 1
        for a in labels_list:
            a.destroy()
        del(products_list[:])
        del(products_id[:])
        del(products_quantity[:])
        del(products_price[:])
        self.total_l.configure(text="")
        self.c_amount.configure(text="")
        self.change_e.delete(0, END)
        self.enteride.focus()
        tkinter.messagebox.showinfo("Success", "Done everything smoothly")

root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.mainloop()
