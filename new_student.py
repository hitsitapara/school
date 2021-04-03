from datetime import date
from tkinter import *
from tkinter import  messagebox
from tkinter.ttk import Combobox
import sqlite3
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import json, re
from validate_email import validate_email


class InsertStudent(Toplevel):
    
    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return
    def validNumber(self, s):
        Pattern = re.compile("(0/91)?[6-9][0-9]{9}")
        return Pattern.match(s)
        
    def submit(self):
        
        try:
            if self.stdentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Standard",parent=self)
            self.stdentry.focus_set()
            return
        try:
            if self.selectmediumentry.get() == "Select Medium":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please select Medium",parent=self)
            self.selectmediumentry.focus_set()
            return
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
            if self.feeentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter Fee",parent=self)
            self.feeentry.focus_set()
            return
        try:
            if self.selectcategoryentry.get() == "Select Category":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please Select Category",parent=self)
            self.selectcategoryentry.focus_set()
            return
        try:
            if self.bloodgroupentry.get() == "Select Blood Group":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please Select Blood Group",parent=self)
            self.bloodgroupentry.focus_set()
            return
        try:
            if self.casteentry.get() == "":
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter caste",parent=self)
            self.casteentry.focus_set()
            return
        try:
            if not self.stdentry.get().isnumeric() and (int(self.std.get()) <= 1) and (int(self.std.get()) >= 12):
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid standard",parent=self)
            self.stdentry.focus_set()
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
            if not self.feeentry.get().isnumeric():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid fee",parent=self)
            self.feeentry.focus_set()
            return
        try:
            if not self.casteentry.get().isalpha():
                raise ValueError
        except:
            m = messagebox.showerror("School Software","Please enter valid caste",parent=self)
            self.casteentry.focus_set()
            return
        self.insert_value()
        
    def insert_value(self):

        grnoCount = """SELECT MAX(grno) FROM master;"""
        grno = self.conn.execute(grnoCount).fetchone()
        if grno[0] == None:
            self.grno = 1
        else:
            self.grno = int(grno[0]) + 1 
        
        if (int(self.stdentry.get()) < 11):
            std = str(self.stdentry.get() + "~" + self.selectmediumentry.get()+"%")
        else:
            std = str(self.stdentry.get() + "~" + self.selectmediumentry.get() + "~" + self.selectstreamentry.get()+"%")
        rollnoCount = """SELECT MAX(rollno) FROM master WHERE ((standard like ?) and (ayear = ?));"""
        rollno = self.conn.execute(rollnoCount,(std,self.academicyear_var.get())).fetchone()
        if rollno[0] == None:
            self.rollno = 1
        else:
            self.rollno = int(rollno[0]) + 1
        m = messagebox.askokcancel("School Software","Student Gr no = {} and  Roll no = {}. if you want to submit data then press ok otherwise cancel  ".format(self.grno,self.rollno),parent=self)
        if (int(self.stdentry.get()) < 11):
            self.std = str(self.stdentry.get() + "~" + self.selectmediumentry.get())
        else:
            self.std = str(self.stdentry.get() + "~" + self.selectmediumentry.get() + "~" + self.selectstreamentry.get())
        if m:
            query = """insert into master (grno,rollno, standard, fname, mname, lname, address, 
                                        student_phno, parents_phno, email, parent_office_address, parents_office_phno,
                                        fee, date_of_birth, category, blood_group, cast, joining_date, ayear) 
                                   VALUES(?,?, ?, ?, ?, ?, ?, 
                                          ?, ?, ?, ?, ?, ?, 
                                          ?, ?, ?, ?, ?, ?)"""
            self.conn.execute(query,(self.grno,self.rollno,self.std,self.firstnameentry.get(),
                                     self.middlenameentry.get(),self.lastnameentry.get(),self.addressentry.get(1.0,END),                                     self.studentphnoentry.get(),self.parentphnoentry.get(),self.emailentry.get(),
                                     self.parentofficeaddentry.get(1.0,END),self.parentofficephnoentry.get(),self.feeentry.get(),
                                     self.dateofbirthentry.get_date(),self.selectcategoryentry.get(),self.bloodgroupentry.get(),
                                     self.casteentry.get(),str(date.today()),self.academicyear_var.get()))
            self.conn.commit()
            m = messagebox.showinfo("School Software","Student data enterd succesfully",parent=self)
        else:
            self.reset()

    def reset(self):
        self.stdentry_var.set("")
        self.selectmedium_var.set("Select Medium")
        self.firstname_var.set("")
        self.middlename_var.set("")
        self.lastname_var.set("")
        self.address_var.set("")
        self.studentphno_var.set("")
        self.parentphno_var.set("")
        self.parentofficeadd_var.set("")
        self.parentofficephno_var.set("")
        self.fee_var.set("")
        self.dateofbirth_var.set_date(date.today())
        self.selectcategory_var.set("Select Category")
        self.bloodgroup_var.set("Select Blood Group")
        self.caste_var.set("")
        self.selectstream_var.set("Select Stream")
            
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

        self.title("ATTENDANCE")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)
##======================================================frame 1=========================================================
        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl,bg=self.bgclr2, bd=5, font=(self.f1, 20), command=self.backf)
        bb.place(x=10, y=10)
##=============================================frame 2==================================================================
        self.lf2 = LabelFrame(self, text="ATTENDANCE WINDOW", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=550, width=1350)
        
        self.stdlabel = Label(self.lf2, text="Standard", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.stdlabel.place(x=50,y=20)
        self.stdentry_var = StringVar()
        self.stdentry = Entry(self.lf2, textvariable=self.stdentry_var, font=(self.f1,15))
        self.stdentry.place(x=300, y=20, height=30,width=200)
        
        self.selectmediumlabel = Label(self.lf2, text="Select Medium", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.selectmediumlabel.place(x=50, y=80)
        self.selectmedium_var = StringVar()
        self.selectmediumentry = Combobox(self.lf2 ,state="readonly", font=(self.f1, 15), textvariable=self.selectmedium_var)
        self.selectmediumentry.place(x=300, y=80, height=30, width=200)
        self.selectmediumentry['values'] = ["Guj", "Eng"]
        self.selectmedium_var.set("Select Medium" )  
        
        self.firstnamelabel = Label(self.lf2, text="First Name", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.firstnamelabel.place(x=50,y=130)
        self.firstname_var = StringVar()
        self.firstnameentry = Entry(self.lf2, textvariable=self.firstname_var, font=(self.f1,15))
        self.firstnameentry.place(x=300, y=130,height=30, width=200)    
        
        self.middlenamelabel = Label(self.lf2, text="Middle Name", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.middlenamelabel.place(x=50, y=180)
        self.middlename_var = StringVar()
        self.middlenameentry = Entry(self.lf2, textvariable=self.middlename_var, font=(self.f1,15))
        self.middlenameentry.place(x=300, y=180, height=30, width=200)
        
        self.lastnamelabel = Label(self.lf2, text="Lastname", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.lastnamelabel.place(x=50, y=230)
        self.lastname_var  = StringVar()
        self.lastnameentry = Entry(self.lf2, textvariable=self.lastname_var, font=(self.f1,15))
        self.lastnameentry.place(x=300, y=230, height=30, width=200)
        
        self.addresslabel = Label(self.lf2, text="Address", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.addresslabel.place(x=50, y=280)
        self.address_var = StringVar()
        self.addressentry = Text(self.lf2,font=(self.f1,10))
        self.addressentry.place(x=300, y=280, width=200, height=60)
        
        self.studentphnolabel = Label(self.lf2, text="Student Phone NO.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.studentphnolabel.place(x=50, y=360)
        self.studentphno_var = StringVar()
        self.studentphnoentry = Entry(self.lf2, textvariable=self.studentphno_var, font=(self.f1,15))
        self.studentphnoentry.place(x=300, y=360, height=30, width=200)
        
        self.parentphnolabel = Label(self.lf2, text="Parent Phone NO.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.parentphnolabel.place(x=50, y=410)
        self.parentphno_var = StringVar()
        self.parentphnoentry = Entry(self.lf2, textvariable=self.parentphno_var, font=(self.f1,15))
        self.parentphnoentry.place(x=300, y=410, height=30, width=200)
        
        self.emaillabel = Label(self.lf2, text="E-mail Id", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.emaillabel.place(x=50, y=460)
        self.email_var = StringVar()
        self.emailentry = Entry(self.lf2, textvariable=self.email_var, font=(self.f1,15))
        self.emailentry.place(x=300, y=460, height=30, width=200)
        
        self.parentofficeaddlabel = Label(self.lf2, text="Parent Office Add.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.parentofficeaddlabel.place(x=600, y= 20)
        self.parentofficeadd_var = StringVar()
        self.parentofficeaddentry = Text(self.lf2, font=(self.f1,10))
        self.parentofficeaddentry.place(x=900, y=20, height=60, width=200)
        
        self.parentofficephnolabel = Label(self.lf2, text="Parent Office Phone NO.", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.parentofficephnolabel.place(x=600, y=100)
        self.parentofficephno_var = StringVar()
        self.parentofficephnoentry = Entry(self.lf2, textvariable=self.parentofficephno_var, font=(self.f1,15))
        self.parentofficephnoentry.place(x=900, y=100, height=30, width=200)
        
        self.feelabel = Label(self.lf2, text="Fee", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.feelabel.place(x=600, y=150)
        self.fee_var = StringVar()
        self.feeentry = Entry(self.lf2, textvariable=self.fee_var, font=(self.f1,15))
        self.feeentry.place(x=900, y=150, height=30, width=200)
                
        self.dateofbirthlabel = Label(self.lf2, text="Date Of Birth", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.dateofbirthlabel.place(x=600, y=200)
        self.dateofbirth_var = StringVar()
        self.dateofbirthentry = DateEntry(self.lf2, width=12, background='darkblue', font=(self.f1, 15), date_pattern='dd/mm/yyyy',foreground='white', borderwidth=2, state="readonly")
        self.dateofbirthentry.place(x=900, y=200, width=200, height=30)
        
        self.selectcategorylabel = Label(self.lf2, text="Select Category", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.selectcategorylabel.place(x=600, y=250)
        self.selectcategory_var = StringVar()
        self.selectcategoryentry = Combobox(self.lf2, state="readonly", font=(self.f1, 15), textvariable=self.selectcategory_var)
        self.selectcategoryentry.place(x=900, y=250, height=30, width=200)
        self.selectcategoryentry['values'] = ["ST", "SC", "OBC", "OPEN", "Other"]
        self.selectcategory_var.set("Select Category")
        
        self.bloodgrouplabel = Label(self.lf2, text="Blood Group", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.bloodgrouplabel.place(x=600, y = 300)
        self.bloodgroup_var = StringVar()
        self.bloodgroupentry = Combobox(self.lf2, state="readonly", font=(self.f1, 15), textvariable=self.bloodgroup_var)
        self.bloodgroupentry.place(x=900, y=300, height=30, width=200)
        self.bloodgroupentry['values'] = ["A+", "B+", "A-", "B-", "AB+", "O+", "O-"]
        self.bloodgroup_var.set("Select Blood Group")
        
        self.castelabel = Label(self.lf2, text="Caste", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.castelabel.place(x=600, y=350)
        self.caste_var = StringVar()
        self.casteentry = Entry(self.lf2, textvariable=self.caste_var, font=(self.f1,15))
        self.casteentry.place(x=900, y=350, height=30, width=200)
        
        self.selectstreamlabel = Label(self.lf2, text="Select Stream", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.selectstreamlabel.place(x=600, y=450)
        self.selectstream_var = StringVar()
        self.selectstreamentry = Combobox(self.lf2, state="readonly", font=(self.f1, 15), textvariable=self.selectstream_var)
        self.selectstreamentry.place(x=900, y=450, height=30, width=200)
        self.selectstreamentry['values'] = ["Sci", "Com"]
        self.selectstream_var.set("Select Stream")
        
        self.academicyearlabel = Label(self.lf2, text="Academic Year", bd=2, bg=self.bgclr1, fg="black", font=(self.f1, 15),relief=GROOVE)
        self.academicyearlabel.place(x=600, y=400)
        self.academicyear_var = IntVar()
        self.academicyearentry = Checkbutton(self.lf2, text="Admission in current year",bg =self.bgclr1, variable=self.academicyear_var, font=(self.f1, 10), onvalue = 0, offvalue = 1, height=5, width=20)
        self.academicyearentry.place(x=900, y=400, height=30, width=200)
        
        self.submitbutton = Button(self.lf2, text="SUBMIT", bg=self.bgclr2, font=(self.f2, 15), bd=5, command=self.submit)
        self.submitbutton.place(x=1200, y=200, width=100, height=30)
        
        self.resetbutton = Button(self.lf2, text="RESET", bg=self.bgclr2, font=(self.f2, 15), bd=5, command=self.reset)
        self.resetbutton.place(x=1200, y=300, width=100, height=30)
        
        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()