from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
import sqlite3,re
from tkcalendar import DateEntry
from datetime import datetime,date
from PIL import Image, ImageTk
from validate_email import validate_email

class UpdateStudent(Toplevel):
    
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
        
    def des(self,event=""):
            self.firstnamelabel.destroy()
            self.firstnameentry.destroy()
            self.middlenamelabel.destroy()
            self.middlenameentry.destroy()
            self.lastnamelabel.destroy()
            self.lastnameentry.destroy()
            self.addresslabel.destroy()
            self.addressentry.destroy()
            self.studentphnolabel.destroy()
            self.studentphnoentry.destroy()
            self.parentphnoentry.destroy()
            self.parentphnolabel.destroy()
            self.emailentry.destroy()
            self.emaillabel.destroy()
            self.parentofficeaddentry.destroy()
            self.parentofficeaddlabel.destroy()
            self.parentofficephnoentry.destroy()
            self.parentofficephnolabel.destroy()
            self.casteentry.destroy()
            self.castelabel.destroy()
            self.selectcategorylabel.destroy()
            self.selectcategoryentry.destroy()
            self.bloodgrouplabel.destroy()
            self.bloodgroupentry.destroy()
            self.dateofbirthentry.destroy()
            self.dateofbirthlabel.destroy()
            self.rollnolabel.destroy()
            self.rollnoentry.destroy()
            self.stdentry.set("Select Standard")
            self.detailcounter = 0
        
    def validNumber(self, s):
        Pattern = re.compile("(0/91)?[6-9][0-9]{9}")
        return Pattern.match(s)
        
    def rollno(self, event=""):
    
        if self.rollcounter == 0:
            self.rollnolabel = Label(self.lf2, text="Roll Number", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),
                                   relief=GROOVE)
            self.rollnolabel.place(x=600, y=20, height=30)
            query1 = """ select rollno, fname, mname, lname from master where standard = ?"""
            a = self.conn.execute(query1, (self.stdentry.get(), )).fetchall()
            self.rno = []
            for i in a:
                self.rno.append(i)
            self.rno.sort()
            self.rollno_var = StringVar()
            self.rollnoentry = ttk.Combobox(self.lf2, state="readonly", textvariable=self.rollno_var, font=(self.f1, 10))
            self.rollnoentry.place(x=900, y=20, height=30)
            self.rollnoentry['values'] = self.rno
            self.rollnoentry.bind("<<ComboboxSelected>>", self.details)
            self.rollnoentry.set("Select")
            self.rollcounter = 1
        else:
            self.rollnolabel.destroy()
            self.rollnoentry.destroy()
            self.rollcounter = 0
            self.rollno()
    
    def details(self,event=""):
        if self.detailcounter == 0:
            rno = self.rollnoentry.get().split(" ")
            query = """ select * from master where standard = ? and rollno = ? """
            self.data = self.conn.execute(query,(self.stdentry.get(),rno[0])).fetchone()
            
            self.firstnamelabel = Label(self.lf2, text="First Name", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.firstnamelabel.place(x=50,y=80)
            self.firstname_var = StringVar()
            self.firstnameentry = Entry(self.lf2, textvariable=self.firstname_var, font=(self.f1,15))
            self.firstnameentry.place(x=300, y=80,height=30, width=200) 
            self.firstname_var.set(self.data[4])   
            
            self.middlenamelabel = Label(self.lf2, text="Middle Name", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.middlenamelabel.place(x=50, y=130)
            self.middlename_var = StringVar()
            self.middlenameentry = Entry(self.lf2, textvariable=self.middlename_var, font=(self.f1,15))
            self.middlenameentry.place(x=300, y=130, height=30, width=200)
            self.middlename_var.set(self.data[5])
            
            self.lastnamelabel = Label(self.lf2, text="Lastname", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.lastnamelabel.place(x=50, y=180)
            self.lastname_var  = StringVar()
            self.lastnameentry = Entry(self.lf2, textvariable=self.lastname_var, font=(self.f1,15))
            self.lastnameentry.place(x=300, y=180, height=30, width=200)
            self.lastname_var.set(self.data[6])
            
            self.addresslabel = Label(self.lf2, text="Address", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.addresslabel.place(x=50, y=230)
            self.address_var = StringVar()
            self.addressentry = Text(self.lf2,font=(self.f1,10))
            self.addressentry.place(x=300, y=230, width=200, height=60)
            self.addressentry.insert(INSERT,self.data[7])
            
            self.studentphnolabel = Label(self.lf2, text="Student Phone No.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.studentphnolabel.place(x=50, y=320)
            self.studentphno_var = StringVar()
            self.studentphnoentry = Entry(self.lf2, textvariable=self.studentphno_var, font=(self.f1,15))
            self.studentphnoentry.place(x=300, y=320, height=30, width=200)
            self.studentphno_var.set(self.data[8])
            
            self.parentphnolabel = Label(self.lf2, text="Parent Phone No.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.parentphnolabel.place(x=50, y=370)
            self.parentphno_var = StringVar()
            self.parentphnoentry = Entry(self.lf2, textvariable=self.parentphno_var, font=(self.f1,15))
            self.parentphnoentry.place(x=300, y=370, height=30, width=200)
            self.parentphno_var.set(self.data[9])
            
            self.emaillabel = Label(self.lf2, text="E-mail Id", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.emaillabel.place(x=50, y=420)
            self.email_var = StringVar()
            self.emailentry = Entry(self.lf2, textvariable=self.email_var, font=(self.f1,15))
            self.emailentry.place(x=300, y=420, height=30, width=200)
            self.email_var.set(self.data[10])
            
            self.parentofficeaddlabel = Label(self.lf2, text="Parent Office Add.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.parentofficeaddlabel.place(x=600, y= 80)
            self.parentofficeadd_var = StringVar()
            self.parentofficeaddentry = Text(self.lf2, font=(self.f1,10))
            self.parentofficeaddentry.place(x=900, y=80, height=60, width=200)
            self.parentofficeaddentry.insert(INSERT,self.data[11])
            
            self.parentofficephnolabel = Label(self.lf2, text="Parent Office Phone No.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.parentofficephnolabel.place(x=600, y=170)
            self.parentofficephno_var = StringVar()
            self.parentofficephnoentry = Entry(self.lf2, textvariable=self.parentofficephno_var, font=(self.f1,15))
            self.parentofficephnoentry.place(x=900, y=170, height=30, width=200)
            self.parentofficephno_var.set(self.data[12])
            
            self.dateofbirthlabel = Label(self.lf2, text="Date Of Birth", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.dateofbirthlabel.place(x=600, y=220)
            self.dateofbirth_var = StringVar()
            self.dateofbirthentry = DateEntry(self.lf2, width=12, background='darkblue', font=(self.f1, 15), date_pattern='dd/mm/yyyy',foreground='white', borderwidth=2, state="readonly")
            self.dateofbirthentry.place(x=900, y=220, width=200, height=30)
            date_time_str = self.data[16]
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
            self.dateofbirthentry.set_date(date_time_obj.date())
            
            self.selectcategorylabel = Label(self.lf2, text="Select Category", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.selectcategorylabel.place(x=600, y=270)
            self.selectcategory_var = StringVar()
            self.selectcategoryentry = Combobox(self.lf2, state="readonly", font=(self.f1, 15), textvariable=self.selectcategory_var)
            self.selectcategoryentry.place(x=900, y=270, height=30, width=200)
            self.selectcategoryentry['values'] = ["ST", "SC", "OBC", "OPEN", "Other"]
            self.selectcategory_var.set(self.data[17])
            
            self.bloodgrouplabel = Label(self.lf2, text="Blood Group", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.bloodgrouplabel.place(x=600, y = 320)
            self.bloodgroup_var = StringVar()
            self.bloodgroupentry = Combobox(self.lf2, state="readonly", font=(self.f1, 15), textvariable=self.bloodgroup_var)
            self.bloodgroupentry.place(x=900, y=320, height=30, width=200)
            self.bloodgroupentry['values'] = ["A+", "B+", "A-", "B-", "AB+", "O+", "O-"]
            self.bloodgroup_var.set(self.data[18])
            
            self.castelabel = Label(self.lf2, text="Caste", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
            self.castelabel.place(x=600, y=370)
            self.caste_var = StringVar()
            self.casteentry = Entry(self.lf2, textvariable=self.caste_var, font=(self.f1,15))
            self.casteentry.place(x=900, y=370, height=30, width=200)
            self.caste_var.set(self.data[19])
            self.detailcounter = 1
            
        else:
            self.des()
            self.details()         

    def update(self):
        
        try:
            if self.firstnameentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter First Name",parent=self)
            self.firstnameentry.focus_set()
            return
        try:
            if self.middlenameentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter middle Name",parent=self)
            self.middlenameentry.focus_set()
            return
        try:
            if self.lastnameentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Last Name",parent=self)
            self.lastnameentry.focus_set()
            return
        try:
            if self.addressentry.get(1.0,END) == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Address",parent=self)
            self.addressentry.focus_set()
            return
        try:
            if self.studentphnoentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Student Phone Number",parent=self)
            self.studentphnoentry.focus_set()
            return
        try:
            if self.parentphnoentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Parent Phone Number",parent=self)
            self.parentphnoentry.focus_set()
            return
        try:
            if self.emailentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter E-mail ID",parent=self)
            self.emailentry.focus_set()
            return
        try:
            if self.parentofficeaddentry.get(1.0,END) == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Parent Office Address",parent=self)
            self.parentofficeaddentry.focus_set()
            return
        try:
            if self.parentofficephnoentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Parent Office Phone Number",parent=self)
            self.parentofficephnoentry.focus_set()
            return
        try:
            if self.selectcategoryentry.get() == "Select Category":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please Select Category",parent=self)
            return
        try:
            if self.bloodgroupentry.get() == "Select Blood Group":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please Select Blood Group",parent=self)
            return
        try:
            if self.casteentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter caste",parent=self)
            self.casteentry.focus_set()
            return
        try:
            if not self.firstnameentry.get().isalpha():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid first name ",parent=self)
            self.firstnameentry.focus_set()
            return
        try:
            if not self.middlenameentry.get().isalpha():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid middle name ",parent=self)
            self.middlenameentry.focus_set()
            return
        try:
            if not self.lastnameentry.get().isalpha():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid last name",parent=self)
            self.lastnameentry.focus_set()
            return
        try:
            if not (self.validNumber(self.studentphnoentry.get()) and len(self.studentphnoentry.get()) == 10):
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid Student phone number",parent=self)
            self.studentphnoentry.focus_set()
            return
        try:
            if  not (self.validNumber(self.parentphnoentry.get()) and len(self.parentphnoentry.get()) == 10):
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid Parent phone number",parent=self)
            self.parentphnoentry.focus_Set()
            return
        try:
            valid= validate_email(self.emailentry.get())
            if not valid:
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid E-mail address",parent=self)
            self.emailentry.focus_set()
            return
        try:
            if  not (self.validNumber(self.parentofficephnoentry.get()) and len(self.parentofficephnoentry.get()) == 10):
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid Parent office phone number",parent=self)
            self.parentofficephnoentry.focus_set()
            return
        try:
            if not self.casteentry.get().isalpha():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid caste",parent=self)
            self.casteentry.focus_set()
            return
        try:
            if(self.dateofbirthentry.get_date() >= date.today()):
                raise ValueError
        except:
            messagebox.showerror("School Software","Invalid date of birth!!")
            return
        
        m = messagebox.askokcancel("School Software" ," Are want to update data", parent= self)
        
        if m:
            query = """UPDATE master SET fname = ?, mname = ?, lname = ?, address = ?, student_phno = ?, 
                            parents_phno = ?, email = ?, parent_office_address = ?, parents_office_phno = ?, 
                            date_of_birth = ?, category = ?, blood_group = ?, cast = ? WHERE grno = ?"""
            self.conn.execute(query,(self.firstnameentry.get(), self.middlenameentry.get(),self.lastnameentry.get(),
                                     self.addressentry.get(1.0,END),self.studentphnoentry.get(),self.parentphnoentry.get(),self.emailentry.get(),
                                     self.parentofficeaddentry.get(1.0,END),self.parentofficephnoentry.get(),
                                     self.dateofbirthentry.get_date(),self.selectcategoryentry.get(),self.bloodgroupentry.get(),
                                     self.casteentry.get(),self.data[0]))
            self.conn.commit()
            m = messagebox.showinfo("School Software","Student data update succesfully",parent=self)
            self.des()
        else:
           self.des()
        
        
    def __init__(self, root, main_root):
            
        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            m = messagebox.showerror("School Software", "Couldn't Connect With Database !", parent=self)

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

        self.title("UPDATE STUDENT")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)
        
        self.rollcounter = 0
        self.detailcounter = 0
##======================================================frame 1=========================================================
        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl,bg=self.bgclr2, bd=5, font=(self.f1, 20), command=self.backf)
        bb.place(x=10, y=10)
##=============================================frame 2==================================================================
        self.lf2 = LabelFrame(self, text="UPDATE STUDENT", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=550, width=1350)
        
        self.stdlabel = Label(self.lf2, text="Standard", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),
                            relief=GROOVE)
        self.stdlabel.place(x=50, y=20, height=30)

        query = """select standard from master """
        a = self.conn.execute(query).fetchall()
        b = set(a)
        self.cals = []
        for i in b:
            self.cals.append(str(i[0]))
        self.cals.sort()

        self.std_var = StringVar()
        self.stdentry = ttk.Combobox(self.lf2, state="readonly", textvariable=self.std_var, font=(self.f1, 10))
        self.stdentry.place(x=300, y=20, height=30, width=200)
        self.stdentry['values'] = self.cals
        self.stdentry.bind("<<ComboboxSelected>>", self.rollno)
        self.std_var.set("Select Standard")
        
        self.submitbutton = Button(self.lf2, text="UPDATE", bg=self.bgclr2, font=(self.f2, 15), bd=5, command=self.update)
        self.submitbutton.place(x=1200, y=200, width=100, height=30)
        
        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()