from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from Main import Main1
from PIL import Image, ImageTk
from registration import Registration
from change_password import ChangePassword
import os

class start:

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            query4 = "update staff set currentuser = 0 where currentuser = 1;"
            self.conn.execute(query4)
            self.conn.commit()
            self.main_root.destroy()
        else:
            return

    def login_method(self):

        c = 0
        self.query1 = "select empno from staff;"
        self.list1 = self.conn.execute(self.query1).fetchall()
        self.query2 = "select password from staff where empno="+str(self.usernameentry.get())
        self.tuple2 = self.conn.execute(self.query2).fetchone()
        self.query3 = "select authority from staff where empno="+str(self.usernameentry.get())
        self. tuple3 = self.conn.execute(self.query3).fetchone()
        user = self.usernameentry.get()
        for i in self.list1:

            if user == str(i[0]):
                c = 1
                if str(self.passwordentry.get()) == str(self.tuple2[0]):
                    c = 2
                    if self.adminvar.get() == 1:
                        c = 3
                        if str(self.tuple3[0]) == "admin":
                            messagebox.showinfo("School Software", "Permission granted,you are allow to use app as admin")
                            query4 = "update staff set currentuser = 0"
                            self.conn.execute(query4)
                            query5 = "update staff set currentuser = 1 where empno=" + str(self.usernameentry.get())
                            self.conn.execute(query5)
                            self.conn.commit()
                            self.usernamevar.set("")
                            self.passwordvar.set("")
                            self.adminvar.set(0)
                            Main1(self.root, self.main_root)
                            self.root.withdraw()

                        else:
                            messagebox.showerror("School Software","You are not appoint as admin so login as staff member")
                            return
                    else:
                        c = 3
                        messagebox.showinfo("School Software", "User authenticated,you are allow to use app")
                        query4 = "update staff set currentuser = 0"
                        self.conn.execute(query4)
                        query5 = "update staff set currentuser = 1 where empno="+str(self.usernameentry.get())
                        self.conn.execute(query5)
                        self.conn.commit()
                        self.usernamevar.set("")
                        self.passwordvar.set("")
                        self.adminvar.set(0)
                        Main1(self.root,self.main_root)
                        self.root.withdraw()
        if c == 0:
            messagebox.showerror("School Software", "User not Found!Enter valid Username")
            self.usernamevar.set("")
            self.usernameentry.focus_set()

        if c == 1:
            messagebox.showerror("School Software", "Password do not match!Enter valid Password")
            self.passwordvar.set("")
            self.passwordentry.focus_set()

    # def reset_method(self):
    #     self.usernamevar.set("")
    #     self.usernameentry.focus_set()
    #     self.passwordvar.set("")
    #     self.adminvar.set(0)

    def change_password_method(self):
        c = 0
        self.query1 = "select empno from staff;"
        self.list1 = self.conn.execute(self.query1).fetchall()
        self.query2 = "select password from staff where empno=" + str(self.usernameentry.get())
        self.tuple2 = self.conn.execute(self.query2).fetchone()
        user = self.usernameentry.get()
        for i in self.list1:
            if user == str(i[0]):
                c = 1
                if str(self.passwordentry.get()) == str(self.tuple2[0]):
                    c = 2
                    query1 = "update staff set currentuser=1 where empno= "+str(self.usernameentry.get())
                    self.conn.execute(query1)
                    self.conn.commit()
                    self.passwordvar.set("")
                    ChangePassword(self.root,self.main_root)
                    self.root.withdraw()

        if c == 0:
            messagebox.showerror("School Software", "User not Found!Enter valid Username")
            self.usernamevar.set("")
            self.usernameentry.focus_set()

        if c == 1:
            messagebox.showerror("School Software", "User not Found!Enter valid Password")
            self.passwordvar.set("")
            self.passwordentry.focus_set()

    def __init__(self, root, main_root):

        self.main_root = main_root
        self.root = root
        try:
            self.conn = sqlite3.connect('sinfo.db')

        except:
            messagebox.showerror("School Software", "There is some error in connection of Database")
        try:
            os.makedirs("C:\\Attendence\\Staff")
            os.makedirs("C:\\Attendence\\Student")
            os.makedirs("C:\\Reports\\Exams")
            os.mkdir("C:\\Fees")

        except:
            pass
        rowcounter = "select count(*) from staff;"
        rc = self.conn.execute(rowcounter).fetchone()
        if rc[0] == 0:
            self.root.withdraw()
            Registration(self.root, self.main_root)

        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"
        self.root.title("Start")
        self.root.config(background=self.bgclr1)
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        imagler = Image.open("right-arrow.png")
        imagler = imagler.resize((60, 15))
        imgr = ImageTk.PhotoImage(imagler)

        bgimg = ImageTk.PhotoImage(file="SzsUyC.jpg")
        lbl = Label(self.root, image=bgimg)
        lbl.place(x=0, y=0, relwidth=1, relheight=1)


        self.loginfr = LabelFrame(self.root, text="Log-In", font=150)

        self.username = Label(self.loginfr, text="Username", font=70)
        self.password = Label(self.loginfr, text="Password", font=70)

        self.usernamevar = StringVar()
        self.usernameentry = Entry(self.loginfr, textvariable=self.usernamevar, font=70)
        self.passwordvar = StringVar()
        self.passwordentry = Entry(self.loginfr, textvariable=self.passwordvar, font=70, show="*")

        self.username.place(x=275, y=100)
        self.password.place(x=275, y=200)

        self.usernameentry.place(x=770, y=100)
        self.passwordentry.place(x=770, y=200)

        self.adminvar = IntVar()
        self.admin = Checkbutton(self.loginfr, text="Log-in as an admin", variable=self.adminvar)
        self.admin.place(x=300, y=275)

        self.login_button = Button(self.loginfr, text="Log-in", font=50, command=self.login_method)
        self.change_password_button = Button(self.loginfr, text="Change Password", font=50, command=self.change_password_method)

        self.login_button.place(x=475, y=400)
        self.change_password_button.place(x=625, y=400)

        self.loginfr.place(x=0, y=200, relwidth=1, relheight=1)

        self.root.protocol("WM_DELETE_WINDOW", self.c_w)


root = Tk()
start(root, root)
root.mainloop()
