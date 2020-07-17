from tkinter import *
import sqlite3
import time
import json
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk

class Exam(Toplevel):
    def done_sub(self):

        m = messagebox.askyesnocancel("School Software","Are you really want to Save the Changes?")
        if m == True:
            try:
                if self.combo_var_std_start.get() != "Select":
                    for i in range(len(self.subject_list)):
                        if i == 0:
                            query = "CREATE TABLE '{}_{}_{}' (std TEXT, rollno NUMERIC,{} NUMERIC NOT NULL );".format(
                                self.exam_entry.get(), self.combo_var_std_start.get(), self.date, self.subject_list[i])
                            self.conn.execute(query)
                        else:
                            query = "ALTER TABLE '{}_{}_{}' ADD {} NUMERIC;".format(self.exam_entry.get(),
                                                                                    self.combo_var_std_start.get(),
                                                                                    self.date, self.subject_list[i])
                            self.conn.execute(query)
                    self.conn.commit()

                    query = "select count(*) from exams"
                    rows = self.conn.execute(query).fetchone()

                    if rows[0] == 0:
                        mark_data = {}
                        data = {}
                        self.subject_list.append(
                            '{}_{}_{}'.format(self.exam_entry.get(), self.combo_var_std_start.get(), self.date))
                        data[self.exam_entry.get()] = self.subject_list
                        mark_data[self.exam_entry.get()] = self.mark_list
                        j_mark = json.dumps(mark_data)
                        j = json.dumps(data)
                        query = """insert into exams(data, marks) values(?,?)"""
                        self.conn.execute(query, (j, j_mark))
                        self.conn.commit()

                    else:

                        query = """select * from exams"""
                        j_fetch = self.conn.execute(query).fetchone()

                        fetched_data = json.loads(j_fetch[0])
                        fetched_mark = json.loads(j_fetch[1])
                        self.subject_list.append(
                            '{}_{}_{}'.format(self.exam_entry.get(), self.combo_var_std_start.get(), self.date))
                        fetched_data[self.exam_entry.get()] = self.subject_list
                        fetched_mark[self.exam_entry.get()] = self.mark_list
                        j = json.dumps(fetched_data)
                        j_mark = json.dumps(fetched_mark)
                        query = """update exams set data=(?), marks=(?)"""
                        self.conn.execute(query, (j, j_mark))
                        self.conn.commit()
                        self.reset()
                else:
                    raise AttributeError

            except:
                messagebox.showerror("School Software", "Please Select Standard First")
                self.cb3.focus_set()
                return

        elif m == False:

            self.reset()

        else:
            return

    def reset(self):
        self.combo_var_std_start.set("Select")
        self.exam_entry_var.set('')
        self.subject_list = []
        self.mark_list = []

    def add_sub_and_mark(self):
        mark = self.mark_entry.get()
        sub = self.subject_entry.get()
        self.subject_list.append(sub)
        self.mark_list.append(mark)
        self.sub_entry_var.set('')
        self.mark_entry_var.set('')

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event=""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def next(self, event=""):
        self.withdraw()
        # Exam(self, self.main_root)

    def __init__(self,root,main_root):
        self.root = root
        self.main_root = main_root
        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            messagebox.showerror("School","Database Problem")
        self.date = time.strftime("%d_%m_%y")
        self.subject_list = []
        self.mark_list = []
        Toplevel.__init__(self)

        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.f1 = "Arial Bold"
        self.f2 = "times new roman"
        self.title("WINDOW2")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.resizable(False, False)

        bgimg = ImageTk.PhotoImage(file="dark-blue-blur-gradation-wallpaper-preview.jpg")
        lbl = Label(self, image=bgimg)
        lbl.place(x=0, y=0, relwidth=1, relheight=1)


        label = Label(self, text="Enter Exam Name")
        label.place(x=20,y=20)
        label = Label(self, text="Enter Subjects for Exam")
        label.place(x=20,y=120)
        label = Label(self, text="Enter Marks for Exam")
        label.place(x=20, y=220)
        label = Label(self, text="Enter Standard")
        label.place(x=20, y=320)
        self.sub_entry_var = StringVar()
        self.mark_entry_var = StringVar()
        self.exam_entry_var = StringVar()
        self.exam_entry = Entry(self, textvariable=self.exam_entry_var)
        self.exam_entry.place(x=220,y=20)
        self.subject_entry = Entry(self, textvariable=self.sub_entry_var)
        self.subject_entry.place(x=220,y=120)
        self.mark_entry = Entry(self, textvariable=self.mark_entry_var)
        self.mark_entry.place(x=220, y=220)
        self.combo_var_std_start = StringVar()
        self.cb3 = Combobox(self, state="readonly", textvariable=self.combo_var_std_start, font=("Arial Bold", 15))
        self.cb3.place(x=220,y=420)
        self.cb3['values'] = ["L.K.G", "H.K.G", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "11~Commerce", "12~Commerce",
                              "11~Science", "12~Science"]
        self.cb3.set("Select")
        add_btn = Button(self, text="ADD", command=self.add_sub_and_mark)
        add_btn.place(x=20,y=320)
        done_btn = Button(self, text="DONE", command=self.done_sub)
        done_btn.place(x=120,y=320)
        self.protocol("WM_DELETE_WINDOW", self.c_w)

