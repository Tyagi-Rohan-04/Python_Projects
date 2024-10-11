from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('library1.db')
cur = con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Member")
        self.resizable(False,False)

        ################### Frames ####################

        # Top Frame
        self.topFrame = Frame(self,height=150,bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self,height=600,bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        # heading
        heading = Label(self.topFrame,text='  ADD PERSON  ',font='arial 22 bold',fg='#003f8a',bg='white')
        heading.place(x=250,y=60)

        ######################### Entries and Labels ########################

        # name
        self.lbl_name = Label(self.bottomFrame,text='Name :',font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name = Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,'Please enter a book name')
        self.ent_name.place(x=150,y=45)

        # phone number
        self.lbl_phone = Label(self.bottomFrame,text='Phone :',font='arial 15 bold',fg='white',bg='#fcc324')
        self.lbl_phone.place(x=40,y=80)
        self.ent_phone = Entry(self.bottomFrame, width=30,bd=4)
        self.ent_phone.insert(0,'Please enter Phone Number')
        self.ent_phone.place(x=150,y=85)

        # Button
        button = Button(self.bottomFrame,text='Add Member',command=self.addMember)
        button.place(x=270,y=200)

    def addMember(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()

        if (name and phone != ""):
            try:
                query = "INSERT INTO 'members' (member_name,member_phone) VALUES(?,?)"
                cur.execute(query,(name,phone))
                con.commit()
                messagebox.showinfo("Success","Successfully added to the database",icon='info')

            except:
                messagebox.showerror("Error","Cant add to the database",icon='warning')
        else:
            messagebox.showerror("Error","Fields cant be empty", icon='warning')