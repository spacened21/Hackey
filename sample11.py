from tkinter import *
from PIL import Image,ImageTk
import pickle
import time
import mysql.connector
from datetime import datetime
import os
from datetime import date
import random
from tkinter import ttk
from tkinter import messagebox
from Snake import snake


root=Tk()
root.title("Welcome page")
mysql=mysql.connector.connect(host='localhost',user='root',passwd='123',db='project')
con=mysql.cursor()
#canvas
canvas=Canvas(root,width=600,height=300)
canvas.grid(columnspan=3)
root.resizable(False,False)

#bg
logo=Image.open("flogo.png")
logo=ImageTk.PhotoImage(logo)
logo_label=Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

#login

def login():
    global user_entry
    global pass_entry
    
    t2=Toplevel(root)
    t2.title("Login Page")
    t2.geometry("600x500")
    t2.resizable(False,False)
    
    Label(t2,text="Login Page",font="Railway").place(x=270,y=70)
    
    username=StringVar()
    password=StringVar()
    
    Label(t2,text="Username",font=23).place(x=100,y=150)
    
    user_entry=Entry(t2,textvariable= username,width=30,bd=2,font=20)
    user_entry.place(x=200,y=150)
    
    Label(t2,text="Password",font=23).place(x=100,y=200)
    
    pass_entry=Entry(t2,textvariable=password,width=30,bd=2,font=20,show='*')
    pass_entry.place(x=200,y=200)
    
    Button(t2,text="Login.",width="10",height="1",font="Railway",command=lambda:selection(user_entry.get(),pass_entry.get())).place(x=250,y=380)

#signup
def signup():
    t1=Toplevel(root)
    t1.title("Sign up page")
    t1.geometry("600x470")
    t1.resizable(False,False)



    Label(t1,text="Sign-up Page",font="Railway").pack(pady=50)

    Label(t1,text="Username",font=23).place(x=100,y=150)
    Label(t1,text="Password",font=23).place(x=100,y=200)
    Label(t1,text="Email",font=23).place(x=100,y=250)

    uname=StringVar()
    pval=StringVar()
    em=StringVar()
    userentry=Entry(t1,textvariable=uname,width=30,bd=2,font=20)
    passentry=Entry(t1,textvariable=pval,width=30,bd=2,font=20)
    mailentry=Entry(t1,textvariable=em,width=30,bd=2,font=20)

    userentry.place(x=200,y=150)
    passentry.place(x=200,y=200)
    mailentry.place(x=200,y=250)

    Button(t1,text="Sign up",width="10",height="1",font="Railway",command=lambda:reguser(userentry.get(),passentry.get())).place(x=250,y=380)


#destroy
def delete():
    s2.destroy()


#reguser    
def reguser(x,y):
    global s2
    s2=Toplevel(root)
    s2.title("Registration complete")
    s2.geometry("300x200")
    Label(s2,text="Registration complete",bg="grey",width="200",height="2",font="Railway").pack()
    Button(s2,text="Exit",width="10",height="1",command=delete).pack()
    con.execute(f'insert into login values(%s,%s)',(x,y))
    mysql.commit()




#selection   
def selection(x,y):
    con.execute('select * from login where username=%s and password=%s',(x,y))
    global user_entry
    global pass_entry
    try :
        next(con)

        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        t3=Toplevel(root)
        t3.geometry("800x650")
        t3.title("Hackey da dhaba")
        t3.resizable(False,False)

        
        logo1=Image.open("flogo.png")
        logo1=ImageTk.PhotoImage(logo1)
        logo_label1=Label(t3,image=logo1)
        logo_label1.image=logo1
        logo_label1.grid(column=1,row=0)

        logo2=Image.open("hackey2.png")
        logo2=ImageTk.PhotoImage(logo2)
        logo_label2=Label(t3,image=logo2)
        logo_label2.image=logo2
        logo_label2.place(x=70,y=90)

        
        wel1=Label(t3,text="Welcome to Hackey da dhaba, Click on any button to continue.",font="Railway",bg="grey").place(x=120,y=50)
        wel.grid(columnspan=3,column=0,row=0)
        
        Button(t3,text="Order here",width=10,height=1,font="Railway",bg="grey",command=orderhere).place(x=180,y=490)
        Button(t3,text="Menu Card",width=10,height=1,font="Railway",bg="grey",command=menuscreen).place(x=320,y=490)
        Button(t3,text="Customer Feedback",width=20,height=1,font="Railway",bg="grey",command=feedback).place(x=450,y=490)
        #Button(t3,text="Admin Portal",width=10,height=1,font="Railway",bg="grey").place(x=455,y=425)
        
    except StopIteration:
        top1=Toplevel(root)
        top1.title("Error")
        top1.geometry("500x450")
        top1.resizable(False,False)
        Label(top1,text="Wrong username or password please try again.",font="Railway",bg="grey").place(x=30,y=150)
        def dest():
            top1.destroy()
        Button(top1,text="Exit",width=10,height=1,bg="grey",font="Railway",command=dest).place(x=200,y=350)
        
        #print('Wrong username or password')

#feedback system

def feedback():
    global entry_name
    global entry_email
    global textcomment
    root2 = Tk()
    root2.title("Feedback")
    frame_header = ttk.Frame(root2)
    frame_header.pack()
    '''logo4 = PhotoImage(file='logo.gif').subsample(2, 2)
    logolabel4 = ttk.Label(frame_header, text='logo', image=logo4)
    logolabel4.grid(row=0, column=0, rowspan=2)'''
    headerlabel4 = ttk.Label(frame_header, text='CUSTOMER FEEDBACK', foreground='orange',
                            font=('Railway', 24))
    headerlabel4.grid(row=0, column=1)
    messagelabel4 = ttk.Label(frame_header,
                             text='Please Let us know what you like and what you do not like',
                             foreground='purple', font=('Arial', 10))
    messagelabel4.grid(row=1, column=1)

    frame_content = ttk.Frame(root2)
    frame_content.pack()
    # def submit():
    #     username = entry_name.get()
    #     print(username)
    myvar = StringVar()
    var = StringVar()
    # cmnt= StringVar()
    namelabel = ttk.Label(frame_content, text='Name')
    namelabel.grid(row=0, column=0, padx=5, sticky='sw')
    entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
    entry_name.grid(row=1, column=0)

    emaillabel = ttk.Label(frame_content, text='Email')
    emaillabel.grid(row=0, column=1, sticky='sw')
    entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
    entry_email.grid(row=1, column=1)

    commentlabel = ttk.Label(frame_content, text='Feedback', font=('Arial', 10))
    commentlabel.grid(row=2, column=0, sticky='sw')
    textcomment = Text(frame_content, width=55, height=10)
    textcomment.grid(row=3, column=0, columnspan=2)


    textcomment.config(wrap ='word')
    # def clear():
    #     textcomment.delete(1.0,'end')
    def clear():
        global entry_name
        global entry_email
        global textcomment
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)


    def submit():
        global entry_name
        global entry_email
        global textcomment
        d1={}
        z='Name:{}'.format(myvar.get())
        y='Email:{}'.format(var.get())
        x='Comment:{}'.format(textcomment.get(1.0, END))
        d1[z]=[y,x]
        with open("feedback.dat",'ab') as f:
            pickle.dump(d1,f)
        messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)


    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')

    mainloop()
    









# To display the menu

def menuscreen():
    img=Image.open("projectmenu.png")
    img.show()

    
# Billing System
def orderhere():
    def dele():
        m.destroy()
        p.destroy()
    def payment():
        global p
        p=Toplevel(root)
        p.title("Payment")
        p.geometry("500x200")
        Label(p,text="Cash on Delivery is Only Available",bg="grey",width="200",height="2",font="Railway").pack()
        Button(p,text="Exit",width="10",height="1",command=dele).pack()
        Button(p,text="GET DISCOUNT!!!",width="15",height="1",command=snake).pack()
        
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
                'lamb_burger': [e10, 33]}
        total = 0
          
        for key, val in dict.items():
            if val[0].get() != "":
                total += int(val[0].get())*val[1]
        label16 = Label(m,text="Your Total Bill is - $"+str(total),font="Railway")
        label16.place(x=600, y=600)
        label16.after(1000, label16.destroy)
        root.after(1000, calculate)

    m=Toplevel(root)
    m.geometry('1200x1200')
    m.resizable(False,False)
    logo=Image.open("download.jpg")
    logo=ImageTk.PhotoImage(logo)
    logo_label=Label(m,image=logo)
    logo_label.image=logo
    logo_label.grid(column=1,row=0)

    canvas=Canvas(m,width=600,height=300)
    canvas.grid(columnspan=3)
    root.resizable(False,False)

    wel=Label(m,text="Good Evening Sir/Ma'am. Hope you are having a great day. What would like to order today",font="Railway")
    wel.place(x=220,y=20)

    label0=Label(m,text="Onion Wings - $13",
                            font="Railway")
    label0.place(x=70,y=170)

    e1=Entry(m)
    e1.place(x=70,y=220)

    label1=Label(m,text="Chicken Wings - $20",
                            font="Railway")
    label1.place(x=370,y=170)

    e2=Entry(m)
    e2.place(x=370,y=220)

    label2=Label(m,text="Cheese Burger - $15",
                            font="Railway")
    label2.place(x=730,y=170)

    e3=Entry(m)
    e3.place(x=730,y=220)

    label3=Label(m,text="Mushrooms - $9",
                            font="Railway")
    label3.place(x=1000,y=170)

    e4=Entry(m)
    e4.place(x=1000,y=220)


    label4=Label(m,text="Herb Burger - $12",
                            font="Railway")
    label4.place(x=70,y=320)

    e5=Entry(m)
    e5.place(x=70,y=370)

    label5=Label(m,text="Cheese Fries - $7",
                            font="Railway")
    label5.place(x=370,y=320)

    e6=Entry(m)
    e6.place(x=370,y=370)

    label6=Label(m,text="Shrimp Eggs - $25",
                            font="Railway")
    label6.place(x=730,y=320)

    e7=Entry(m)
    e7.place(x=730,y=370)

    label7=Label(m,text="Spam Burger - $10",
                            font="Railway")
    label7.place(x=1000,y=320)

    e8=Entry(m)
    e8.place(x=1000,y=370)

    label8=Label(m,text="Bacon & Eggs - $18",
                            font="Railway")
    label8.place(x=370,y=450)

    e9=Entry(m)
    e9.place(x=370,y=500)

    label9=Label(m,text="Lamb Burger - $33",
                            font="Railway")
    label9.place(x=730,y=450)

    e10=Entry(m)
    e10.place(x=730,y=500)

    buttonpay=Button(m,text="Pay here",bg="grey",font="Railway",height=2,width=10,command=payment)
    buttonpay.place(x=900,y=600)

    m.after(1000, calculate)
    m.mainloop()


def admin():
    password = 123
    intpass= int(input("\nEnter Unique password: "))
    if intpass == password:
        print("Successfully logged in")
        while True:
            print("1-Add a New Employee \n2-Display all Employee \n3-Search an Employee \n4-Update Employee Details"
                  "\n5-Fire an Employee \n6-Display Feedback's(Work in Progress)")
            userinput=int(input("Which option: "))
            if userinput == 1:
                with open("employee.dat", "ab+") as f:
                    lis = []
                    while True:
                        no = int(input("Enter Employee Number: "))
                        nam = input("Enter Employee Name: ")
                        net = int(input("Enter Net Salary: "))
                        work= input("Enter Employee Shift(On Duty/On Break):" )
                        lis.append([no, nam, net,work])
                        pickle.dump(lis, f)
                        c = input("Would you like to add more(y/n): ").lower()
                        if c == 'n':
                            break
            elif userinput == 2:
                with open("employee.dat", "rb") as f:
                    print("Employee Number".center(20), "Employee Name".center(20), "Employee Salary".center(20),"Employee Shift".center(20))
                    print("-------------------------------------------------------------------------------------")
                    while True:
                        try:
                            read=pickle.load(f)
                            print(str(read[0]).center(10),str(read[1]).center(30),str(read[2]).center(20),str(read[3]).center(20))
                            print('-'*70)
                        except EOFError:
                            break
            elif userinput == 3:
                with open("employee.dat", "rb") as f:
                    read = pickle.load(f)
                    leng = len(read)
                    usern = int(input("Enter Employee Name: "))
                    for i in range(leng):
                        if read[i][0] == usern:
                            print(read[i])
            elif userinput == 4:
                with open("employee.dat","rb+") as f:
                    b=pickle.load(f)
                    lenb=len(b)
                    print("Things to update:")
                    print("1- No \n2- Salary \n3- Shift")
                    a=int(input("Enter number to be edited: "))
                    c = int(input("Enter Eno.: "))
                    if a == 1:
                        for i in range(lenb):
                            if b[i][0] == c:
                                eno = int(input("Enter new No.: "))
                                b[i][0] = eno
                                pickle.dump(b,f)
                                print(b[i])
                    elif a == 2:
                        for i in range(lenb):
                            if b[i][0] == c:
                                esalary = int(input("Enter new Salary: "))
                                b[i][2] = esalary
                                pickle.dump(b,f)
                                print(b[i])
                    elif a == 3:
                        for i in range(lenb):
                            if b[i][0] == c:
                                if b[i][3] == "On Duty":
                                    b[i][3] = "On Break"
                                elif b[i][3] == "On Break":
                                    b[i][3] = "On Duty"
                                pickle.dump(b,f)
                                print(b[i])
                    else:
                        print("Incorrect option")
            elif userinput == 5:
                with open("employee.dat","rb+") as f:
                    read = pickle.load(f)
                    lenread = len(read)
                    userd = int(input("Enter Eno. to be deleted: "))
                    for i in range(lenread):
                        if read[i][0] == userd:
                            read.remove(read[i])
                            pickle.dump(read,f)
                            print("Employee Fired!!!")
            elif userinput==6:
                with open("feedback.dat",'rb') as f:
                    try:
                        a=pickle.load(f)
                        for j in range(a):
                            for i in a:                    
                                    print(a[i][1])
                    except EOFError:
                        pass
                     
            else :
                print("Incorrect option")
            userinput1=input("Do you want to continue ? (y/n) : ")
            if userinput1 == "n":
                break
    
    
    

#labels
wel=Label(text="Welcome to Hacky Da Dhaba! To continue, Please click on Login/Sign up",font="Railway")
wel.grid(columnspan=3,column=0,row=0)
b1=Button(text="Login",bg="grey",font="Railway",height=2,width=10,command=login)
b1.place(relx=0.25,rely=0.60)

b2=Button(text="Sign Up",bg="grey",font="Railway",height=2,width=10,command=signup)
b2.place(relx=0.45,rely=0.599)

b3=Button(text="Admin Portal",bg="grey",font="Railway",height=2,width=10,command=admin)
b3.place(relx=0.65,rely=0.599)


root.mainloop()
