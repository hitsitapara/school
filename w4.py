from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from w5 import Window5
from PIL import Image, ImageTk

class Window4(Toplevel):

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
        self.title("WINDOW4")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((50, 50))
        imager = Image.open("right-arrow.png")
        imager = imager.resize((50, 50))

        imgl = ImageTk.PhotoImage(imagel)
        imgr = ImageTk.PhotoImage(imager)

        bb = Button(self, image = imgl , bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.backf)
        bb.pack()
        nb = Button(self, image = imgr , bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.next)
        nb.pack()

        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
