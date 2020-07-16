from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from w5 import Window5
from PIL import Image, ImageTk

class Attedance1(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def next(self, event=""):
        self.withdraw()
        obj=Window5(self, self.main_root)

    def __init__(self, root, main_root):

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

        self.title("ATTENDANCE")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imager = Image.open("right-arrow.png")
        imager = imager.resize((60, 15))

        imgl = ImageTk.PhotoImage(imagel)
        imgr = ImageTk.PhotoImage(imager)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), command=self.backf)
        bb.place(x=10, y=10)
        nb = Button(self.lf1, image=imgr, bd=5, font=(self.f1, 20), command=self.next)
        nb.place(x=1260, y=10)

        self.lf2 = LabelFrame(self, text="ATTENDANCE WINDOW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=600, width=675)

        self.datelabel = Label(self.lf2, text="DATE", bd=2, bg="black", fg="White", font=(self.f1, 15), relief=GROOVE)
        self.datelabel.place(x=10, y=10, height=25)

        self.date = ttk.Combobox(self.lf2, state="readonly", font=(self.f1, 10))
        self.date.place(x=100, y=10, height=25)
        self.date.set("DATE")
        d = []
        for i in range(1, 32):
            d.append(i)
        self.date['values'] = d

        self.month = ttk.Combobox(self.lf2, state="readonly", font=(self.f1, 10))
        self.month.place(x=300, y=10, height=25)
        self.month.set("MONTH")
        mo = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
        self.month['values'] = mo

        self.year = ttk.Combobox(self.lf2, state="readonly", font=(self.f1, 10))
        self.year.place(x=500, y=10, height=25)
        self.year.set("YEAR")
        y = []
        for i in range(2001,2100):
            y.append(i)
        self.year['values'] = y

        self.classlabel = Label(self.lf2, text="CLASS", bd=2 ,bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
        self.classlabel.place(x=10, y=85, height=25)


        self.lf3 = LabelFrame(self, text="ATTENDANCE PREVIEW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf3.place(x=675, y=150, height=600, width=675)



        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
