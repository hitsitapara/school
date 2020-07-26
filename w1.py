from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from Main import Main1
from PIL import Image, ImageTk
import os

class Window1:

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def next(self, event=""):
        root.withdraw()
        Main1(root, self.main_root)

    def __init__(self, root, main_root):

        try:
            os.mkdir("C:\\Fees")

        except:
            pass

        self.main_root = main_root
        self.root = root
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"
        self.root.title("WINDOW1")
        self.root.config(background=self.bgclr1)
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        imagler = Image.open("right-arrow.png")
        imagler = imagler.resize((60, 15))
        imgr = ImageTk.PhotoImage(imagler)

        bgimg = ImageTk.PhotoImage(file="SzsUyC.jpg")
        lbl = Label(self.root, image=bgimg)
        lbl.place(x=0, y=0, relwidth=1, relheight=1)

        nb = Button(self.root, image=imgr, bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.next)
        nb.place(x=10, y=10)
        self.root.protocol("WM_DELETE_WINDOW", self.c_w)
        self.root.mainloop()


root = Tk()
Window1(root, root)
root.mainloop()
