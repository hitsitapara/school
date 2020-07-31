from tkinter import *
from tkinter import  messagebox
from tkinter.ttk import Combobox
import sqlite3
from PIL import Image, ImageTk


class InsertStudent(Toplevel):

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

            # ========================================================validation function============================================================

    def validNumber(self, s):
        Pattern = re.compile("(0/91)?[6-9][0-9]{9}")
        return Pattern.match(s)

    def validEmail(self, s):
        Pattern = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
        return Pattern.match(s)

    def validName(self, s):
        Pattern = re.compile("([A-Za-z]+)*$")
        return Pattern.match(s)

    def validRollno(self, s):
        Pattern = re.compile("^[0-9]*$")
        return Pattern.match(s)

    def validDivision(self, s):
        Pattern = re.compile("([A-Za-z]+)*$")
        return Pattern.match(s)

    def validFee(self, s):
        Pattern = re.compile("^[0-9]*$")
        return Pattern.match(s)

        # ===========================================================to get gr number=========================================================

    def getGrno(self):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            grnoCount = """SELECT grno FROM master WHERE grno = (SELECT MAX(grno) FROM master);"""
            cursor.execute(grnoCount)
            return cursor.fetchall()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

        # ===========================================================to get Roll number=========================================================

    def getRollno(self, std, ):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            grnoCount = """SELECT MAX(rollno) FROM master WHERE standard = ?;"""
            data_tuple = (std,)
            cursor.execute(grnoCount, data_tuple)
            return cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
            print("here")
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

        # ============================================================to set all field as null========================================================

    def setValue(self):
        self.rno = "-"
        self.std.set("")
        self.medium.set("Select Medium")
        self.stream.set("Select Stream")
        self.cbd2()
        # self.div.set("")
        self.fname.set("")
        self.mname.set("")
        self.lname.set("")
        self.addressentry.delete(1.0, END)
        self.phnos.set("")
        self.phnop.set("")
        self.email.set("")
        self.poaddentry.delete(1.0, END)
        self.pophno.set("")
        self.fee.set("")

        # ============================================================to insert value in database========================================================

    def insertVaribleIntoTable(self, rollno, std, fname, mname, lname, address, phnos, phnop, email, poadd, pophno, fee):

        try:

            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert = """INSERT INTO master
                                   (rollno, standard, fname, mname, lname, address, student_phno, parents_phno, email, parent_office_address, parents_office_phno, fee) 
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

            data_tuple = (rollno, std, fname, mname, lname, address, phnos, phnop, email, poadd, pophno, fee)
            cursor.execute(sqlite_insert, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into detail table")
            messagebox.showinfo('Successfully done', 'Entry is done in database')

            text = Label(self,text="GR no.")
            text.place(x=300, y=5, height=25)
            self.grno = int(self.getGrno()[0][0])
            text = Label(self,text=self.grno)
            text.place(x=400, y=5, height=25)

            self.grn = "Your Gr number is " + str(self.grno)
            messagebox.showinfo('GR number', self.grn)

            if (int(self.std.get()) < 11):

                print(self.getRollno(self.std.get() + "~" + self.medium.get()))
                self.rno = str(self.getRollno(self.std.get() + "~" + self.medium.get())[0][0])

            else:

                print(self.getRollno(self.std.get() + "~" + self.medium.get() + "~" + self.stream.get()))
                self.rno = str(
                    self.getRollno(self.std.get() + "~" + self.medium.get() + "~" + self.stream.get())[0][0])

            text = Label(self,text="Roll no.")
            text.place(x=300, y=35, height=25)
            self.roll = Label(self,text=self.rno)
            self.roll.place(x=400, y=35, height=25)

            self.rn = "Your Roll number is " + (self.rno)
            messagebox.showinfo('Roll number', self.rn)

            cursor.close()


        except sqlite3.Error as error:

            print("Failed to insert Python variable into sqlite table", error)
            messagebox.showinfo('Error!!!!', 'Entry is not done in database')
        finally:

            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

        # ==========================================================to check validation==========================================================

    def submitvalue(self):

        self.address = self.addressentry.get(1.0, END)
        self.poadd = self.poaddentry.get(1.0, END)
        if (self.validNumber(self.phnop.get()) and self.validNumber(self.phnos.get()) and self.validNumber(
                self.pophno.get()) and (len(self.phnos.get()) == 10) and (len(self.phnop.get()) == 10) and (
                len(self.pophno.get()) == 10)):

            if (self.validEmail(self.email.get()) and self.medium.get() != "Select Medium"):

                if (self.validName(self.fname.get()) and self.validName(self.mname.get()) and self.validName(
                        self.lname.get()) and (self.fname.get() != "") and (self.mname.get() != "") and (
                        self.lname.get() != "")):

                    if (((self.std.get() != "") and (int(self.std.get()) >= 1) and (
                            int(self.std.get()) <= 12)) and (
                            (self.fee.get() != "") and self.validFee(self.fee.get()))):

                        if (int(self.std.get()) < 11):
                            text = Label(self,text="Roll no.")
                            text.place(x=300, y=35, height=25)
                            self.rno = self.getRollno(self.std.get() + "~" + self.medium.get())
                            print(self.rno)
                            if (self.rno[0][0] == None or len(self.rno) == 0):
                                self.rno = str(1)
                            else:
                                print(self.rno)
                                self.rno = str(
                                    self.getRollno(self.std.get() + "~" + self.medium.get())[0][0] + 1)
                            self.roll = Label(self,text=self.rno)
                            self.roll.place(x=400, y=35, height=25)
                            self.insertVaribleIntoTable(self.rno, self.std.get() + "~" + self.medium.get(),
                                                        self.fname.get(), self.mname.get(), self.lname.get(),
                                                        self.address, self.phnos.get(), self.phnop.get(),
                                                        self.email.get(), self.poadd, self.pophno.get(),
                                                        self.fee.get())
                            self.setValue()
                            self.stdentry.focus_set()
                            text = Label(self,text="GR no.")
                            text.place(x=300, y=5, height=25)
                            self.grno = self.getGrno()
                            if (len(self.grno) == 0):
                                self.grno = 1
                            else:
                                self.grno = self.getGrno()[0][0] + 1
                            text = Label(self,text=self.grno)
                            text.place(x=400, y=5, height=25)
                            text = Label(self,text="Roll no.")
                            text.place(x=300, y=35, height=25)
                            self.roll = Label(self,text=self.rno)
                            self.roll.place(x=400, y=35, height=25)
                            print("done")

                        else:
                            text = Label(self,text="Select Stream : ")
                            text.place(x=300, y=125, height=25)
                            self.cb2()
                            self.cbp2()

                            if (self.stream.get() == "Select Stream"):
                                messagebox.showinfo('Error', 'Please select stream')

                            else:

                                text = Label(self,text="Roll no.")
                                text.place(x=300, y=35, height=25)
                                self.rno = self.getRollno(
                                    self.std.get() + "~" + self.medium.get() + "~" + self.stream.get())
                                print(self.rno)
                                if (len(self.rno) == 0 or self.rno[0][0] == None):
                                    self.rno = str(1)
                                else:
                                    print(self.rno)
                                    self.rno = str(self.getRollno(
                                        self.std.get() + "~" + self.medium.get() + "~" + self.stream.get())[0][
                                                       0] + 1)
                                self.roll = Label(self,text=self.rno)
                                self.roll.place(x=400, y=35, height=25)
                                self.insertVaribleIntoTable(self.rno,
                                                            self.std.get() + "~" + self.medium.get() + "~" + self.stream.get(),
                                                            self.fname.get(), self.mname.get(),
                                                            self.lname.get(),
                                                            self.address, self.phnos.get(), self.phnop.get(),
                                                            self.email.get(), self.poadd, self.pophno.get(),
                                                            self.fee.get())
                                self.setValue()
                                self.stdentry.focus_set()
                                text = Label(self,text="GR no.")
                                text.place(x=300, y=5, height=25)
                                self.grno = self.getGrno()
                                if (len(self.grno) == 0):
                                    self.grno = 1
                                else:
                                    self.grno = self.getGrno()[0][0] + 1
                                text = Label(self,text=self.grno)
                                text.place(x=400, y=5, height=25)
                                text = Label(self,text="Roll no.")
                                text.place(x=300, y=35, height=25)
                                self.roll = Label(self,text=self.rno)
                                self.roll.place(x=400, y=35, height=25)
                                print("done")

                    else:

                        """if ((self.rno.get() == "") or (not(self.validRollno(self.rno.get())))):
                            self.rnoentry.focus_set()
                            tkinter.messagebox.showinfo('Error', 'Please enter valid Roll number')

                        elif (self.div.get() == ""):
                            self.diventry.focus_set()
                            tkinter.messagebox.showinfo('Error', 'Please enter Division')"""

                        if ((self.std.get() == "") or (int(self.std.get()) < 1) or (int(self.std.get()) > 12)):
                            self.stdentry.focus_set()
                            print(self.std.get())
                            print(type(self.std.get()))
                            messagebox.showinfo('Error', 'Please enter valid standard')

                        elif ((not (self.validFee(self.fee.get()))) or (self.fee.get() == "")):
                            self.feesentry.focus_set()
                            messagebox.showinfo('Error', 'Please enter valid fees')

                else:

                    if ((not (self.validName(self.fname.get()))) or (self.fname.get() == "")):
                        self.fnameentry.focus_set()
                        messagebox.showinfo('Error', 'Invalid first name')

                    elif ((not (self.validName(self.mname.get()))) or (self.mname.get() == "")):
                        self.mnameentry.focus_set()
                        messagebox.showinfo('Error', 'Invalid middle name')

                    elif ((not (self.validName(self.lname.get()))) or (self.lname.get() == "")):
                        self.lnameentry.focus_set()
                        messagebox.showinfo('Error', 'Invalid last name')

            else:

                if (self.medium.get() == "Select Medium"):

                    messagebox.showinfo('Error', 'please select medium')

                else:

                    self.emailentry.focus_set()
                    messagebox.showinfo('Error', 'Invalid email address')

        else:

            if ((not (self.validNumber(self.phnop.get()))) or (len(self.phnop.get()) != 10)):

                self.phnopentry.focus_set()
                messagebox.showinfo('Error', 'Invalid parent mobile number')

            elif ((not (self.validNumber(self.phnos.get()))) or (len(self.phnos.get()) != 10)):

                self.phnosentry.focus_set()
                messagebox.showinfo('Error', 'Invalid student mobile number')

            elif ((not (self.validNumber(self.pophno.get()))) or (len(self.pophno.get()) != 10)):

                self.pophnoentry.focus_set()
                messagebox.showinfo('Error', 'Invalid parent office mobile number')

        # ====================================================================================================================

    def cb2(self):
        text = Label(self.lf2,text="Select Stream : ")
        text.place(x=500, y=170, height=25)
        self.streamchoosen = Combobox(self.lf2, state="readonly", textvariable=self.stream)

        # ====================================================================================================================

    def cbp2(self):
        self.streamchoosen.place(x=640, y=170, height=25, width=200)

        self.streamchoosen['values'] = ["Sci", "Com"]

        # ====================================================================================================================

    def cbd2(self):
        self.streamchoosen.destroy()
    # ====================================================================================================================

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
        # ========================================================variables============================================================
        # self.rno = StringVar()
        self.std = StringVar()
        self.medium = StringVar()
        self.medium.set("Select Medium")
        self.stream = StringVar()
        self.stream.set("Select Stream")
        # self.div = StringVar()
        self.fname = StringVar()
        self.mname = StringVar()
        self.lname = StringVar()
        self.address = StringVar()
        self.phnos = StringVar()
        self.phnop = StringVar()
        self.email = StringVar()
        self.poadd = StringVar()
        self.pophno = StringVar()
        self.fee = StringVar()

        ##===================================================frame 1====================================================
        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((60, 15))

        imgl = ImageTk.PhotoImage(imagel)

        self.lf1 = LabelFrame(self, text="NAME", bd=2, bg="black", fg="white", font=(self.f1, 20), relief=GROOVE)
        self.lf1.place(x=0, y=0, height=150, width=1350)

        bb = Button(self.lf1, image=imgl, bd=5, font=(self.f1, 20), command=self.backf)
        bb.place(x=10, y=10)

        ##=============================================frame 2==========================================================
        self.lf2 = LabelFrame(self, text="Student Registration", bd=2, bg="black", fg="white", font=(self.f1, 20),
                              relief=GROOVE)
        self.lf2.place(x=0, y=150, height=550, width=1350)

        # ===========================================================Entry Fields======================================

        text = Label(self.lf2,text="GR no.")
        text.place(x=500, y=90, height=25)
        """self.grno = self.getGrno()
        if (len(self.grno) == 0):
            self.grno = 1
        else:
            self.grno = self.getGrno()[0][0] + 1
        self.grnotext = Label(self.lf2,text=self.grno)
        self.grnotext.place(x=400, y=5, height=25)"""

        """text = Label(self.lf2,text="Roll no.")
        text.place(x=5, y=5, height=25)
        self.rnoentry = Entry(self.lf2 textvariable=self.rno)
        self.rnoentry.place(x=100, y=5, height=25, width=150)"""

        text = Label(self.lf2,text="Select Medium : ")
        text.place(x=500, y=130, height=25)
        self.mediumchoosen = Combobox(self.lf2 ,state="readonly", textvariable=self.medium)
        self.mediumchoosen.place(x=640, y=130, height=25, width=200)

        self.mediumchoosen['values'] = ["Guj", "Eng"]

        # self.cb2()

        text = Label(self.lf2,text="Select Stream : ")
        text.place(x=500, y=170, height=25)
        self.streamchoosen = Combobox(self.lf2, state="readonly", textvariable=self.stream)

        text = Label(self.lf2,text="Std.")
        text.place(x=10, y=10, height=25)
        self.stdentry = Entry(self.lf2, textvariable=self.std)
        self.stdentry.place(x=150, y=10, height=25, width=150)
        self.stdentry.focus_set()

        text = Label(self.lf2,text="First name")
        text.place(x=10, y=50, height=25)
        self.fnameentry = Entry(self.lf2, textvariable=self.fname)
        self.fnameentry.place(x=150, y=50, height=25, width=150)

        text = Label(self.lf2,text="Middle name")
        text.place(x=10, y=90, height=25)
        self.mnameentry = Entry(self.lf2, textvariable=self.mname)
        self.mnameentry.place(x=150, y=90, height=25, width=150)

        text = Label(self.lf2,text="Last name")
        text.place(x=10, y=130, height=25)
        self.lnameentry = Entry(self.lf2, textvariable=self.lname)
        self.lnameentry.place(x=150, y=130, height=25, width=150)

        text = Label(self.lf2,text="Address")
        text.place(x=10, y=170, height=25)
        self.addressentry = Text(self.lf2, width=20, height=5, padx=2, pady=2, wrap=WORD)
        self.addressentry.place(x=150, y=170, height=75, width=150)

        text = Label(self.lf2,text="Student ph.")
        text.place(x=10, y=260, height=25)
        self.phnosentry = Entry(self.lf2, textvariable=self.phnos)
        self.phnosentry.place(x=150, y=260, height=25, width=150)

        text = Label(self.lf2,text="Parent ph.")
        text.place(x=10, y=300, height=25)
        self.phnopentry = Entry(self.lf2, textvariable=self.phnop)
        self.phnopentry.place(x=150, y=300, height=25, width=150)

        text = Label(self.lf2,text="Email id")
        text.place(x=10, y=340, height=25)
        self.emailentry = Entry(self.lf2, textvariable=self.email)
        self.emailentry.place(x=150, y=340, height=25, width=150)

        text = Label(self.lf2,text="Parent office add.")
        text.place(x=10, y=380, height=25)
        self.poaddentry = Text(self.lf2, width=20, height=5, padx=2, pady=2, wrap=WORD)
        self.poaddentry.place(x=150, y=380, height=75, width=150)

        text = Label(self.lf2,text="Parent office ph.")
        text.place(x=500, y=10, height=25)
        self.pophnoentry = Entry(self.lf2, textvariable=self.pophno)
        self.pophnoentry.place(x=640, y=10, height=25, width=150)

        text = Label(self.lf2,text="Fees")
        text.place(x=500, y=50, height=25)
        self.feesentry = Entry(self.lf2, textvariable=self.fee)
        self.feesentry.place(x=640, y=50, height=25, width=150)

        # =====================================================Button===============================================================

        btn = Button(self.lf2, text='Insert', bd='5', command=self.submitvalue)
        btn.place(x=550, y=450, height=25, width=150)

        # ====================================================================================================================
        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()
