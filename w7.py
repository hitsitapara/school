from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from w8 import Window8


class Window7(Toplevel):

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
        obj=Window8(self, self.main_root)

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
        self.title("WINDOW7")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")

        bb = Button(self, text="BACK", bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.backf)
        bb.pack()
        nb = Button(self, text="NEXT", bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.next)
        nb.pack()

        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
