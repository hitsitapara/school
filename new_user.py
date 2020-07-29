from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import *
from remove_user import RemoveUser
import sqlite3
from PIL import Image, ImageTk
from registration import Registration
from update_user import UpdateUser


class NewUser(Toplevel):

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

    def create_user(self):
        self.withdraw()
        Registration(self, self.main_root)

    def update_user(self):
        self.withdraw()
        UpdateUser(self,self.main_root)

    def remove_user(self):
        self.withdraw()
        RemoveUser(self,self.main_root)

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

        create_user = Button(self, text='Create New User',  command=self.create_user)
        create_user.pack()
        update_user = Button(self,text="Update User",  command=self.update_user)
        update_user.pack()
        remove_user = Button(self, text="Remove User", command=self.remove_user)
        remove_user.pack()
        self.protocol("WM_DELETE_WINDOW", self.c_w)