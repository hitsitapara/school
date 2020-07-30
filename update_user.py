from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from validate_email import validate_email
from registration import Registration

class UpdateUser(Toplevel):

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

    def update_button_method(self):
        #   """" ''' """     form  mathi  data -> database  ma  jase     """ ''' """
        try:
            a = self.firstnameentry.get().isalpha()
            if a:
                pass
            else:
                raise ValueError
        except:
            messagebox.showerror("School Software", "First name can't be number!")
            self.firstnamevar.set("")
            return
        try:
            a = self.middlenameentry.get().isalpha()
            if a:
                pass
            else:
                raise ValueError
        except:
            messagebox.showerror("School Software", "Middle name can't be number!")
            self.middlenamevar.set("")
            return
        try:
            a = self.lastnameentry.get().isalpha()
            if a:
                pass
            else:
                raise ValueError
        except:
            messagebox.showerror("School Software", "Last name can't be number!")
            self.lastnamevar.set("")
            return
        try:
            if (self.firstnameentry.get() == "" or self.middlenameentry.get() == "" or self.lastnameentry.get() == "" or self.salaryentry.get() == "" or self.phonenoentry.get() == "" or self.addressentry.get(1.0, END) == "\n\n" or self.emailentry.get() == "" or self.passwordentry.get() == ""):
                raise AttributeError
        except:
            messagebox.showerror("School Software", "Any Entry Field Can't Be Empty")
            return

        try:
            self.sal = int(self.salaryentry.get())
            if self.sal >= 0:
                pass
            else:
                raise ValueError
        except:
            messagebox.showerror("School Software", "Salary must be numeric")
            self.salaryvar.set("")
            self.salaryentry.focus_set()
            return

        try:
            self.phno = int(self.phonenoentry.get())
            if self.phno >= 0:
                pass
            else:
                raise ValueError
        except:
            messagebox.showerror("School Software", "Phonenember must be numeric")
            self.phonenovar.set("")
            self.phonenoentry.focus_set()
            return

        try:
            self.phno1 = list(self.phonenoentry.get())
            if len(self.phno1) != 10:
                raise ValueError
        except:
            messagebox.showerror("School Software", "Phonenumber must be of 10-digit")
            self.phonenovar.set("")
            self.phonenoentry.focus_set()
            return

        try:
            self.phno2 = ('9', '8', '7', '6')
            if (self.phno1[0] not in self.phno2):
                raise ValueError
        except:
            messagebox.showerror("School Software", "Phonenumber must be valid")
            self.phonenovar.set("")
            self.phonenoentry.focus_set()
            return

        valid = validate_email(self.emailentry.get())
        if not valid:
            m = messagebox.showerror("Error", "email id must be valid")
            self.emailentry.focus_set()
            return

        if self.adminvar.get() == 1:
            self.authority_value = "admin"
        else:
            self.authority_value = "staff"

        self.answer=messagebox.askyesno("School Software","Do you really want to update user whose empno="+str(self.select_user_combo.get()))

        if self.answer>0:
            if(self.update_query_tuple[1]!=self.firstnameentry.get()):
                update_query1 = "Update staff set fname = '"+self.firstnameentry.get()+"' where empno="+str(self.select_user_combo.get())
                self.conn.execute(update_query1)

            if (self.update_query_tuple[2]!= self.middlenameentry.get()):
                update_query2 = "update staff set mname = '"+self.middlenameentry.get()+"' where empno="+str(self.select_user_combo.get())
                self.conn.execute(update_query2)

            if (self.update_query_tuple[3]!= self.lastnameentry.get()):
                update_query3 = "update staff set lname = '"+self.lastnameentry.get()+"' where empno="+str(self.select_user_combo.get())
                self.conn.execute(update_query3)

            if (self.update_query_tuple[4]!= self.salaryentry.get()):
                update_query4 = "update staff set salary = " + str(self.salaryentry.get())+" where empno="+str(self.select_user_combo.get())
                self.conn.execute(update_query4)

            if (self.update_query_tuple[5]!=self.phonenoentry.get()):
                update_query5 = "update staff set phno = '"+str(self.phonenoentry.get()) + "' where empno=" + str(self.select_user_combo.get())
                self.conn.execute(update_query5)

            if (self.update_query_tuple[6]!=self.addressentry.get(1.0,END)):
                update_query6 = "update staff set address = '" + str(self.addressentry.get(1.0,END)) + "' where empno=" + str(self.select_user_combo.get())
                self.conn.execute(update_query6)

            if (self.update_query_tuple[7]!=self.emailentry.get()):
                update_query7 = "update staff set email = '" + str(self.emailentry.get()) + "' where empno=" + str(self.select_user_combo.get())
                self.conn.execute(update_query7)

            if (self.update_query_tuple[8]!=self.authority_value):
                update_query8 = "update staff set authority = '" + str(self.authority_value) + "' where empno=" + str(self.select_user_combo.get())
                self.conn.execute(update_query8)

            if (self.update_query_tuple[10]!=self.passwordentry.get()):
                update_query10 = "update staff set password = '" + str(self.passwordentry.get()) + "' where empno=" + str(self.select_user_combo.get())
                self.conn.execute(update_query10)

            self.conn.commit()
            messagebox.showinfo("School Software","Operation Successful")
            self.select_user_combo.set("")
            self.lf2.destroy()
        else:
            return

    def reset(self):

        self.firstnamevar.set("")
        self.firstnameentry.focus_set()
        self.middlenamevar.set("")
        self.lastnamevar.set("")
        self.salaryvar.set("")
        self.phonenovar.set("")
        self.emailvar.set("")
        self.passwordvar.set("")
        self.addressentry.delete(1.0,END)

    def select_combo_method(self,event=""):
        # form lakhay ne aavse.,';
        self.lf2 = LabelFrame(self, text="Update User", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=200, height=500, width=1350)

        self.firstname = Label(self.lf2, text='firstname', bd=2, bg="black", fg="white", font=(self.f1, 15),
                               relief=GROOVE)
        self.middlename = Label(self.lf2, text='middlename', bd=2, bg="black", fg="white", font=(self.f1, 15),
                                relief=GROOVE)
        self.lastname = Label(self.lf2, text='lastname', bd=2, bg="black", fg="white", font=(self.f1, 15),
                              relief=GROOVE)
        self.salary = Label(self.lf2, text='salary', bd=2, bg="black", fg="white", font=(self.f1, 15),
                            relief=GROOVE)
        self.phoneno = Label(self.lf2, text='phoneno', bd=2, bg="black", fg="white", font=(self.f1, 15),
                             relief=GROOVE)
        self.address = Label(self.lf2, text='address', bd=2, bg="black", fg="white", font=(self.f1, 15),
                             relief=GROOVE)
        self.email = Label(self.lf2, text='email', bd=2, bg="black", fg="white", font=(self.f1, 15), relief=GROOVE)
        self.password = Label(self.lf2, text='password', bd=2, bg="black", fg="white", font=(self.f1, 15),
                              relief=GROOVE)

        self.firstnamevar = StringVar()
        self.firstnameentry = Entry(self.lf2, textvariable=self.firstnamevar, font=(self.f1, 10))
        self.middlenamevar = StringVar()
        self.middlenameentry = Entry(self.lf2, textvariable=self.middlenamevar, font=(self.f1, 10))
        self.lastnamevar = StringVar()
        self.lastnameentry = Entry(self.lf2, textvariable=self.lastnamevar, font=(self.f1, 10))
        self.salaryvar = StringVar()
        self.salaryentry = Entry(self.lf2, textvariable=self.salaryvar, font=(self.f1, 10))
        self.phonenovar = StringVar()
        self.phonenoentry = Entry(self.lf2, textvariable=self.phonenovar, font=(self.f1, 10))
        self.emailvar = StringVar()
        self.emailentry = Entry(self.lf2, textvariable=self.emailvar, font=(self.f1, 10))
        self.passwordvar = StringVar()
        self.passwordentry = Entry(self.lf2, textvariable=self.passwordvar,  show="*", font=(self.f1, 10))
        self.addressentry = Text(self.lf2, width=20, height=3,wrap=WORD)

        self.firstname.place(x=175, y=2)
        self.firstnameentry.place(x=970, y=2)
        self.middlename.place(x=175, y=52)
        self.middlenameentry.place(x=970, y=52)
        self.lastname.place(x=175, y=102)
        self.lastnameentry.place(x=970, y=102.5)
        self.salary.place(x=175, y=152)
        self.salaryentry.place(x=970, y=152)
        self.phoneno.place(x=175, y=202)
        self.phonenoentry.place(x=970, y=202)
        self.email.place(x=175, y=252)
        self.emailentry.place(x=970, y=252)
        self.password.place(x=175, y=302)
        self.passwordentry.place(x=970, y=302)
        self.address.place(x=175, y=352)
        self.addressentry.place(x=970, y=352)

        rowcounter = "select count(*) from staff;"
        rc = self.conn.execute(rowcounter).fetchone()
        self.adminvar = IntVar()
        self.admin = Checkbutton(self.lf2, text='admin', variable=self.adminvar
                                 )
        self.admin.place(x=175, y=402)
        self.authority_value = "abcd"

        self.update_query="select * from staff where empno="+str(self.select_user_combo.get())
        self.update_query_tuple = self.conn.execute(self.update_query).fetchone()

        self.firstnamevar.set(self.update_query_tuple[1])
        self.middlenamevar.set(self.update_query_tuple[2])
        self.lastnamevar.set(self.update_query_tuple[3])
        self.salaryvar.set(self.update_query_tuple[4])
        self.phonenovar.set(self.update_query_tuple[5])
        self.addressentry.insert(END,self.update_query_tuple[6])
        self.emailvar.set(self.update_query_tuple[7])

        if self.update_query_tuple[8] == 'admin':
            if rc[0] == 1:
                self.admin.config(state='disabled')
            self.adminvar.set(1)
        else:
            self.adminvar.set(0)
        self.passwordvar.set(self.update_query_tuple[10])

        self.update_button = Button(self.lf2, text="Update", command=self.update_button_method)
        self.update_button.place(x=500, y=432)

        self.reset_btn = Button(self.lf2, text="Reset",  command=self.reset)
        self.reset_btn.place(x=645, y=432)


    def __init__(self, root, main_root):
        self.main_root = main_root
        self.root = root
        try:
            self.conn = sqlite3.connect('sinfo.db')

        except:
            messagebox.showerror("School Project", "There is some error in connection of Database")
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"
        self.title("Update User")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        ##====================================================frame 1===================================================

        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)
        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 15), command=self.backf)
        bb.place(x=10, y=10, height=25)
        ##==================================================frame 2=====================================================

        query1 = "select empno from staff where currentuser=0;"
        list1 = self.conn.execute(query1).fetchall()
        my_list = []
        for i in list1:
            my_list.append(i)

        self.select_user_combo = ttk.Combobox(self, values=my_list,height=10)
        self.select_user_combo.bind("<<ComboboxSelected>>",self.select_combo_method)
        self.select_user_combo.place(x=750, y=150)

        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()
