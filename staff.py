from tkinter import *
from tkinter import ttk, messagebox
from remove_user import RemoveUser
import sqlite3
from PIL import Image, ImageTk
from registration import Registration
from update_user import UpdateUser
from attendancestaff import Attendancestaff
from staffatreport import Staffatreport


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

    def attendance(self, event=""):
        self.withdraw()
        Attendancestaff(self, self.main_root)

    def atreport(self,event=""):
        self.withdraw()
        Staffatreport(self, self.main_root)

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
        self.title("STAFF")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        ##====================================================frame 1===================================================

        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), command=self.backf)
        bb.place(x=10, y=10)

        ##==================================================frame 2=====================================================

        self.lf2 = LabelFrame(self, text="ATTENDANCE WINDOW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=550, width=1350)

        create_user = Button(self.lf2, text='Create New User', font=(self.f2, 15),  command=self.create_user)
        create_user.place(x=100, y=250, height=30, width=200)
        update_user = Button(self.lf2,text="Update User", font=(self.f2, 15),  command=self.update_user)
        update_user.place(x=400, y=250, height=30, width=200)
        remove_user = Button(self.lf2, text="Remove User", font=(self.f2, 15), command=self.remove_user)
        remove_user.place(x=700, y=250, height=30, width=200)
        attendance_staff = Button(self.lf2,text="Attendance", font=(self.f2, 15), command=self.attendance)
        attendance_staff.place(x=1000, y=250, height=30, width=200)
        staffat_report = Button(self.lf2, text="Attedance Report", font=(self.lf2, 15), command=self.atreport)
        staffat_report.place(x=500, y=350, height=30, )

        self.protocol("WM_DELETE_WINDOW", self.c_w)