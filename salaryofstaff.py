from tkinter import *
from calendar import monthrange
import sqlite3
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from datetime import date
from tkcalendar import DateEntry
import json

class Salary(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def gensalary(self, event=""):

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
        self.cutsalary = []
        self.paysalary = []
        self.totalsalary = []
        query = """select empno, jiondate, salary, abdate from staff"""
        a = self.conn.execute(query).fetchall()
        for item in a:

            fromdate = str(self.fromcal.get_date())
            todate = str(self.tocal.get_date())
            count= 0
            if item[1] > fromdate:
                fromdate = item[1]
            self.daygap = (self.tocal.get_date() - self.fromcal.get_date())
            self.daygap = str(self.daygap).split(' ')
            self.abdate = json.loads(item[3])
            for j in range(len(self.abdate)):
                if fromdate <= str(self.abdate[j]) and todate >= str(self.abdate[j]):
                    count +=1

            dailysalary = item[2]/30
            self.cutsalary.append(dailysalary*count)
            presentday = int(self.daygap[0])- count
            self.paysalary.append(presentday*dailysalary)
            self.totalsalary.append(float(self.daygap[0])*dailysalary)

        print(self.cutsalary)
        print(self.paysalary)
        print(self.totalsalary)






    def __init__(self, root, main_root):

        self.main_root = main_root
        self.root = root
        try:
            self.conn = sqlite3.connect('sinfo.db')

        except:
            messagebox.showerror("School Software", "There is some error in connection of Database")
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"
        self.title("WINDOW2")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)
        ##===================================================frame1 ====================================================
        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), bg="white", command=self.backf)
        bb.place(x=10, y=10)
        ##===============================================frame 2========================================================
        self.lf2 = LabelFrame(self, text="Buttons", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf2.place(x=0, y=150, height=600, width=1350)

        self.fromdatelabel = Label(self.lf2, text="FROM DATE", bd=2, bg="black", fg="White", font=(self.f1, 15),
                                   relief=GROOVE)
        self.fromdatelabel.place(x=50, y=10, height=25)

        self.fromcal = DateEntry(self.lf2, width=12, background='darkblue', date_pattern='dd/mm/yyyy',
                                 foreground='white', borderwidth=2, state="readonly")
        self.fromcal.place(x=250, y=10, height=25)

        self.todatelabel = Label(self.lf2, text="TO DATE", bd=2, bg="black", fg="White", font=(self.f1, 15),
                                 relief=GROOVE)
        self.todatelabel.place(x=550, y=10, height=25)

        self.tocal = DateEntry(self.lf2, width=12, background='darkblue', date_pattern='dd/mm/yyyy',
                               foreground='white', borderwidth=2, state="readonly")
        self.tocal.place(x=750, y=10, height=25)


        self.salarybutton = Button(self.lf2, text="Genrate Salary", bd=5, font=(self.f2, 15), command=self.gensalary)
        self.salarybutton.place(x=550, y=450, height=30)

        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()