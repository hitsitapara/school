from tkinter import *
from new_exam import Exam
from tkinter import messagebox
from PIL import ImageTk
from mark_entry import Mark_Entry
from delete_exam import Delete_Exam
from update_mark import Update_Mark


class r1(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return
    def mark_entry(self):
        self.withdraw()
        Mark_Entry(self, self.main_root)

    def create_exam(self, event=""):
        self.withdraw()
        Exam(self, self.main_root)


    def delete_exam(self):
        self.withdraw()
        Delete_Exam(self,self.main_root)

    def update_marks(self):
        self.withdraw()
        Update_Mark(self,self.main_root)

    def __init__(self,root,main_root):
        self.root = root
        self.main_root = main_root
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

        bgimg = ImageTk.PhotoImage(file="dark-blue-blur-gradation-wallpaper-preview.jpg")
        lbl = Label(self, image=bgimg)
        lbl.place(x=0, y=0, relwidth=1, relheight=1)


        btn = Button(self, text="Create Exam",command=self.create_exam)
        btn.pack()
        mark_btn = Button(self, text="MARK ENTRY", command=self.mark_entry)
        mark_btn.place(x=220, y=320)
        btn = Button(self, text="Update Marks", command=self.update_marks)
        btn.pack()
        btn = Button(self, text="Delete Exam", command=self.delete_exam)
        btn.pack()
        self.protocol("WM_DELETE_WINDOW", self.c_w)
