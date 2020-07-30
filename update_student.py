from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
import sqlite3
from PIL import Image, ImageTk


class UpdateStudent(Toplevel):
    updater = 0

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

    def start(self):

        self.updater = 0
        self.stds = StringVar()
        self.stds.set("Select Standard")
        self.rno = StringVar()
        self.rno.set("Select Roll number")
        self.grno = StringVar()
        self.rollno = StringVar()
        self.std = StringVar()
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
        print(self.stds.get())

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

    # ========================================================to Update record============================================================

    def UpdateVaribleIntoTable(self, fname, mname, lname, address, phnos, phnop, email, poadd, pophno, fees, grno):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_update = """UPDATE master SET fname = ?, mname = ?, lname = ?, address = ?, student_phno = ?, parents_phno = ?, email = ?, parent_office_address = ?, parents_office_phno = ?, fee = ? WHERE grno = ?;"""

            data_tuple = (fname, mname, lname, address, phnos, phnop, email, poadd, pophno, fees, grno)
            cursor.execute(sqlite_update, data_tuple)
            sqliteConnection.commit()
            print("Python Variables Updated successfully into detail table")
            messagebox.showinfo('Successfully done', 'Entry is done in database')
            self.updater = 1
            cursor.close()

        except sqlite3.Error as error:
            print("update")
            print("Failed to insert Python variable into sqlite table", error)
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

            if (self.validEmail(self.email.get())):

                if (self.validName(self.fname.get()) and self.validName(self.mname.get()) and self.validName(
                        self.lname.get()) and (self.fname.get() != "") and (self.mname.get() != "") and (
                        self.lname.get() != "")):

                    if ((self.fee.get() != "") and self.validFee(self.fee.get())):

                        self.grn = str(self.getGrn(self.stds.get(), self.rnochoosen.get())[0][0])
                        self.UpdateVaribleIntoTable(self.fname.get(), self.mname.get(), self.lname.get(), self.address,
                                                    self.phnos.get(), self.phnop.get(), self.email.get(), self.poadd,
                                                    self.pophno.get(), self.fee.get(), self.grn)
                        self.setValue()
                        print("done")

                    else:

                        """if ((self.rno.get() == "") or (not(self.validRollno(self.rno.get())))):

                            self.rnoentry.focus_set()

                            messagebox.showinfo('Error', 'Please enter valid Roll number')


                        elif (self.div.get() == ""):

                            self.diventry.focus_set()

                            messagebox.showinfo('Error', 'Please enter Division')"""

                        """if ((self.stds.get() == "") or (self.stds.get() < "1") or (self.stds.get() > "12")):

                            self.stdentry.focus_set()

                            messagebox.showinfo('Error', 'Please enter valid standard')"""

                        if ((not (self.validFee(self.fee.get()))) or (self.fee.get() == "")):
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

    # ============================================================to set all field as null========================================================

    def setValue(self):
        self.rno = "-"
        self.std = "-"
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

    # ========================================================to get standard============================================================

    def getStd(self):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_getstd = """SELECT DISTINCT standard FROM master;"""

            cursor.execute(sqlite_getstd)
            # sqliteConnection.commit()
            # print("Python Variables deleted successfully from detail table")
            # messagebox.showinfo('Successfully done', 'Deletion is done in database')
            return cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    # ========================================================to get standard============================================================

    def getRoll(self, stds, ):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_getrno = """SELECT rollno FROM master WHERE standard = ?;"""
            data_tuple = (stds,)

            cursor.execute(sqlite_getrno, data_tuple)
            # sqliteConnection.commit()
            # print("Python Variables deleted successfully from detail table")
            # messagebox.showinfo('Successfully done', 'Deletion is done in database')
            return cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    # ========================================================to get current values============================================================

    def getRow(self, stds, rno):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_getrow = """SELECT * FROM master WHERE standard = ? AND rollno = ?;"""
            data_tuple = (stds, rno)

            cursor.execute(sqlite_getrow, data_tuple)
            # sqliteConnection.commit()
            # print("Python Variables deleted successfully from detail table")
            # messagebox.showinfo('Successfully done', 'Deletion is done in database')
            return cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("roll")
            print("Failed to delete Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    # ========================================================to get gr number============================================================

    def getGrn(self, stds, rno):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_getgr = """SELECT grno FROM master WHERE standard = ? AND rollno = ?;"""
            data_tuple = (stds, rno)

            cursor.execute(sqlite_getgr, data_tuple)
            # sqliteConnection.commit()
            # print("Python Variables deleted successfully from detail table")
            # messagebox.showinfo('Successfully done', 'Deletion is done in database')
            return cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("roll")
            print("Failed to delete Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    # ========================================================1st next============================================================

    def nextStep(self, event):

        if (self.stds.get() == "Select Standard"):

            messagebox.showinfo('Error', 'Please select standard')

        else:

            text = Label(text="Select Rollno : ")
            text.place(x=505, y=5, height=25)
            self.rnochoosen = Combobox(self, state="readonly", textvariable=self.rno)
            self.rnochoosen.place(x=700, y=5, height=25, width=200)
            self.rnochoosen['values'] = self.getRoll(self.stds.get(), )
            self.rnochoosen.bind("<<ComboboxSelected>>", self.nextStep2)
            # Create a Button
            """self.btn2 = Button(self, text='Next', bd='5', command=self.nextStep2)
            # Set the position of button on the top of window.
            self.btn2.place(x=100, y=550, height=25, width=150)"""

    # ========================================================2nd next============================================================

    def nextStep2(self, event):

        if (self.rnochoosen.get() == "Select Roll number"):

            messagebox.showinfo('Error', 'Please select roll number')

        else:
            self.row = self.getRow(self.stds.get(), self.rnochoosen.get())
            self.grno = (self.row[0][0])
            self.rollno = (self.row[0][1])
            self.std = (self.row[0][2])
            # self.div = (self.row[0][2].split("-")[1])
            self.fname.set(self.row[0][3])
            self.mname.set(self.row[0][4])
            self.lname.set(self.row[0][5])
            self.address = (self.row[0][6])
            self.phnos.set(self.row[0][7])
            self.phnop.set(self.row[0][8])
            self.email.set(self.row[0][9])
            self.poadd = (self.row[0][10])
            self.pophno.set(self.row[0][11])
            self.fee.set(self.row[0][12])
            print(self.row[0][0])

            text = Label(self,text="GRno")
            text.place(x=505, y=35, height=25)
            self.grnotext = Label(self,text=self.grno)
            self.grnotext.place(x=600, y=35, height=25)

            text = Label(self,text="Rollno")
            text.place(x=505, y=65, height=25)
            self.rollnotext = Label(self,text=self.rollno)
            self.rollnotext.place(x=600, y=65, height=25)

            text = Label(self,text="Std.")
            text.place(x=5, y=35, height=25)
            self.stdentry = Label(self,text=self.std)
            self.stdentry.place(x=100, y=35, height=25)
            self.stdentry.focus_set()

            """text = Label(self,text="Div.")
            text.place(x=5, y=65, height=25)
            self.diventry = Entry(self, textvariable=self.div)
            self.diventry.place(x=100, y=65, height=25, width=150)"""

            text = Label(self,text="First name")
            text.place(x=5, y=95, height=25)
            self.fnameentry = Entry(self, textvariable=self.fname)
            self.fnameentry.place(x=100, y=95, height=25, width=150)

            text = Label(self,text="Middle name")
            text.place(x=5, y=125, height=25)
            self.mnameentry = Entry(self, textvariable=self.mname)
            self.mnameentry.place(x=100, y=125, height=25, width=150)

            text = Label(self,text="Last name")
            text.place(x=5, y=155, height=25)
            self.lnameentry = Entry(self, textvariable=self.lname)
            self.lnameentry.place(x=100, y=155, height=25, width=150)

            text = Label(self,text="Address")
            text.place(x=5, y=185, height=25)
            self.addressentry = Text(self, width=20, height=5, padx=2, pady=2, wrap=WORD)
            self.addressentry.place(x=100, y=185, height=75, width=150)
            self.addressentry.insert(INSERT, self.address)

            text = Label(self,text="Student ph.")
            text.place(x=5, y=275, height=25)
            self.phnosentry = Entry(self, textvariable=self.phnos)
            self.phnosentry.place(x=100, y=275, height=25, width=150)

            text = Label(self,text="Parent ph.")
            text.place(x=5, y=305, height=25)
            self.phnopentry = Entry(self, textvariable=self.phnop)
            self.phnopentry.place(x=100, y=305, height=25, width=150)

            text = Label(self,text="Email id")
            text.place(x=5, y=335, height=25)
            self.emailentry = Entry(self, textvariable=self.email)
            self.emailentry.place(x=100, y=335, height=25, width=150)

            text = Label(self,text="Parent office add.")
            text.place(x=5, y=365, height=25)
            self.poaddentry = Text(self, width=20, height=5, padx=2, pady=2, wrap=WORD)
            self.poaddentry.place(x=100, y=365, height=75, width=150)
            self.poaddentry.insert(INSERT, self.poadd)

            text = Label(self,text="Parent office ph.")
            text.place(x=5, y=455, height=25)
            self.pophnoentry = Entry(self, textvariable=self.pophno)
            self.pophnoentry.place(x=100, y=455, height=25, width=150)

            text = Label(self,text="Fees")
            text.place(x=5, y=485, height=25)
            self.feesentry = Entry(self, textvariable=self.fee)
            self.feesentry.place(x=100, y=485, height=25, width=150)

            # Create a Button
            self.btn3 = Button(self, text='Update', bd='5', command=self.lastStep)
            # Set the position of button on the top of window.
            self.btn3.place(x=100, y=550, height=25, width=150)

    # ========================================================Last Step============================================================

    def lastStep(self):

        self.submitvalue()

        if (self.updater == 1):
            self.rnochoosen.destroy()
            self.grnotext.destroy()
            self.rollnotext.destroy()
            self.stdentry.destroy()
            self.fnameentry.destroy()
            self.mnameentry.destroy()
            self.lnameentry.destroy()
            self.addressentry.destroy()
            self.phnosentry.destroy()
            self.phnopentry.destroy()
            self.emailentry.destroy()
            self.poaddentry.destroy()
            self.pophnoentry.destroy()
            self.feesentry.destroy()
            self.btn3.destroy()
            self.start()

    # ========================================================Main============================================================

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
        bb.pack()

        self.start()

        text = Label(self,text="Select Standard : ")
        text.place(x=5, y=5, height=25)
        self.stdchoosen = Combobox(self, state="readonly", textvariable=self.stds)
        self.stdchoosen.place(x=200, y=5, height=25, width=200)

        self.stdchoosen['values'] = self.getStd()

        self.stdchoosen.bind("<<ComboboxSelected>>", self.nextStep)

        # Create a Button
        """self.btn = Button(self, text='Next', bd='5', command=self.nextStep)
        # Set the position of button on the top of window.
        self.btn.place(x=100, y=550, height=25, width=150)"""
        self.protocol("WM_DELETE_WINDOW", self.c_w)