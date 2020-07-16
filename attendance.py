from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from w5 import Window5
from PIL import Image, ImageTk
from tkcalendar import Calendar


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
            self.divlabel = Label(self.lf2, text="DIV", bd=2 ,bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
            self.divlabel.place(x=225, y=85, height=25)
            query = """ select div from master where std = ? """
            a = self.conn.execute(query, (self.classbox.get(),)).fetchall()
            b = set(a)
            self.divs = []
            for i in b:
                self.divs.append(i[0])
            self.divs.sort()
            self.divbox = ttk.Combobox(self.lf2, state="readonly", font=(self.f1,15))
            self.divbox.place(x=225, y=150, height=25, width=100)
            self.divbox['values'] = self.divs
            self.divbox.bind("<<ComboboxSelected>>", self.rollno)


    def rollno(self, event=""):
        self.rolllabel = Label(self.lf2, text="ROLL NO", bd=2, bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
        self.rolllabel.place(x=400, y=85, height=25)
        query1 = """ select rno from master where std = ? AND div=?"""
        a = self.conn.execute(query1, (self.classbox.get(),self.divbox.get() )).fetchall()
        self.rno = []
        for i in a:
            self.rno.append(i[0])
        self.rno.sort()
        frame = Frame(self.lf2)
        frame.place(x=400,y=150,height=100, width=100)
        self.rnobox = Listbox(frame,  font=(self.f1, 15), selectmode="multiple", selectbackground="yellow")
        for i in self.rno:
            self.rnobox.insert(END, i)
        self.rnobox.pack()
        yscrollbar = Scrollbar(frame)
        yscrollbar.pack(side=RIGHT, fill=Y)
        yscrollbar.config(command=self.rnobox.yview)

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

        self.classlabel = Label(self.lf2, text="CLASS", bd=2 ,bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
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




##======================================================frame 3=====================================================================
        self.lf3 = LabelFrame(self, text="ATTENDANCE PREVIEW", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf3.place(x=675, y=150, height=600, width=675)



        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
