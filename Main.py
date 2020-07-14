from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
from w3 import Window3
from PIL import Image, ImageTk


class Main1(Toplevel):

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
        Window3(self, self.main_root)

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
        self.title("WINDOW2")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imager = Image.open("right-arrow.png")
        imager = imager.resize((60, 15))

        imgl = ImageTk.PhotoImage(imagel)
        imgr = ImageTk.PhotoImage(imager)

        bgimg = ImageTk.PhotoImage(file="dark-blue-blur-gradation-wallpaper-preview.jpg")
        lbl = Label(self, image=bgimg)
        lbl.place(x=0, y=0, relwidth=1, relheight=1)

        self.lf1 = LabelFrame(lbl, text="NAME", bd=5, bg="black", fg="white", font=(self.f1, 20), relief=SUNKEN)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.backf)
        bb.place(x=10, y=10)
        nb = Button(self.lf1, image=imgr, bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.next)
        nb.place(x=1260, y=10)

        self.lf2 = LabelFrame(self, text="Buttons", bd=5, bg="black", fg="white", font=(self.f1, 20), relief=SUNKEN)
        self.lf2.place(x=0, y=150, height=600, width=1350)

        atimg = ImageTk.PhotoImage(file="attedence.jpeg")
        atbutton = Button(self.lf2, image=atimg, bd=5, bg=self.bgclr2, relief=FLAT)
        atbutton.place(x=50, y=50, height=175, width=350)

        feeimg = ImageTk.PhotoImage(file="fee.jpeg")
        feebutton = Button(self.lf2, image=feeimg, bd=5, bg=self.bgclr2, relief=FLAT)
        feebutton.place(x=500, y=50, height=175, width=350)

        simg = ImageTk.PhotoImage(file="student.jpeg")
        sbutoon = Button(self.lf2, image=simg, bd=5, bg=self.bgclr2, relief=FLAT)
        sbutoon.place(x=950, y=50, height=175, width=350)

        rimg = ImageTk.PhotoImage(file="result.jpeg")
        rbutton = Button(self.lf2, image=rimg, bd=5, bg=self.bgclr2, relief=FLAT)
        rbutton.place(x=50, y=300, height=175, width=350)

        imimg = ImageTk.PhotoImage(file="internal.jpeg")
        imbutton = Button(self.lf2, image=imimg, bd=5, bg=self.bgclr2, relief=FLAT)
        imbutton.place(x=500, y=300, height=175, width=350)

        stimg = ImageTk.PhotoImage(file="staff.jpeg")
        stbutton = Button(self.lf2, image=stimg, bd=5, bg=self.bgclr2, relief=FLAT)
        stbutton.place(x=950, y=300, height=175, width=350)

        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
