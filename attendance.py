from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from w5 import Window5
from PIL import Image, ImageTk
from tkcalendar import Calendar
import json


class Attedance1(Toplevel):

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
        Window5(self, self.main_root)

    def calselect(self):
        if (self.calcount == 0):
            self.cal.place(x=400, y=10)
            self.calcount = 1
        else:
            self.cal.place_forget()
            self.calcount = 0

    def division(self, event=""):
        if self.divcounter == 0:
            query = """ select div from master where std = ? """
            a = self.conn.execute(query, (self.classbox.get(), )).fetchall() ## fetch division from database
            b = set(a)
            self.divlabel = Label(self.lf2, text="DIV", bd=2, bg="black", fg="white", font=(self.f1, 15),
                                  relief=GROOVE)
            self.divlabel.place(x=225, y=85, height=25)
            self.divs = []
            for i in b:
                self.divs.append(i[0])
            self.divs.sort()
            self.divbox = ttk.Combobox(self.lf2, state="readonly", font=(self.f1, 15))
            self.divbox.place(x=225, y=150, height=25, width=150)
            self.divbox['values'] = self.divs
            self.divbox.bind("<<ComboboxSelected>>", self.rollno)
            self.divbox.set("DIVISION")
            self.divcounter = 1
        else:
            self.divbox.destroy()
            self.divlabel.destroy()
            self.rollno()
            self.divcounter = 0
            self.division()

    def rollno(self, event=""):
        if self.rollcounter == 0:
            self.rolllabel = Label(self.lf2, text="ROLL NO", bd=2, bg="black", fg="white", font=(self.f1, 15),
                                   relief=GROOVE)
            self.rolllabel.place(x=50, y=200, height=25)
            query1 = """ select rno from master where std = ? AND div=?"""
            a = self.conn.execute(query1, (self.classbox.get(), self.divbox.get())).fetchall()
            self.rno = []
            for i in a:
                self.rno.append(i[0])
            self.rno.sort()
            self.frame = Frame(self.lf2)
            self.frame.place(x=200, y=200, height=100, width=100)
            self.rnobox = Listbox(self.frame, font=(self.f1, 15), selectmode="multiple", selectbackground="yellow")
            for i in self.rno:
                self.rnobox.insert(END, i)
            self.rnobox.pack()
            yscrollbar = Scrollbar(self.frame)
            yscrollbar.pack(side=RIGHT, fill=Y)
            yscrollbar.config(command=self.rnobox.yview)
            self.rollcounter = 1
        else:
            self.frame.destroy()
            self.rolllabel.destroy()
            self.rnobox.destroy()
            self.rollcounter = 0

    def addat(self, event=""):

        try:
            if(self.classbox.get() == "CLASS"):
                raise ValueError
            try:
                if(self.divbox.get() == "DIVISION"):
                    raise ValueError
            except:
                m = messagebox.showerror("School Software", "Please Select Division")
                self.divbox.focus_set()
                return
        except:
            m = messagebox.showerror("School Software", "First select Standard", parent=self)
            self.classbox.focus_set()
            return

        y = self.rnobox.curselection()
        for item in y:

            query = """ select abday from master where std = ? and div=? and rno = ?"""
            a = self.conn.execute(query, (self.classbox.get(), self.divbox.get(), self.rno[item])).fetchone()
            if a[0] == None:
                b = [self.cal.get_date()]
                p = json.dumps(b)
                query1 = """ update master set abday = ? where std =? and div=? and rno=?"""
                self.conn.execute(query1, (p, self.classbox.get(), self.divbox.get(), self.rno[item]))
                self.conn.commit()
            else:
                x = json.loads(a[0])
                x.append(self.cal.get_date())
                p = json.dumps(x)
                query1 = """ update master set abday = ? where std =? and div=? and rno=?"""
                self.conn.execute(query1, (p, self.classbox.get(), self.divbox.get(), self.rno[item]))
                self.conn.commit()
        self.frame.destroy()
        self.rolllabel.destroy()
        self.rnobox.destroy()
        self.divbox.destroy()
        self.divlabel.destroy()
        self.classbox.set("CLASS")
        self.classbox.focus_set()

    def __init__(self, root, main_root):

        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            m = messagebox.showerror("School Software","Couldn't Connect With Database !", parent=self)

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

        self.title("ATTENDANCE")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)
##================================================variables =============================================================================
        self.calcount = 0
        self.divcounter = 0
        self.rollcounter = 0

##======================================================frame 1===========================================================================
        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imager = Image.open("right-arrow.png")
        imager = imager.resize((60, 15))

        imgl = ImageTk.PhotoImage(imagel)
        imgr = ImageTk.PhotoImage(imager)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), command=self.backf)
        bb.place(x=10, y=10)
        nb = Button(self.lf1, image=imgr, bd=5, font=(self.f1, 20), command=self.next)
        nb.place(x=1260, y=10)
##=============================================frame 2======================================================================
        self.lf2 = LabelFrame(self, text="ATTENDANCE WINDOW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=600, width=675)

        self.datelabel = Label(self.lf2, text="DATE", bd=2, bg="black", fg="White", font=(self.f1, 15), relief=GROOVE)
        self.datelabel.place(x=50, y=10, height=25)

        calimg = ImageTk.PhotoImage(file="calendar-icon-vector-22895109.jpg")
        self.cbutton = Button(self.lf2, image= calimg, bd=2, relief=GROOVE, command=self.calselect)
        self.cbutton.place(x=300, y=10, height=30, width=30)

        self.cal = Calendar(self.lf2, font="Arial 10", background='black', foreground='white', selectmode='day')
        self.cal.pack_forget()

        self.classlabel = Label(self.lf2, text="STANDARD", bd=2 ,bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
        self.classlabel.place(x=50, y=85, height=25)

        query = """select std from master """
        a = self.conn.execute(query).fetchall()
        b = set(a)
        self.cals = []
        for i in b:
            self.cals.append(i[0])
        self.cals.sort()

        self.c_lassbox = StringVar()
        self.classbox = ttk.Combobox(self.lf2, state="readonly", textvariable=self.c_lassbox ,font=(self.f1, 10))
        self.classbox.place(x=50, y=150, height=25, width=100)
        self.classbox['values'] = self.cals
        self.classbox.bind("<<ComboboxSelected>>",self.division)
        self.c_lassbox.set("CLASS")

        self.addbutton = Button(self.lf2, text="ADD",font=(self.f2, 15), bd=5, command=self.addat)
        self.addbutton.place(x=100, y=400, height=30)




##======================================================frame 3=====================================================================
        self.lf3 = LabelFrame(self, text="ATTENDANCE PREVIEW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf3.place(x=675, y=150, height=600, width=675)



        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
