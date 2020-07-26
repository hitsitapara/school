from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk


class ChangePassword(Toplevel):

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

    def change_method(self):
        if self.new_password_entry.get() == self.re_password_entry.get():
            query = "update staff set password= '"+str(self.new_password_entry.get())+"' where currentuser=1"
            self.conn.execute(query)
            self.conn.commit()
            messagebox.showinfo("School Software","Password updated successfully")
            self.destroy()
            self.root.deiconify()

        else:
            messagebox.showerror("School Software","Password and re-password are not matching,enter same password in both entry")
            self.new_password_var.set("")
            self.re_password_var.set("")
            return

    def cancel_method(self):
        answer = messagebox.askyesno("School Software","Are you sure to exit the screen")
        if answer>0:
            self.destroy()
            self.root.deiconify()

        else:
            return

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

        self.fr = LabelFrame(self,text="Change Password",font=150)
        self.new_password = Label(self.fr,text="New Password",font=70)
        self.new_password_var = StringVar()
        self.new_password_entry=Entry(self.fr,textvariable=self.new_password_var,font=70,show='*')
        self.new_password.place(x=275,y=100)
        self.new_password_entry.place(x=770,y=100)

        self.re_password =Label(self.fr,text="Re-type new password",font=70)
        self.re_password_var = StringVar()
        self.re_password_entry =Entry(self.fr,textvariable=self.re_password_var,font=70,show='*')
        self.re_password.place(x=275,y=200)
        self.re_password_entry.place(x=770,y=200)


        self.change_button = Button(self.fr,text="Change",font=70,command=self.change_method)
        self.cancel_button = Button(self.fr,text="cancel",font=70,command=self.cancel_method)

        self.change_button.place(x=475, y=400)
        self.cancel_button.place(x=625, y=400)

        self.fr.place(x=0, y=200, relwidth=1, relheight=1)

        imagel = Image.open("left-arrow.png")
        imagel = imagel.resize((50, 50))
        imgl = ImageTk.PhotoImage(imagel)



        self.protocol("WM_DELETE_WINDOW", self.c_w)


