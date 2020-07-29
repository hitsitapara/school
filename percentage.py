from tkinter import *
from tkinter import  messagebox
import sqlite3
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import json
from reportlab.pdfgen import canvas
import os
import webbrowser

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
    
    def get_data_for_preview_and_result(self):
        return_value = True
        query = "select data from exams"
        j_data = self.conn.execute(query).fetchone()
        self.data = json.loads(j_data[0])
        self.subject = self.data[self.cb1.get()]

        get_std_from_table_name = str(self.subject[-1])
        self.get_std_list = get_std_from_table_name.split("_")

        query = "select count(*) from master where standard = '{}'".format((self.get_std_list[1]))
        self.roll_from_master = self.conn.execute(query).fetchone()
        query = "select count(*) from '{}' where std = '{}'".format(self.subject[-1], (self.get_std_list[1]))
        self.roll_from_result = self.conn.execute(query).fetchone()

        if self.roll_from_master[0] == self.roll_from_result[0]:
            query = "select * from '{}' where std = '{}'".format(self.subject[-1], (self.get_std_list[1]))
            self.fetched_result = self.conn.execute(query).fetchall()
            self.get_mark = []

            query = "select marks from exams"
            fetched_total = self.conn.execute(query).fetchone()
            self.mark = json.loads(fetched_total[0])
            self.mark_list = self.mark[self.cb1.get()]
            self.total_exam_mark = 0
            for i in self.mark_list:
                self.total_exam_mark += int(i)
            query = "select * from '{}' order by rollno".format(self.subject[-1])
            self.all_details_marks = self.conn.execute(query).fetchall()
            query = "select * from master where standard = '{}' order by rollno".format((self.get_std_list[1]))
            self.all_details_student = self.conn.execute(query).fetchall()

            return_value = True
        else:
            messagebox.showerror("School Software",
                                 "Mark Entry of All Students for Exam '{}' is not Done.".format(self.cb1.get()))
            self.cb1.set("Select")
            return_value = False
        return return_value
        
    def selected_exam(self,event):
        get_return_value = self.get_data_for_preview_and_result()
        if not get_return_value:
            return
        self.preview_btn = Button(self, text="See Preview", command=self.preview)
        self.preview_btn.place(x=550, y=350, height=25)
        self.generate_btn = Button(self, text="Generate Result", command=self.generate_result)
        self.generate_btn.place(x=750, y=350, height=25)

    def preview(self):
        pdf = canvas.Canvas("C:\\Reports\\Exams\\preview_{}.pdf".format(self.cb1.get()))
        pdf.setPageSize((600, 930))
        pdf.line(10, 800, 590, 800)

        length_cols = len(self.all_details_marks)
        length_rows = len(self.all_details_marks[0])
        diff = int(550 / (length_rows - 1))

        pdf.setFont("Courier-Bold", 15)
        heading = self.cb1.get().split("_")

        pdf.drawString(215, 885, "Preview Report : {}".format(heading[0]))
        pdf.drawString(50, 870, "Standard : {}".format(heading[1]))
        pdf.drawString(430, 870, "Date : {}".format(heading[2]))

        side = 40
        top = 780
        pdf.setFont("Courier-Bold", 12)
        head_side = 30
        pdf.drawString(head_side, 820, "Roll")
        head_side += diff
        for i in range(len(self.subject) - 1):
            if i % 2 == 0:
                pdf.drawString(head_side, 825, self.subject[i])
            else:
                pdf.drawString((head_side + 10), 820, "Int.")
            pdf.drawString((side + diff), 805, '({})'.format(self.mark_list[i]))
            side += diff
            head_side += diff
        pdf.setFont("Courier-Bold", 12)
        side = 50
        for i in range(length_cols):
            for j in range(1, length_rows):
                pdf.drawString(side, top, str(self.all_details_marks[i][j]))
                side += diff
            top -= 10
            side = 50

        pdf.save()
        messagebox.showinfo("School Software",
                            "Your Preview for Exam '{}' is Generated Succesfully !\n".format(self.cb1.get()))
        webbrowser.open("C:\\Reports\\Exams\\report_{}.pdf".format(self.cb1.get()))
    def generate_result(self):
        m = messagebox.askyesnocancel("School Software", "Before Generating Result Please Ensure that you have Entered Correct Marks for all Students, After Generating Result you can't Update Marks.\nFor Mark Details Please See Preview.\nAre You really Want to Generate Result of Exam : '{}' ?".format(self.cb1.get()))
        if m == True:
            os.makedirs("C:\\Results\\{}".format(self.cb1.get()))
            get_return_value = self.get_data_for_preview_and_result()
            if get_return_value:
                percentage = []
                obtained = []
                self.got = 0
                query = "alter table '{}' add percentage NUMERIC;".format(self.subject[-1])
                self.conn.execute(query)
                self.conn.commit()

                for i in self.fetched_result:
                    for j in range(2,len(i)):
                        self.got += i[j]
                    per = float((self.got*100)/self.total_exam_mark)
                    percentage.append(per)
                    obtained.append(self.got)
                    query = "update '{}' set percentage={} where rollno = {}".format(self.subject[-1], per, i[1])
                    self.conn.execute(query)
                    self.got = 0
                    self.conn.commit()
                query = "select percentage from '{}' order by percentage desc".format(self.subject[-1])
                self.fetched_percentage = self.conn.execute(query).fetchall()
                self.set_percentage = set()
                for i in self.fetched_percentage:
                    self.set_percentage.add(i[0])

                self.collect_data()
                self.result_pdf()
                self.report_pdf()
                del self.data[self.cb1.get()]
                del self.mark[self.cb1.get()]

                j_mark = json.dumps(self.mark)
                j_data = json.dumps(self.data)
                query = """update exams set data=(?), marks=(?)"""
                self.conn.execute(query, (j_data, j_mark))
                self.conn.commit()

                query = "drop table '{}'".format(self.subject[-1])
                self.conn.execute(query)
                self.conn.commit()
                self.combo_maintain()
                messagebox.showinfo("School Software","Your Result for Exam '{}' is Generated Succesfully !".format(self.cb1.get()))
                self.preview_btn.destroy()
                self.generate_btn.destroy()
                self.cb1.set("Select")
            else:
                return
        elif m == False:
            self.combo_var.set('Select')
            self.preview_btn.destroy()
            self.generate_btn.destroy()
            return
        else:
            return

    def collect_data(self):
        query = "select * from '{}' order by rollno".format(self.subject[-1])
        self.all_details_marks = self.conn.execute(query).fetchall()
        query = "select * from master where standard = '{}' order by rollno".format((self.get_std_list[1]))
        self.all_details_student = self.conn.execute(query).fetchall()
        self.rankers = set()
        for i in self.all_details_marks:
            self.rankers.add(i[-1])
        self.ranks = []
        for i in self.rankers:
            self.ranks.append(i)
        self.ranks.sort()
        self.ranks.reverse()
        self.rank_list = []
        for i in range(1):
            self.rank_list.append(self.ranks[i])
    def combo_maintain(self):
        query = "select data from exams"
        j_data = self.conn.execute(query).fetchone()
        data = json.loads(j_data[0])
        exams = data.keys()
        k = []
        for i in exams:
            k.append(i)
        self.cb1['values'] = k

    def report_pdf(self):
        pdf = canvas.Canvas("C:\\Reports\\Exams\\{}.pdf".format(self.cb1.get()))
        pdf.setPageSize((600, 930))
        pdf.line(10, 800, 590, 800)

        length_cols = len(self.all_details_marks)
        length_rows = len(self.all_details_marks[0])
        diff = int(550/(length_rows-1))

        pdf.setFont("Courier-Bold", 15)
        heading = self.cb1.get().split("_")

        pdf.drawString(215, 885, "Exam Report : {}".format(heading[0]))
        pdf.drawString(50, 870, "Standard : {}".format(heading[1]))
        pdf.drawString(430, 870, "Date : {}".format(heading[2]))

        side = 40
        top = 780
        pdf.setFont("Courier-Bold", 12)
        head_side = 30
        pdf.drawString(head_side,820,"Roll")
        head_side += diff
        for i in range(len(self.subject)-1):
            if i%2 ==0:
                pdf.drawString(head_side,825,self.subject[i])
            else:
                pdf.drawString((head_side+10),820,"Int.")
            pdf.drawString((side+diff),805,'({})'.format(self.mark_list[i]))
            side += diff
            head_side += diff
        pdf.drawString(head_side, 825, "Percentage")
        pdf.setFont("Courier-Bold", 12)
        side = 50
        for i in range(length_cols):
            for j in range(1, length_rows):
                pdf.drawString(side, top, str(self.all_details_marks[i][j]))
                side += diff
            top -= 10
            side = 50
        pdf.save()
    def result_pdf(self):
        for i in self.all_details_student:

            pdf = canvas.Canvas("C:\\Results\\{}\\result_{}_{}.pdf".format(self.cb1.get(),i[2],i[1]))
            pdf.setFillColor('#F9F280')
            pdf.setPageSize((600, 900))
            pdf.rect(0, 0, 600, 900, fill=1)
            pdf.setFillColor('#4D722E')

            pdf.line(10, 600, 10, 200)
            pdf.line(580, 600, 580, 200)
            pdf.line(10, 200, 580, 200)

            pdf.line(10, 570, 580, 570)
            pdf.line(10, 600, 580, 600)
            pdf.line(50, 600, 50, 200)
            pdf.line(530, 600, 530, 200)
            pdf.line(480, 600, 480, 200)
            pdf.line(430, 600, 430, 200)
            pdf.line(380, 600, 380, 200)
            pdf.line(330, 600, 330, 200)
            pdf.line(280, 600, 280, 200)

            pdf.line(10, 725, 10, 825)
            pdf.line(150, 725, 150, 825)
            pdf.line(10, 725, 150, 725)
            pdf.line(10, 825, 150, 825)

            logo = 'logo.jpg'
            pdf.drawInlineImage(logo, 30, 725)

            pdf.setFont("Courier-Bold", 30)
            pdf.drawString(225, 800, "SCHOOL NAME")

            pdf.setFont("Courier-Bold", 25)
            pdf.drawString(250, 750, "EXAM NAME")

            pdf.setFont("Courier-Bold", 10)
            pdf.drawString(15, 580, "Sr No.")
            pdf.drawString(130, 580, "Subjects")
            pdf.drawString(289, 587, " Exam")
            pdf.drawString(286, 577, "(Total)")
            pdf.drawString(335, 587, " Exam")
            pdf.drawString(330, 577, " (obt.)")
            pdf.drawString(381, 587, "Internal")
            pdf.drawString(381, 577, " (Total)")
            pdf.drawString(431, 587, "Internal")
            pdf.drawString(431, 577, " (obt.)")
            pdf.drawString(488, 587, "TOTAL")
            pdf.drawString(488, 577, "MARKS")
            pdf.drawString(531, 587, "OBTAINED")
            pdf.drawString(538, 577, "MARKS")

            pdf.setFont("Courier-Bold", 12)

            pdf.line(10, 700, 580, 700)
            pdf.line(10, 620, 580, 620)
            pdf.line(20, 610, 20, 710)
            pdf.line(570, 610, 570, 710)

            pdf.line(10, 120, 580, 120)
            pdf.line(10, 170, 580, 170)
            pdf.line(20, 110, 20, 180)
            pdf.line(570, 110, 570, 180)

            pdf.line(460, 40, 580, 40)
            pdf.drawString(450, 20, "Principal Signature")

            #===========================================

            pdf.drawString(60, 680, "Student Name : {}".format(str(i[3])))
            pdf.drawString(60, 665, "Standard : {}".format(str(i[2])))
            pdf.drawString(60, 650, "Gr. No. : {}".format(str(i[0])))
            pdf.drawString(60, 635, "Roll No. : {}".format(str(i[1])))

            result = True
            #=========Fetching Marks==================================

            top = 500
            sr = 1
            for j in range(0,len(self.subject)-1,2):
                pdf.drawString(130,top,str(self.subject[j]))
                pdf.drawString(30, top,str(sr))
                sr += 1
                top -= 25
            top_e_m = 500
            top_i_m = 500
            subject_total = []

            #this is mark calculation counter for subject total
            x = 0
            for j in range(len(self.mark_list)):
                if j%2 ==0 :
                    pdf.drawString(293, top_e_m, str(self.mark_list[j]))
                    top_e_m -= 25
                    x += int(self.mark_list[j])
                else:
                    pdf.drawString(389, top_i_m, str(self.mark_list[j]))
                    top_i_m -= 25
                    x += int(self.mark_list[j])
                    subject_total.append(x)
                    x=0

            query = "select * from '{}' where rollno = {}".format(self.subject[-1], i[1])
            mark_detail = self.conn.execute(query).fetchone()

            # this is mark calculation counter for obtained
            x = 0
            subject_obtained = []
            top_e_m = 500
            top_i_m = 500
            for j in range(2,len(mark_detail)-1):
                if j%2 == 0:
                    pdf.drawString(343, top_e_m, str(mark_detail[j]))
                    top_e_m -= 25
                    x += int(mark_detail[j])
                    if float(mark_detail[j]) < float((int(self.mark_list[j-2])*33)/100):
                        result = False
                else:
                    pdf.drawString(443, top_i_m, str(mark_detail[j]))
                    top_i_m -= 25
                    x += int(mark_detail[j])
                    subject_obtained.append(x)
                    x = 0

                    if float(mark_detail[j]) < float((int(self.mark_list[j-2])*33)/100):
                        result = False
            top = 500
            for j in range(len(subject_obtained)):
                pdf.drawString(490, top, str(subject_total[j]))
                pdf.drawString(540, top, str(subject_obtained[j]))
                top -= 25

            sum = 0
            for j in range(len(subject_obtained)):
                sum += subject_obtained[j]

            pdf.drawString(60, 125, "TOTAL : {}  / {}".format(sum, self.total_exam_mark))
            query = "select percentage from '{}' where rollno = {}".format(self.subject[-1], i[1])
            per = self.conn.execute(query).fetchone()
            pdf.drawString(60, 155, "Percentage : {}".format(round(float(per[0]),2)))
            if result:
                pdf.drawString(450, 155, "Result : PASS")
            else:
                pdf.drawString(450, 155, "Result : FAIL")

            try:
                rank = self.rank_list.index(per[0])
                pdf.drawString(60, 140, "Rank : {}".format(str(rank + 1)))

            except:
                pdf.drawString(60, 140, "Rank : NA")
            #===========================================
            pdf.save()



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
