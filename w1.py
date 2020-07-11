from tkinter import *
from tkinter import messagebox,ttk
import sqlite3
from w2 import  Window2
from PIL import Image,ImageTk

class Window1():

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

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
        self.root.resizable(False,False)

        imagler = Image.open("right-arrow.png")
        imagler = imagler.resize((50,50))
        imgr = ImageTk.PhotoImage(imagler)

        bgimg = ImageTk.PhotoImage(file="download (2).jpg")
        lbl = Label(self.root,image=bgimg)
        lbl.place(x=0,y=0,relwidth=1,relheight=1)

        nb = Button(self.root, image=imgr, bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.next)
        nb.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.c_w)
        self.root.mainloop()


root = Tk()
Window1(root, root)
root.mainloop()
