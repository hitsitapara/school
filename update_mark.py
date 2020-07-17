from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import json

class Update_Mark(Toplevel):

    def backf(self, event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self, event = ""):
        m = messagebox.askyesno("School Software", "Are you Want to Close Application?", parent=self.root)
        if m > 0:
            self.main_root.destroy()
        else:
            return

    def set_mark(self):

        m = messagebox.askyesnocancel("School Software","Are you really want to Save the Changes?")

        if m == True:

            self.insert_data_list = []
            self.insert_data_list.append(self.standard_entry_var.get())
            self.insert_data_list.append(self.combo_roll.get())
            self.add_query_formatting = "?"
            for i in range(len(self.subject)-1):
                self.insert_data_list.append(self.mark_ent[i].get())
                self.add_query_formatting += ",?"
            self.add_query_formatting += ",?"
            self.insert_data_tuple = tuple(self.insert_data_list)

            query = "delete from '{}' where std='{}' and rollno = '{}' ".format(self.subject[-1],self.get_std_list[1],self.combo_roll.get())
            print(query)
            self.conn.execute(query)

            query = "insert into '{}' values ({})".format(self.subject[-1], self.add_query_formatting)
            print(query)
            print(self.insert_data_tuple)
            self.conn.execute(query, self.insert_data_tuple)
            for i in range(len(self.subject)-1):
                self.var[i].set('')
            self.rollno_maintain()
            self.combo_roll.set('Select')
            self.conn.commit()

        elif m == False:

            self.reset()

        else:
            return

    def reset(self):
        self.combo_get_exam.config(state="normal")

        for i in range(len(self.subject)-1):
            self.mark_ent[i].destroy()
            self.mark_label[i].destroy()
        self.confirm_btn.destroy()
        self.reset_btn.destroy()
        self.standard_label.destroy()
        self.standard_entry.destroy()

    def get_exam_details(self,event):

        self.combo_get_exam.config(state='disabled')
        query = "select data from exams"
        j_data = self.conn.execute(query).fetchone()
        data = json.loads(j_data[0])
        self.subject = data[self.combo_get_exam_var.get()]

        self.standard_label = Label(self, text="Standard")
        self.standard_label.place(x=20, y=620)

        self.standard_entry_var = StringVar()
        self.standard_entry = Entry(self,state="disabled", textvariable=self.standard_entry_var)
        self.standard_entry.place(x=220, y=620)

        get_std_from_table_name = str(self.subject[-1])
        self.get_std_list = get_std_from_table_name.split("_")

        self.standard_entry_var.set(self.get_std_list[1])
        print(self.standard_entry_var.get())

        self.var = []
        self.mark_ent = []
        self.mark_label = []
        for i in range(len(self.subject)-1):
            self.var.append(str(i))
            self.mark_ent.append(str(i))
            self.mark_label.append(str(i))
        self.roll_var = StringVar()
        self.combo_roll = Combobox(self, state="readonly", textvariable=self.roll_var, font=("Arial Bold", 15))
        self.combo_roll.pack()
        self.combo_roll.bind("<<ComboboxSelected>>", self.set_exist_values)
        self.rollno_maintain()
        for i in range(len(self.subject)-1):
            self.var[i] = StringVar()
            self.mark_label[i] = Label(self,text=self.subject[i])
            self.mark_label[i].pack()
            self.mark_ent[i] = Entry(self, textvariable=self.var[i])
            self.mark_ent[i].pack()
        self.confirm_btn= Button(self,text="Confirm",command=self.set_mark)
        self.confirm_btn.pack()
        self.reset_btn = Button(self, text="Reset", command=self.reset)
        self.reset_btn.pack()

    def set_exist_values(self,event):

        query = "select * from '{}' where std = '{}' and rollno = '{}'".format(self.subject[-1],self.get_std_list[1],self.combo_roll.get())
        print(query)
        self.fetch_value = self.conn.execute(query).fetchall()
        print(len(self.fetch_value[0]))
        for i in range(2,len(self.fetch_value[0])):
            self.var[i-2].set(self.fetch_value[0][i])

    def rollno_maintain(self):
        query = "select rollno from '{}'".format(self.subject[-1])
        self.count= self.conn.execute(query).fetchone()
        if self.count[0] == 0:
            self.combo_roll['values'] = []
        else:

            query = "select rollno from '{}'".format(self.subject[-1])
            self.inserted_roll = self.conn.execute(query).fetchall()
            self.roll_from_result = []
            for i in self.inserted_roll:
                self.roll_from_result.append(i[0])

            self.combo_roll['values'] = self.roll_from_result


    def __init__(self, root, main_root):

        self.main_root = main_root
        self.root = root
        Toplevel.__init__(self)
        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            messagebox.showerror("School Software", "Database Problem")
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

        self.combo_get_exam_var = StringVar()
        self.combo_get_exam = Combobox(self, state="readonly", textvariable=self.combo_get_exam_var,
                                       font=("Arial Bold", 15))
        self.combo_get_exam.place(x=220, y=420)
        query = "select data from exams"
        j_data = self.conn.execute(query).fetchone()
        data = json.loads(j_data[0])
        exams = data.keys()
        k = []
        for i in exams:
            k.append(i)
        self.combo_get_exam['values'] = k
        self.combo_get_exam.set("Select")
        self.combo_get_exam.bind("<<ComboboxSelected>>", self.get_exam_details)



        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
