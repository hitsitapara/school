from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import  Image, ImageTk


class fee1(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def rollno(self, event=""):

        if self.rollcounter == 0:
            self.rolllabel = Label(self.lf2, text="ROLL NO", bd=2, bg="black", fg="white", font=(self.f1, 15),
                                   relief=GROOVE)
            self.rolllabel.place(x=300, y=85, height=25)
            query1 = """ select rollno from master where standard = ?"""
            a = self.conn.execute(query1, (self.classbox.get(), )).fetchall()
            self.rno = []
            for i in a:
                self.rno.append(i[0])
            self.rno.sort()
            self.r_ollbox = StringVar()
            self.rollbox = ttk.Combobox(self.lf2, state="readonly", textvariable=self.r_ollbox, font=(self.f1, 10))
            self.rollbox.place(x=300, y=150, height=25, width=100)
            self.rollbox['values'] = self.rno
            self.rollbox.set("Select")
            self.rollbox.bind("<<ComboboxSelected>>", self.amountoffee)
            self.rollcounter = 1
        else:
            self.rolllabel.destroy()
            self.rollbox.destroy()
            self.rollcounter = 0
            self.rollno()

    def amountoffee(self, event=""):

        if self.feecounter == 0:
            self.tfeelabel = Label(self.lf2, text="Total Fee", bd=2, bg="black", fg="white",font=(self.f1, 15),
                                  relief=GROOVE)
            self.tfeelabel.place(x=50, y=275, height=25)

            query = """ select fee from master where standard=? AND rollno=?"""
            a = self.conn.execute(query,(self.classbox.get(), self.rollbox.get())).fetchone()
            self.t_feeentry = StringVar()
            self.tfeeentry = Entry(self.lf2, textvariable=self.t_feeentry, font=(self.f1,10))
            self.tfeeentry.place(x=50, y=350, height=25, width=150)
            self.tfeeentry.config(state="disabled")
            self.t_feeentry.set(a[0])

            self.pfeelabel = Label(self.lf2, text="Pay Amount", bd=2, bg="black", fg="white", font=(self.f1, 15),
                                   relief=GROOVE)
            self.pfeelabel.place(x=300, y=275, height=25)
            self.p_feeentry = StringVar()
            self.pfeeentry = Entry(self.lf2, textvariable=self.p_feeentry, font=(self.f1,10))
            self.pfeeentry.place(x=300, y=350, height=25, width=150)
            self.feecounter = 1
        else:
            self.pfeeentry.destroy()
            self.pfeelabel.destroy()
            self.tfeeentry.destroy()
            self.tfeelabel.destroy()
            self.feecounter = 0
            self.amountoffee()

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
        self.title("FEES")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        self.rollcounter = 0
        self.feecounter = 0

        ##===================================================frame 1====================================================
        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))

        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), command=self.backf)
        bb.place(x=10, y=10)

        ##=============================================frame 2==========================================================
        self.lf2 = LabelFrame(self, text="PAY FEE", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=600, width=675)

        self.classlabel = Label(self.lf2, text="STANDARD", bd=2, bg="black", fg="white", font=(self.f1, 15),
                                relief=GROOVE)
        self.classlabel.place(x=50, y=85, height=25)

        query = """select standard from master """
        a = self.conn.execute(query).fetchall()
        b = set(a)
        self.cals = []
        for i in b:
            self.cals.append(i[0])
        self.cals.sort()

        self.c_lassbox = StringVar()
        self.classbox = ttk.Combobox(self.lf2, state="readonly", textvariable=self.c_lassbox, font=(self.f1, 10))
        self.classbox.place(x=50, y=150, height=25, width=100)
        self.classbox['values'] = self.cals
        self.classbox.bind("<<ComboboxSelected>>", self.rollno)
        self.c_lassbox.set("CLASS")


        ##======================================================frame 3=================================================
        self.lf3 = LabelFrame(self, text="FEES PREVIEW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf3.place(x=675, y=150, height=600, width=675)

        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
