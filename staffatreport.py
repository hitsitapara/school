from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import json
from datetime import date, timedelta

class Staffatreport(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def atreport(self, event=""):

        try:
            if self.fromcal.get_date() == self.tocal.get_date():
                raise ValueError
        except:
            m = messagebox.showerror("School Software", "You cannot genrate report because both date same ", parent=self)
            self.fromcal.focus_set()
            return
        try:
            if self.tocal.get_date() > date.today():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","You can not gerate feture report", parent=self)
            self.tocal.focus_set()
            return
        try:
            if self.workdayentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter working days ", parent=self)
            self.workdayentry.focus_set()
            return

        query = """ select abdate from staff """
        a = self.conn.execute(query).fetchall()
        self.abdate = []
        for item in a:
            self.abdate.append(item[0])
        for i in self.abdate:
            print(i)

    def spreport(self, event=""):

        try:
            if self.fromcal.get_date() == self.tocal.get_date():
                raise ValueError
        except:
            m = messagebox.showerror("School Software", "You cannot genrate report because both date same ", parent=self)
            self.fromcal.focus_set()
            return
        try:
            if self.tocal.get_date() > date.today():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","You can not gerate feture report", parent=self)
            self.tocal.focus_set()
            return
        try:
            if self.workdayentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter working days ", parent=self)
            self.workdayentry.focus_set()
            return
        try:
            if not(int(self.workdayentry.get()) > 0 and int(self.workdayentry.get()) < 365):
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Working day must be less than365")
            self.workdayentry.focus_set()
            return

        y = self.staffbox.curselection()
        if y == ():
            m = messagebox.showerror("School Software","Please select any staff member", parent=self)
            self.staffbox.focus_set()
            return
        else:
            self.empno = self.staffinfo[y[0]]
            query = """ select abdate from staff where empno= ? """
            a = self.conn.execute(query, (self.empno[0], )).fetchone()
            self.abdate = []
            for item in a:
                print(item)

    def __init__(self, root, main_root):

        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            m = messagebox.showerror("School Software", "Couldn't Connect With Database !", parent=self)

        self.main_root = main_root
        self.root = root
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"

        self.title("ATTENDANCE OF STAFF")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        ##====================================================frame 1===================================================

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, text="BACK", bd=5, font=(self.f1, 15), command=self.backf)
        bb.place(x=10, y=10, height=25)

        ##==================================================frame 2=====================================================

        self.lf2 = LabelFrame(self, text="ATTENDANCE WINDOW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=550, width=1350)

        self.fromdatelabel = Label(self.lf2, text="FROM DATE", bd=2, bg="black", fg="White", font=(self.f1, 15), relief=GROOVE)
        self.fromdatelabel.place(x=50, y=10, height=25)

        self.fromcal = DateEntry(self.lf2, width=12, background='darkblue', date_pattern='dd/mm/yyyy',
                             foreground='white', borderwidth=2, state="readonly")
        self.fromcal.place(x=250, y=10, height=25)

        self.todatelabel = Label(self.lf2, text="TO DATE", bd=2, bg="black", fg="White", font=(self.f1, 15), relief=GROOVE)
        self.todatelabel.place(x=550, y=10, height=25)

        self.tocal = DateEntry(self.lf2, width=12, background='darkblue', date_pattern='dd/mm/yyyy',
                             foreground='white', borderwidth=2, state="readonly")
        self.tocal.place(x=750, y=10, height=25)

        self.workdaylabel =Label(self.lf2, text="Working Day", bd=2, bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
        self.workdaylabel.place(x=1000, y=10, height=25)
        self.w_orkdayentry = int()
        self.workdayentry = Entry(self.lf2, textvariable=self.w_orkdayentry, font=(self.f1, 10))
        self.workdayentry.place(x=1200, y=10, height=25, width=100)

        self.stafflabel =Label(self.lf2, text="STAFF NAME", bd=2, bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
        self.stafflabel.place(x=100, y=100, height=25)

        query = """ select empno, fname, mname, lname from staff"""
        a = self.conn.execute(query).fetchall()
        self.staffinfo = []

        self.listframe = Frame(self.lf2)
        self.listframe.place(x=400, y=100, height=300, width=300)
        self.staffbox = Listbox(self.listframe, font=(self.f1, 15), selectmode="single", selectbackground="yellow")
        for i in a:
            self.staffinfo.append(i)
            self.staffbox.insert(END, i)
        self.staffbox.place(height=300, width=300)
        yscrollbar = Scrollbar(self.listframe)
        yscrollbar.pack(side=RIGHT, fill=Y)
        yscrollbar.config(command=self.staffbox.yview)
        xscrollbar = Scrollbar(self.listframe, orient="horizontal")
        xscrollbar.pack(side=BOTTOM, fill=X)
        xscrollbar.config(command=self.staffbox.xview)

        self.reportbutton = Button(self.lf2, text="Genrate For All Report", bd=5, font=(self.f2, 15), command=self.atreport)
        self.reportbutton.place(x=800, y=450, height=25)

        self.spreportbutton = Button(self.lf2, text="Genrate Report", bd=5, font=(self.f2, 15), command=self.spreport)
        self.spreportbutton.place(x=400, y=450, height=25)

        self.protocol("WM_DELETE_WINDOW", self.c_w)