from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from insert_student import InsertStudent
from update_student import UpdateStudent
from remove_student import RemoveStudent


class NewStudent(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            query4 = "update staff set currentuser = 0 where currentuser = 1;"
            self.conn.execute(query4)
            self.conn.commit()
            self.main_root.destroy()
        else:
            return

    def insert_student_method(self):
        self.withdraw()
        InsertStudent(self,self.main_root)

    def update_student_method(self):
        self.withdraw()
        UpdateStudent(self, self.main_root)

    def remove_student_method(self):
        self.withdraw()
        RemoveStudent(self, self.main_root)

    def __init__(self, root, main_root):
        self.main_root = main_root
        self.root = root
        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            messagebox.showerror("School Software", "Database Connection Error.")
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"
        self.title("WINDOW10")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((50, 50))

        imgl = ImageTk.PhotoImage(imagel)
        bb = Button(self, image=imgl, command=self.backf)
        bb.pack()

        insert_student = Button(self, text='Insert New Student',  command=self.insert_student_method)
        insert_student.pack()
        update_student = Button(self,text="Update Student",  command=self.update_student_method)
        update_student.pack()
        remove_student = Button(self, text="Remove Student", command=self.remove_student_method)
        remove_student.pack()
        self.protocol("WM_DELETE_WINDOW", self.c_w)


