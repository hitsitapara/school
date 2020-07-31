from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk


class RemoveUser(Toplevel):

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

    def remove_button_method(self):
        answer = messagebox.askyesno("School Software","Are you sure to want to remove this user")

        if answer>0:
            query="delete from staff where empno=" + str(self.remove_user_combo.get())
            self.conn.execute(query)
            self.conn.commit()
            self.remove_user_combo.set("")
            self.firstname.destroy()
            self.middlename.destroy()
            self.lastname.destroy()
            self.salary.destroy()
            self.phoneno.destroy()
            self.firstnameentry.destroy()
            self.middlenameentry.destroy()
            self.lastnameentry.destroy()
            self.salaryentry.destroy()
            self.phonenoentry.destroy()
            self.remove_user_button.destroy()
            query2 = "select empno from staff where currentuser=0;"
            list2 = self.conn.execute(query2).fetchall()
            my_list = []
            for i in list2:
                my_list.append(i)
            self.remove_user_combo.config(values=my_list)
        else:
            return

    def remove_combo_method(self,event=""):
        self.firstname = Label(self.lf2, text='firstname')
        self.middlename = Label(self.lf2, text='middlename')
        self.lastname = Label(self.lf2, text='lastname')
        self.salary = Label(self.lf2, text='salary')
        self.phoneno = Label(self.lf2, text='phoneno')

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

        self.firstname.place(x=175, y=202)
        self.firstnameentry.place(x=970, y=202)
        self.middlename.place(x=175, y=252)
        self.middlenameentry.place(x=970, y=252)
        self.lastname.place(x=175, y=302)
        self.lastnameentry.place(x=970, y=302)
        self.salary.place(x=175, y=352)
        self.salaryentry.place(x=970, y=352)
        self.phoneno.place(x=175, y=402)
        self.phonenoentry.place(x=970, y=402)

        queryfname = "select fname from staff where empno=" + str(self.remove_user_combo.get())
        querymname = "select mname from staff where empno=" + str(self.remove_user_combo.get())
        querylname = "select lname from staff where empno=" + str(self.remove_user_combo.get())
        querysalary = "select salary from staff where empno=" + str(self.remove_user_combo.get())
        queryphno = "select phno from staff where empno=" + str(self.remove_user_combo.get())

        fname = self.conn.execute(queryfname).fetchone()
        mname = self.conn.execute(querymname).fetchone()
        lname = self.conn.execute(querylname).fetchone()
        salary = self.conn.execute(querysalary).fetchone()
        phno = self.conn.execute(queryphno).fetchone()

        self.firstnamevar.set(fname[0])
        self.middlenamevar.set(mname[0])
        self.lastnamevar.set(lname[0])
        self.salaryvar.set(salary[0])
        self.phonenovar.set(phno[0])

        self.firstnameentry.config(state="disabled")
        self.middlenameentry.config(state="disabled")
        self.lastnameentry.config(state="disabled")
        self.salaryentry.config(state="disabled")
        self.phonenoentry.config(state="disabled")

        self.remove_user_button = Button(self.lf2,text="remove",command=self.remove_button_method)
        self.remove_user_button.place(x=550,y=450)

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

        ##===================================================frame1 ====================================================
        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))
        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), bg="white", command=self.backf)
        bb.place(x=10, y=10)
        ##===============================================frame 2========================================================
        self.lf2 = LabelFrame(self, text="Remove User", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf2.place(x=0, y=150, height=600, width=1350)

        query1 = "select empno from staff where currentuser=0;"
        list1 = self.conn.execute(query1).fetchall()
        my_list = []
        for i in list1:
            my_list.append(i)
        self.remove_user_combo = ttk.Combobox(self.lf2, values=my_list, height=10)
        self.remove_user_combo.bind("<<ComboboxSelected>>", self.remove_combo_method)
        self.remove_user_combo.pack()

        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()