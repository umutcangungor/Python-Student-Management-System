from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+250+150")
        self.root.title=("Student Management System")
        self.root.tk.call("wm", "iconphoto", self.root._w, tk.PhotoImage(file="images/student.png"))

        #ALL VARIABLES##
        self.roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


        #Images
        self.back1=ImageTk.PhotoImage(file="images/4827229.jpg")
        #Images end
        bg_label=Label(self.root,image=self.back1).pack()
        title_label=Label(self.root,text="Student Management System",font=("times new roman",30,"bold"),bg="snow",fg="steelblue2",bd=8,relief=GROOVE)
        title_label.place(x=0,y=0,relwidth=1)

        #LEFT FRAME
        left_frame=Frame(self.root,bd=4,bg="royal blue",relief=RIDGE)
        left_frame.place(x=50,y=75,width=430,height=600)
        left_title=Label(left_frame,text="Manage Students",font=("times new roman",20,"bold"),bg="royal blue",fg="white")
        left_title.grid(row=0,columnspan=2,pady=20)

        left_roll=Label(left_frame,text="Roll No.",font=("times new roman",20,"bold"),bg="royal blue",fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        roll_text=Entry(left_frame,textvariable=self.roll,font=("times new roman",15,"bold"),bd=5,relief=GROOVE).grid(row=1,column=1,padx=00,pady=10,sticky="w")

        left_name = Label(left_frame, text="Name", font=("times new roman", 20, "bold"), bg="royal blue",fg="white").grid(row=2, column=0, padx=10, pady=10,sticky="w")
        name_text = Entry(left_frame ,textvariable=self.name,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE).grid(row=2, column=1,padx=00, pady=10, sticky="w")

        left_email = Label(left_frame, text="Email", font=("times new roman", 20, "bold"), bg="royal blue",fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        email_text = Entry(left_frame,textvariable=self.email ,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE).grid(row=3, column=1, padx=00, pady=10,sticky="w")

        left_gender = Label(left_frame, text="Gender", font=("times new roman", 20, "bold"), bg="royal blue",fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        combo_gender=ttk.Combobox(left_frame,textvariable=self.gender,font=("times new roman",13),state="readonly")
        combo_gender["values"]=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=0,pady=10,sticky="w")

        left_contact = Label(left_frame, text="Contact", font=("times new roman", 20, "bold"), bg="royal blue",
                           fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        contact_text = Entry(left_frame,textvariable=self.contact,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE).grid(row=5, column=1,padx=00, pady=10,sticky="w")

        left_dob = Label(left_frame, text="D.O.B", font=("times new roman", 20, "bold"), bg="royal blue",fg="white").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        dob_text = Entry(left_frame,textvariable=self.dob,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE).grid(row=6,column=1, padx=00, pady=10, sticky="w")

        left_adress = Label(left_frame, text="Address", font=("times new roman", 20, "bold"), bg="royal blue",fg="white").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.adress_text = Text(left_frame,width=25 ,height=5,font=("", 10), bd=5, relief=GROOVE)
        self.adress_text.grid(row=7,column=1, padx=00, pady=10, sticky="w")


        #Button Frame
        btn_frame=Frame(self.root, bd=3, bg="royal blue", relief=RIDGE)
        btn_frame.place(x=50,y=625,width=430)

        btn1=Button(btn_frame,text="Add",command=self.add_students,width=10).grid(row=0,column=0,padx=10,pady=10)
        btn2 = Button(btn_frame, text="Update",command=self.update_data, width=10).grid(row=0, column=1, padx=10, pady=10)
        btn3 = Button(btn_frame, command=self.delete_data,text="Delete",width=10).grid(row=0, column=2, padx=10, pady=10)
        btn4 = Button(btn_frame, text="Clear",command=self.clear_data, width=10).grid(row=0, column=3, padx=10, pady=10)

        #RIGHT FRAME
        r_frame = Frame(self.root, bd=3, bg="royal blue", relief=RIDGE)
        r_frame.place(x=500, y=75, width=800, height=600)
        rigth_title = Label(r_frame, text="Search By", font=("times new roman", 20, "bold"), bg="royal blue", fg="white").grid(row=0, column=0, padx=5, pady=15)

        combo_search = ttk.Combobox(r_frame,textvariable=self.search_by ,font=("times new roman", 13), state="readonly")
        combo_search["values"] = ("Roll_no","Name", "Contact" )
        combo_search.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        search_text = Entry(r_frame, font=(" ", 12), bd=5,textvariable=self.search_txt ,relief=GROOVE).grid(row=0, column=2,   padx=10, pady=10, sticky="w")

        src_btn1 = Button(r_frame, text="Search",command=self.search_data, width=10,height=2).grid(row=0, column=3, padx=10, pady=10)
        shw_btn1 = Button(r_frame, text="Show All",command=self.fetch_Data ,width=10, height=2).grid(row=0, column=4, padx=10, pady=10)

        #Table FRAME
        table_frame=Frame(r_frame,bd=4,relief=RIDGE,bg="royal blue")
        table_frame.place(x=0,y=75,width=790,height=525)

        scrool_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scrool_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_Table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        scrool_x.config(command=self.student_Table.xview)
        scrool_y.config(command=self.student_Table.yview)

        self.student_Table.heading("roll",text="Roll no")
        self.student_Table.heading("name", text="Name")
        self.student_Table.heading("email", text="Email")
        self.student_Table.heading("gender", text="Gender")
        self. student_Table.heading("contact", text="Contact")
        self.student_Table.heading("dob", text="Dob")
        self.student_Table.heading("address", text="Address")
        self.student_Table["show"]="headings"

        self.student_Table.column("roll", width=100)
        self.student_Table.column("name", width=100)
        self.student_Table.column("email", width=100)
        self.student_Table.column("gender", width=100)
        self.student_Table.column("contact", width=100)
        self.student_Table.column("dob", width=100)
        self.student_Table.column("contact", width=100)
        self.student_Table.column("address", width=160)

        self.student_Table.pack(fill=BOTH,expand=1)
        self.student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_Data()

    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="12345678",database="students")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll.get(),
                                                                      self.name.get(),
                                                                      self.email.get(),
                                                                      self.gender.get(),
                                                                      self.contact.get(),
                                                                      self.dob.get(),
                                                                      self.adress_text.get("1.0",END)))
        con.commit()
        self.fetch_Data()
        self.clear_data()
        con.close()

    def fetch_Data(self):
        con = pymysql.connect(host="localhost", user="root", password="12345678", database="students")
        cur = con.cursor()
        cur.execute("select * from students ")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_Table.delete(*self.student_Table.get_children())
            for row in rows:
                self.student_Table.insert("",END,values=row)
                con.commit()
            con.close()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="12345678", database="students")
        cur = con.cursor()
        cur.execute("select * from students  where " + str(self.search_by.get()) + " LIKE '%" + str(
            self.search_txt.get()) + "%'")

        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_Table.delete(*self.student_Table.get_children())
            for row in rows:
                self.student_Table.insert("",END,values=row)
                con.commit()
            con.close()


    def clear_data(self):
        self.roll.set(""),
        self.name.set(""),
        self.email.set(""),
        self.gender.set(""),
        self.contact.set(""),
        self.dob.set(""),
        self.adress_text.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.student_Table.focus()
        contents=self.student_Table.item(cursor_row)
        row=contents["values"]
        self.roll.set(row[0]),
        self.name.set(row[1]),
        self.email.set(row[2]),
        self.gender.set(row[3]),
        self.contact.set(row[4]),
        self.dob.set(row[5]),
        self.adress_text.delete("1.0", END),
        self.adress_text.insert(END,row[6])




    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="12345678",database="students")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                      self.name.get(),
                                                                      self.email.get(),
                                                                      self.gender.get(),
                                                                      self.contact.get(),
                                                                      self.dob.get(),
                                                                      self.adress_text.get("1.0",END),
                                                                      self.roll.get()
                                                                       ))
        con.commit()
        self.fetch_Data()
        self.clear_data()
        con.close()
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="12345678", database="students")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll.get())



        con.commit()
        self.fetch_Data()
        self.clear_data()
        con.close()


root=Tk()
obj=Student(root)
root.mainloop()