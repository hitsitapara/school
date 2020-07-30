from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
import sqlite3
from PIL import Image, ImageTk


class RemoveStudent(Toplevel):

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

    # ========================================================to delete record============================================================

    def deleteFromTable(self, grno):
        try:
            sqliteConnection = sqlite3.connect('sinfo.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_delete = """DELETE FROM master WHERE grno=?;"""

            data_tuple = (grno)
            cursor.execute(sqlite_delete, data_tuple)
            sqliteConnection.commit()
            print("Python Variables deleted successfully from detail table")
            messagebox.showinfo('Successfully done', 'Deletion is done in database')
            cursor.close()

        except sqlite3.Error as error:
            print("delete")
            print("Failed to delete Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def start(self):
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

    # ========================================================to get gr number============================================================

    """def setValue(self):

        self.stds.set("Select Standard")
        self.rno.set("Select Roll number")
        self.grno.set("-")
        self.rollno.set("-")
        self.std.set("-")
        self.fname.set("-")
        self.mname.set("-")
        self.lname.set("-")
        self.address.set("-")
        self.phnos.set("-")
        self.phnop.set("-")
        self.email.set("-")
        self.poadd.set("-")
        self.pophno.set("-")
        self.fee.set("-")"""

    # ========================================================1st next============================================================

    def nextStep(self, event):

        if (self.stds.get() == "Select Standard"):

            messagebox.showinfo('Error', 'Please select standard')

        else:

            text = Label(self,text="Select Rollno : ")
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

        if (self.rno.get() == "Select Roll number"):

            messagebox.showinfo('Error', 'Please select roll number')

        else:
            self.row = self.getRow(self.stds.get(), self.rno.get())
            self.grno = (self.row[0][0])
            self.rollno = (self.row[0][1])
            self.std = (self.row[0][2])
            # self.div = (self.row[0][2].split("-")[1])
            self.fname = (self.row[0][3])
            self.mname = (self.row[0][4])
            self.lname = (self.row[0][5])
            self.address = (self.row[0][6])
            self.phnos = (self.row[0][7])
            self.phnop = (self.row[0][8])
            self.email = (self.row[0][9])
            self.poadd = (self.row[0][10])
            self.pophno = (self.row[0][11])
            self.fee = (self.row[0][12])
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
            self.stdtext = Label(self,text=self.std)
            self.stdtext.place(x=100, y=35, height=25)

            """text = Label(self,text="Div.")
            text.place(x=5, y=65, height=25)
            self.divtext = Label(self,text=self.div)
            self.divtext.place(x=100, y=65, height=25)"""

            text = Label(self,text="First name")
            text.place(x=5, y=95, height=25)
            self.fnametext = Label(self,text=self.fname)
            self.fnametext.place(x=100, y=95, height=25)

            text = Label(self,text="Middle name")
            text.place(x=5, y=125, height=25)
            self.mnametext = Label(self,text=self.mname)
            self.mnametext.place(x=100, y=125, height=25)

            text = Label(self,text="Last name")
            text.place(x=5, y=155, height=25)
            self.lnametext = Label(self,text=self.lname)
            self.lnametext.place(x=100, y=155, height=25)

            text = Label(self,text="Address")
            text.place(x=5, y=185, height=25)
            self.addresstext = Label(self,text=self.address)
            self.addresstext.place(x=100, y=185, height=75)

            text = Label(self,text="Phnos.")
            text.place(x=5, y=275, height=25)
            self.phnostext = Label(self,text=self.phnos)
            self.phnostext.place(x=100, y=275, height=25)

            text = Label(self,text="Phnop.")
            text.place(x=5, y=305, height=25)
            self.phnoptext = Label(self,text=self.phnop)
            self.phnoptext.place(x=100, y=305, height=25)

            text = Label(self,text="Email id")
            text.place(x=5, y=335, height=25)
            self.emailtext = Label(self,text=self.email)
            self.emailtext.place(x=100, y=335, height=25)

            text = Label(self,text="Poadd")
            text.place(x=5, y=365, height=25)
            self.poaddtext = Label(self,text=self.poadd)
            self.poaddtext.place(x=100, y=365, height=75)

            text = Label(self,text="Pophno")
            text.place(x=5, y=455, height=25)
            self.pophnotext = Label(self,text=self.pophno)
            self.pophnotext.place(x=100, y=455, height=25)

            text = Label(self,text="Fees")
            text.place(x=5, y=485, height=25)
            self.feetext = Label(self,text=self.fee)
            self.feetext.place(x=100, y=485, height=25)

            # Create a Button
            self.btn3 = Button(self, text='Delete', bd='5', command=self.lastStep)
            # Set the position of button on the top of window.
            self.btn3.place(x=100, y=550, height=25, width=150)

    # ========================================================Last Step============================================================

    def lastStep(self):
        self.grn = self.getGrn(self.stds.get(), self.rno.get())
        self.deleteFromTable(self.grn[0])
        self.rnochoosen.destroy()
        self.grnotext.destroy()
        self.rollnotext.destroy()
        self.stdtext.destroy()
        self.fnametext.destroy()
        self.mnametext.destroy()
        self.lnametext.destroy()
        self.addresstext.destroy()
        self.phnostext.destroy()
        self.phnoptext.destroy()
        self.emailtext.destroy()
        self.poaddtext.destroy()
        self.pophnotext.destroy()
        self.feetext.destroy()
        self.btn3.destroy()
        self.start()

    # ========================================================Main============================================================

    def __init__(self,root ,main_root):
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
        self.protocol("WM_DELETE_WINDOW", self.c_w)
