from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import *
import sqlite3
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import json
from datetime import date, timedelta


class StudentAttendanceReport(Toplevel):

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

    def std_combo_method(self,event=""):
        query1 = "select rollno from master where standard = '"+str(self.std_combo.get())+"'"
        print(query1)
        roll_list=self.conn.execute(query1).fetchall()
        x = set(roll_list)
        self.rollno = []
        for i in x:
            self.rollno.append(i[0])
        self.rollno.sort()
        self.roll_combo = Combobox(self,values=self.rollno,height=20)
        self.roll_combo.place(x=100,y=400)
        self.roll_combo.bind("<<ComboboxSelected>>",self.report_method)

    def report_method(self,event=""):
        self.report_button = Button(self,text='Generate Report',command=self.generate_report_method)
        self.report_button.place(x=200,y=600)

    def generate_report_method(self):
        query1 = "select abday from master where rollno = ? and standard = ?"
        abday = self.conn.execute(query1,(self.roll_combo.get(),self.std_combo.get())).fetchone()
        abday_list = json.loads(abday[0])
        print("absent dates are :-> ")
        for dates in abday_list:
            print(dates)
        print("Total no of absent days are: "+str(len(abday_list)))

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
        bb.place(x=10, y=10)

        self.from_date_label = Label(self,text='From :')
        self.from_date_label.place(x=100,y=100)

        self.from_cal = DateEntry(self,date_pattern = 'dd/mm/yyyy',state="read only")
        self.from_cal.place(x=200,y=100)

        self.to_date_label = Label(self, text='To :')
        self.to_date_label.place(x=100, y=200)

        self.to_cal = DateEntry(self, date_pattern='dd/mm/yyyy', state="read only")
        self.to_cal.place(x=200, y=200)

        query1 = "select standard from master"
        standard_list = self.conn.execute(query1).fetchall()
        b = set(standard_list)
        self.student = []
        for i in b:
            self.student.append(i[0])
        self.std_combo = Combobox(self,values=self.student,height=10)
        self.std_combo.place(x=100,y=300)
        self.std_combo.bind("<<ComboboxSelected>>",self.std_combo_method)

        self.protocol("WM_DELETE_WINDOW", self.c_w)

