from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import json
from datetime import date, timedelta
from reportlab.pdfgen import canvas
import webbrowser

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
        self.combo_roll_var = StringVar()
        self.roll_combo = ttk.Combobox(self,values=self.rollno, textvariable=self.combo_roll_var ,height=20,state="readonly")
        self.roll_combo.place(x=100,y=400)
        self.roll_combo.bind("<<ComboboxSelected>>",self.report_method)
        self.combo_roll_var.set("Select")

    def report_method(self,event=""):
        self.report_button = Button(self,text='Generate Report',command=self.generate_report_method)
        self.report_button.place(x=200,y=600)

    def generate_report_method(self):
        query1 = "select abday,grno,fname,mname,lname from master where rollno = ? and standard = ?"
        self.data = self.conn.execute(query1,(self.roll_combo.get(),self.std_combo.get())).fetchone()
        self.returned_none = False
        if self.data[0] is not None:
            self.abday_list = json.loads(self.data[0])
        else:
            self.returned_none = True
        self.report_pdf()

    def report_pdf(self):

        pdf = canvas.Canvas("C:\\Reports\\Attendence\\Student\\report_{}_{}_{}_to_{}.pdf".format(self.std_combo.get() , self.roll_combo.get(), self.from_cal.get_date(), self.to_cal.get_date()) )
        pdf.setPageSize((600,900))
        pdf.line(10,700,590,700)
        pdf.line(10,860,590,860)
        pdf.line(20,690,20,870)
        pdf.line(580,690,580,870)
        pdf.setFont("Courier-Bold", 20)
        pdf.drawString(200,880,"Attendence Report")
        pdf.setFont("Courier-Bold", 15)
        pdf.drawString(30,840,"Student Name : {} {} {}".format(self.data[2], self.data[3], self.data[4]))
        pdf.drawString(30,815,"Standard : {}".format(self.std_combo.get()))
        pdf.drawString(30,790,"Roll No : {}".format(self.roll_combo.get()))
        pdf.drawString(30,765,"Gr No : {}".format(self.data[1]))
        pdf.drawString(30,740,"From Date : {}".format(self.from_cal.get_date()))
        pdf.drawString(30,715,"To Date : {}".format(self.to_cal.get_date()))
        pdf.line(35, 670, 550 , 670)
        pdf.drawString(40, 655, "Sr No.")
        pdf.drawString(300, 655, "Absent Dates")
        pdf.line(35, 650, 550 , 650)
        pdf.line(120, 670, 120 , 30)
        top = 620
        sr = 1

        if not self.returned_none:
            for i in self.abday_list:
                if top<30:
                    pdf.showPage()
                    top = 830
                    pdf.setFont("Courier-Bold", 15)
                    pdf.drawString(40, 855, "Sr No.")
                    pdf.drawString(300, 855, "Absent Dates")
                    pdf.line(35, 870, 550 , 870)
                    pdf.line(35, 850, 550 , 850)
                    pdf.line(120, 870, 120 , 30)
                pdf.drawString(50, top, str(sr))
                pdf.drawString(320, top, str(i))
                
                top -= 750
                sr += 1
        else:
            pdf.drawString(50, 500, "There is No Absent Days Recorded for This Student !")

        pdf.save()
        print("succesfull")
        webbrowser.open("C:\\Reports\\Attendence\\Student\\report_{}_{}_{}_to_{}.pdf".format(self.std_combo.get() , self.roll_combo.get(), self.from_cal.get_date(), self.to_cal.get_date()))

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
        self.combo_std_var = StringVar()
        self.std_combo = ttk.Combobox(self,values=self.student, textvariable =self.combo_std_var , height=10,state="readonly")
        self.std_combo.place(x=100,y=300)
        self.std_combo.bind("<<ComboboxSelected>>",self.std_combo_method)
        self.combo_std_var.set("Select")

        self.protocol("WM_DELETE_WINDOW", self.c_w)

