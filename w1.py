from tkinter import *
from tkinter import messagebox,ttk
import sqlite3
from w2 import  Window2

class Window1():

    def next(self, event=""):
        root.withdraw()
        obj=Window2(root,self.main_root)


    def __init__(self, root, main_root):

        self.main_root = main_root
        self.root = root
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"
        self.root.title("WINDOW1")
        self.root.config(background=self.bgclr1)
        self.root.geometry("1350x700+0+0")

        nb = Button(self.root, text="NEXT", bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.next)
        nb.pack()

        self.root.mainloop()


root = Tk()
Window1(root, root)
root.mainloop()
