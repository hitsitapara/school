from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from datetime import date


class ViewStaff(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def select_combo_method(self,event=""):
        # form lakhay ne aavse.,';
        self.lf2 = LabelFrame(self, text="View Staff", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=100, height=600, width=1350)

        self.firstname = Label(self.lf2, text='firstname', bd=2, bg="black", fg="white",relief=GROOVE)
        self.middlename = Label(self.lf2, text='middlename', bd=2, bg="black", fg="white",relief=GROOVE)
        self.lastname = Label(self.lf2, text='lastname', bd=2, bg="black", fg="white",relief=GROOVE)
        self.salary = Label(self.lf2, text='salary', bd=2, bg="black", fg="white", relief=GROOVE)
        self.phoneno = Label(self.lf2, text='phoneno', bd=2, bg="black", fg="white",relief=GROOVE)
        self.address = Label(self.lf2, text='address', bd=2, bg="black", fg="white",relief=GROOVE)
        self.email = Label(self.lf2, text='email', bd=2, bg="black", fg="white", relief=GROOVE)
        self.password = Label(self.lf2, text='password', bd=2, bg="black", fg="white", relief=GROOVE)
        self.authority = Label(self.lf2, text="authority", bd=2, bg="black", fg="white", relief=GROOVE)
        self.joindate = Label(self.lf2, text="Join-Date", bd=2, bg="black", fg="white", relief=GROOVE)
        self.dob = Label(self.lf2, text="DOB", bd=2, bg="black", fg="white", relief=GROOVE)
        self.category = Label(self.lf2, text="Category", bd=2, bg="black", fg="white", relief=GROOVE)
        self.bloodgroup = Label(self.lf2, text="Blood-Group", bd=2, bg="black", fg="white", relief=GROOVE)
        self.cast = Label(self.lf2, text="Cast", bd=2, bg="black", fg="white", relief=GROOVE)

        self.firstnamevar = StringVar()
        self.firstnameentry = Entry(self.lf2, textvariable=self.firstnamevar)
        self.middlenamevar = StringVar()
        self.middlenameentry = Entry(self.lf2, textvariable=self.middlenamevar)
        self.lastnamevar = StringVar()
        self.lastnameentry = Entry(self.lf2, textvariable=self.lastnamevar)
        self.salaryvar = StringVar()
        self.salaryentry = Entry(self.lf2, textvariable=self.salaryvar)
        self.phonenovar = StringVar()
        self.phonenoentry = Entry(self.lf2, textvariable=self.phonenovar)
        self.emailvar = StringVar()
        self.emailentry = Entry(self.lf2, textvariable=self.emailvar)
        self.passwordvar = StringVar()
        self.passwordentry = Entry(self.lf2, textvariable=self.passwordvar)
        self.addressentry = Text(self.lf2, width=20, height=3,wrap=WORD)
        self.authorityvar = StringVar()
        self.authorityentry = Entry(self.lf2, textvariable=self.authorityvar)
        self.joindatevar = StringVar()
        self.joindateentry = Entry(self.lf2, textvariable=self.joindatevar)
        self.dobvar = StringVar()
        self.dobentry = Entry(self.lf2, textvariable=self.dobvar)
        self.categoryvar = StringVar()
        self.categoryentry = Entry(self.lf2, textvariable=self.categoryvar)
        self.bloodgroupvar = StringVar()
        self.bloodgroupentry = Entry(self.lf2, textvariable=self.bloodgroupvar)
        self.castvar = StringVar()
        self.castentry = Entry(self.lf2, textvariable=self.castvar)

        self.firstname.place(x=5, y=35, height=25)
        self.firstnameentry.place(x=250, y=35, height=25, width=150)
        self.middlename.place(x=5, y=65, height=25)
        self.middlenameentry.place(x=250, y=65, height=25, width=150)
        self.lastname.place(x=5, y=95, height=25)
        self.lastnameentry.place(x=250, y=95, height=25, width=150)
        self.salary.place(x=5, y=125, height=25)
        self.salaryentry.place(x=250, y=125, height=25, width=150)
        self.phoneno.place(x=5, y=155, height=25)
        self.phonenoentry.place(x=250, y=155, height=25, width=150)
        self.email.place(x=5, y=185, height=25)
        self.emailentry.place(x=250, y=185, height=25, width=150)
        self.password.place(x=5, y=215, height=25)
        self.passwordentry.place(x=250, y=215, height=25, width=150)
        self.address.place(x=5, y=245, height=25)
        self.addressentry.place(x=250, y=245, height=75, width=150)
        self.authority.place(x=5, y=335, height=25)
        self.authorityentry.place(x=250, y=335, height=25, width=150)
        self.joindate.place(x=5, y=365, height=25)
        self.joindateentry.place(x=250, y=365, height=25, width=150)
        self.dob.place(x=5, y=395, height=25)
        self.dobentry.place(x=250, y=395, height=25, width=150)
        self.category.place(x=5, y=425, height=25)
        self.categoryentry.place(x=250, y=425, height=25, width=150)
        self.bloodgroup.place(x=5, y=455, height=25)
        self.bloodgroupentry.place(x=250, y=455, height=25, width=150)
        self.cast.place(x=5, y=485, height=25)
        self.castentry.place(x=250, y=485, height=25, width=150)

        self.update_query = "select * from staff where empno=" + str(self.select_user_combo.get())
        self.update_query_tuple = self.conn.execute(self.update_query).fetchone()

        self.firstnamevar.set(self.update_query_tuple[1])
        self.middlenamevar.set(self.update_query_tuple[2])
        self.lastnamevar.set(self.update_query_tuple[3])
        self.salaryvar.set(self.update_query_tuple[4])
        self.phonenovar.set(self.update_query_tuple[5])
        self.addressentry.insert(END, self.update_query_tuple[6])
        self.emailvar.set(self.update_query_tuple[7])
        self.authorityvar.set(self.update_query_tuple[8])
        self.passwordvar.set(self.update_query_tuple[10])
        self.joindatevar.set(self.update_query_tuple[12])
        self.dobvar.set(self.update_query_tuple[13])
        self.categoryvar.set(self.update_query_tuple[14])
        self.bloodgroupvar.set(self.update_query_tuple[15])
        self.castvar.set(self.update_query_tuple[16])

        self.firstnameentry.config(state="disabled")
        self.middlenameentry.config(state="disabled")
        self.lastnameentry.config(state="disabled")
        self.salaryentry.config(state="disabled")
        self.phonenoentry.config(state="disabled")
        self.emailentry.config(state="disabled")
        self.passwordentry.config(state="disabled")
        self.addressentry.config(state="disabled")
        self.authorityentry.config(state="disabled")
        self.joindateentry.config(state="disabled")
        self.dobentry.config(state="disabled")
        self.categoryentry.config(state="disabled")
        self.bloodgroupentry.config(state="disabled")
        self.castentry.config(state="disabled")

        self.generate_button = Button(self.lf2, text="Generate Report", command=self.staff_report_pdf_method)
        self.generate_button.place(x=300, y=545)

        self.cancel_button = Button(self.lf2, text="Cancel", command=self.cancel_method)
        self.cancel_button.place(x=400, y=545)

    def staff_report_pdf_method(self):
        pdf = canvas.Canvas("C:\\Reports\\View\\Staff\\report_{}_{}.pdf".format(self.select_user_combo.get(), self.update_query_tuple[1]))
        pdf.setPageSize((600, 900))
        pdf.line(10, 700, 590, 700)
        pdf.line(10, 860, 590, 860)
        pdf.line(20, 690, 20, 870)
        pdf.line(580, 690, 580, 870)
        pdf.setFont("Courier-Bold", 20)
        pdf.drawString(220, 880, "SCHOOL NAME")
        pdf.drawString(200, 840, "Staff-Info")
        pdf.setFont("Courier-Bold", 15)
        pdf.drawString(30, 815, "Staff Name : {} {} {}".format(self.update_query_tuple[1], self.update_query_tuple[2], self.update_query_tuple[3]))
        pdf.drawString(30, 790, "Emp No. : {}".format(self.select_user_combo.get()))
        pdf.drawString(30, 765, "Date : {}".format(date.today()))
        pdf.setFont("Courier-Bold", 12)
        pdf.drawString(30, 680, "Salary : {}".format(self.update_query_tuple[4]))
        pdf.drawString(30, 617.28, "Phone no. : {}".format(self.update_query_tuple[5]))
        pdf.drawString(30, 554.56, "Email : {}".format(self.update_query_tuple[7]))
        pdf.drawString(30, 491.84, "Password : {}".format(self.update_query_tuple[10]))
        pdf.drawString(30, 429.12, "Address : {}".format(self.update_query_tuple[6]))
        pdf.drawString(30, 366.4, "Authority : {}".format(self.update_query_tuple[8]))
        pdf.drawString(30, 303.68, "Join-Date : {}".format(self.update_query_tuple[12]))
        pdf.drawString(30, 240.96, "DOB : {}".format(self.update_query_tuple[13]))
        pdf.drawString(30, 178.24, "Category : {}".format(self.update_query_tuple[14]))
        pdf.drawString(30, 115.52, "Blood-group : {}".format(self.update_query_tuple[15]))
        pdf.drawString(30, 52.8, "Cast : {}".format(self.update_query_tuple[16]))
        pdf.save()

    def cancel_method(self):
        self.lf2.destroy()
        self.select_user_combo_var.set("Select emp-no.")
        self.select_user_combo.focus_set()

    def __init__(self, root, main_root):

        self.main_root = main_root
        self.root = root
        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            messagebox.showerror("School Software", "There is some error in connection of Database")
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

        bb = Button(self, image = imgl, bd=5, font=(self.f1, 20), bg=self.bgclr2, command=self.backf)
        bb.pack()

        query1 = "select empno from staff where currentuser=0;"
        list1 = self.conn.execute(query1).fetchall()
        my_list = []
        for i in list1:
            my_list.append(i)

        self.select_user_combo_var = StringVar()
        self.select_user_combo = ttk.Combobox(self, values=my_list, height=10, textvariable= self.select_user_combo_var,state="readonly")
        self.select_user_combo.bind("<<ComboboxSelected>>", self.select_combo_method)
        self.select_user_combo.place(x=100, y=45)
        self.select_user_combo_var.set("SELECT EMP-NO.")
        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
