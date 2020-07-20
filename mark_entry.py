from tkinter import *
from tkinter import  messagebox
from tkinter.ttk import Combobox
import sqlite3
from PIL import Image, ImageTk
import json
import time

class Mark_Entry(Toplevel):

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

        self.cb1.config(state='disabled')
        query = "select data from exams"
        j_data = self.conn.execute(query).fetchone()
        data = json.loads(j_data[0])
        self.subject = data[self.cb1.get()]

        label = Label(self, text="Standard")
        label.place(x=20, y=420)

        self.standard_entry_var = StringVar()
        self.standard_entry = Entry(self,state="disabled", textvariable=self.standard_entry_var)
        self.standard_entry.place(x=220, y=420)

        get_std_from_table_name = str(self.subject[-1])
        self.get_std_list = get_std_from_table_name.split("_")

        self.standard_entry_var.set(self.get_std_list[1])

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
        self.combo_roll.set('Select')
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


    def reset(self):
        self.cb1.config(state="normal")
        self.cb1.config(state="readonly")

        for i in range(len(self.subject)-1):
            self.mark_ent[i].destroy()
            self.mark_label[i].destroy()

        self.confirm_btn.destroy()
        self.reset_btn.destroy()
        self.standard_entry.destroy()
        self.combo_roll.destroy()


    def rollno_maintain(self):

        # ==========Conting the current entries from result table==========
        query = "select count(*) from '{}' ".format(self.subject[-1])
        self.count = self.conn.execute(query).fetchone()
        # =========Get Roll Numbers from master Table====================
        query = "select rollno from master where standard = '{}'".format(self.get_std_list[1])
        self.remaining_roll = self.conn.execute(query).fetchall()
        self.roll_from_master = []
        for i in self.remaining_roll:
            self.roll_from_master.append(i[0])

        if self.count[0] == 0:
            self.combo_roll['values'] = self.roll_from_master

        else:

            query = "select rollno from '{}' where std = '{}'".format(self.subject[-1], self.get_std_list[1])

            self.inserted_roll = self.conn.execute(query).fetchall()
            self.roll_from_result = []
            for i in self.inserted_roll:
                self.roll_from_result.append(i[0])
            self.set_of_masterroll = set(self.roll_from_master)
            self.set_of_resultroll = set(self.roll_from_result)

            self.list_for_combo = list(self.set_of_masterroll.difference(self.set_of_resultroll))
            self.combo_roll['values'] = self.list_for_combo

    def set_mark(self):

        m = messagebox.askyesnocancel("School Software","Are you really want to Save the Changes?")

        if m == True:
            if self.combo_roll.get() != 'Select':
                pass
            else:
                messagebox.showerror("School Software", "Please Select Roll Number first.")
                self.combo_roll.focus_set()
                return

            for i in range(len(self.subject) - 1):

                try:
                    int(self.mark_ent[i].get())
                except:
                    messagebox.showerror("School Software",
                                         "For Subject '{}' Marks field Should be Positive Number and Not Null.".format(
                                             self.subject[i]))
                    self.mark_ent[i].focus_set()
                    return

                query = "select marks from exams"
                fetched_total = self.conn.execute(query).fetchone()
                j = json.loads(fetched_total[0])
                mark_list = j[self.cb1.get()]
                print(mark_list)
                if int(self.mark_ent[i].get()) > int(mark_list[i]):
                    messagebox.showerror("School Software",
                                         "For Subject '{}' Total Marks are '{}' and you Entered '{}'.\nIt's not Posiible to give marks more then Total.".format(
                                             self.subject[i], mark_list[i], self.mark_ent[i].get()))
                    self.mark_ent[i].focus_set()
                    return


                if self.mark_ent[i].get() == "" or int(self.mark_ent[i].get())<0:
                    messagebox.showerror("School Software","For Subject '{}' Marks field Should be Positive Number and Not Null.".format(self.subject[i]))
                    self.mark_ent[i].focus_set()
                    return




            self.insert_data_list = []
            self.insert_data_list.append(self.standard_entry_var.get())
            self.insert_data_list.append(self.combo_roll.get())
            self.add_query_formatting = "?"
            for i in range(len(self.subject)-1):
                self.insert_data_list.append(self.mark_ent[i].get())
                self.add_query_formatting += ",?"
            self.add_query_formatting += ",?"
            self.insert_data_tuple = tuple(self.insert_data_list)

            query = "insert into '{}' values ({})".format(self.subject[-1], self.add_query_formatting)
            self.conn.execute(query, self.insert_data_tuple)
            for i in range(len(self.subject)-1):
                self.var[i].set('')
            self.rollno_maintain()
            self.combo_roll.set('Select')
            for i in range(len(self.subject) - 1):
                self.var[i].set('')
            self.conn.commit()
            messagebox.showinfo("School Software", "Your Entry of Marks is Succesful!")

        elif m == False:

            self.reset()

        else:
            return


    def __init__(self, root, main_root):

        self.main_root = main_root
        self.root = root
        try:
            self.conn = sqlite3.connect('sinfo.db')
        except:
            messagebox.showerror("School", "Database Problem")
        self.date = time.strftime("%d_%m_%y")

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

        self.protocol("WM_DELETE_WINDOW", self.c_w)

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


        self.mainloop()
