from tkinter import *
from PIL import Image,ImageTk
import pickle
import time
import mysql.connector
from datetime import datetime
import os
from datetime import date
import random

def calculate():
    dict = {'onion_wings': [e1, 13],
           'chicken_wings': [e2, 20],
           'cheese_burger': [e3, 15],
           'mushrooms': [e4, 9],
           'herb_burger': [e5, 12],
           'cheese_fries': [e6, 7],
            'shrimp_eggs': [e7, 25],
            'spam_burger': [e8, 10],
            'bacon_&_eggs': [e9, 18],
            'lamp_burger': [e10, 33]}
    total = 0
      
    for key, val in dict.items():
        if val[0].get() != "":
            total += int(val[0].get())*val[1]
    label16 = Label(root,text="Your Total Bill is - "+str(total),font="times 18")
    label16.place(x=600, y=600)
    label16.after(1000, label16.destroy)
    root.after(1000, calculate)

root=Tk()
root.geometry('1200x1200')
root.resizable(False,False)
logo=Image.open("download.jpg")
logo=ImageTk.PhotoImage(logo)
logo_label=Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

canvas=Canvas(root,width=600,height=300)
canvas.grid(columnspan=3)
root.resizable(False,False)

wel=Label(text="Good Evening Sir/Ma'am. Hope you are having a great day. What would like to order today",font="Railway")
wel.place(x=220,y=20)

label0=Label(root,text="Onion Wings - $13",
			font="times 18")
label0.place(x=70,y=170)

e1=Entry(root)
e1.place(x=70,y=220)

label1=Label(root,text="Chicken Wings - $20",
			font="times 18")
label1.place(x=370,y=170)

e2=Entry(root)
e2.place(x=370,y=220)

label2=Label(root,text="Cheese Burger - $15",
			font="times 18")
label2.place(x=730,y=170)

e3=Entry(root)
e3.place(x=730,y=220)

label3=Label(root,text="Mushrooms - $9",
			font="times 18")
label3.place(x=1000,y=170)

e4=Entry(root)
e4.place(x=1000,y=220)


label4=Label(root,text="Herb Burger - $12",
			font="times 18")
label4.place(x=70,y=320)

e5=Entry(root)
e5.place(x=70,y=370)

label5=Label(root,text="Cheese Fries - $7",
			font="times 18")
label5.place(x=370,y=320)

e6=Entry(root)
e6.place(x=370,y=370)

label6=Label(root,text="Shrimp Eggs - $25",
			font="times 18")
label6.place(x=730,y=320)

e7=Entry(root)
e7.place(x=730,y=370)

label7=Label(root,text="Spam Burger - $10",
			font="times 18")
label7.place(x=1000,y=320)

e8=Entry(root)
e8.place(x=1000,y=370)

label8=Label(root,text="Bacon & Eggs - $18",
			font="times 18")
label8.place(x=370,y=450)

e9=Entry(root)
e9.place(x=370,y=500)

label9=Label(root,text="Lamp Burger - $33",
			font="times 18")
label9.place(x=730,y=450)

e10=Entry(root)
e10.place(x=730,y=500)

root.after(1000, calculate)
root.mainloop()
