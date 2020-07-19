from tkinter import *
from tkinter import  messagebox
import sqlite3
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import json

class Percentage(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def selected_exam(self,event):
        query = "select data from exams"
        j_data = self.conn.execute(query).fetchone()
        data = json.loads(j_data[0])
        self.subject = data[self.cb1.get()]

        get_std_from_table_name = str(self.subject[-1])
        self.get_std_list = get_std_from_table_name.split("_")

        query = "select count(*) from master where standard = {}".format(self.get_std_list[1])
        self.roll_from_master = self.conn.execute(query).fetchone()
        query = "select count(*) from {} where std = {}".format(self.subject[-1],self.get_std_list[1])
        self.roll_from_result = self.conn.execute(query).fetchone()

        if self.roll_from_master[0] == self.roll_from_result[0]:
            query = "select * from {} where std = {}".format(self.subject[-1],self.get_std_list[1])
            fetched_result = self.conn.execute(query).fetchall()
            self.get_mark = []
            print(fetched_result)

            query = "select marks from exams"
            fetched_total = self.conn.execute(query).fetchone()
            j = json.loads(fetched_total[0])
            mark_list = j[self.cb1.get()]
            print(mark_list)
            total_exam_mark = 0
            for i in mark_list:
                total_exam_mark += int(i)
            print(total_exam_mark)
            percentage = []
            obtained = []
            got = 0

            query = "alter table '{}' add percentage NUMERIC;".format(self.subject[-1])
            self.conn.execute(query)
            self.conn.commit()

            for i in fetched_result:
                for j in range(2,len(i)):
                    got += i[j]
                per = float((got*100)/total_exam_mark)
                percentage.append(per)
                obtained.append(got)
                query = "update '{}' set percentage={} where rollno = {}".format(self.subject[-1], per, i[1])
                print(query)
                self.conn.execute(query)
                got = 0
                self.conn.commit()

            messagebox.showinfo("School Software","Your Percentage for Exam '{}' is Calculated Succesfully.".format(self.cb1.get()))
        else:
            messagebox.showerror("School Software", "Mark Entry of All Students for Exam '{}' is not Done.".format(self.cb1.get()))


    def __init__(self, root, main_root):

        self.main_root = main_root
        self.root = root
        Toplevel.__init__(self)
        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            messagebox.showerror("School", "Database Problem")
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

        self.combo_var = StringVar()
        self.cb1 = Combobox(self, state="readonly", textvariable=self.combo_var, font=("Arial Bold", 15))
        self.cb1.pack()
        query = "select data from exams"
        j_data = self.conn.execute(query).fetchone()
        data = json.loads(j_data[0])
        exams = data.keys()
        k = []
        for i in exams:
            k.append(i)
        self.cb1['values'] = k
        self.cb1.bind("<<ComboboxSelected>>", self.selected_exam)
        self.cb1.set("Select")


        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
