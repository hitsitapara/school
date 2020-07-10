from tkinter import *
from tkinter import messagebox,ttk
import sqlite3

class Window1():


    def __init__(self, root, main_root):
        self.main_root = main_root
        self.root = root
        self.bg1 = "#0080c0"
        self.bg2 = "#e7d95a"
        self.root.title("WINDOW1")
        self.root.config(background=self.bg1)
        self.root.geometry("1350x700+0+0")


        self.root.mainloop()


root = Tk()
Window1(root, root)
root.mainloop()
