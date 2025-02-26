from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('library1.db')
cur = con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add book")
        self.resizable(False,False)

        ################### Frames ####################

        # Top Frame
        self.topFrame = Frame(self,height=150,bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self,height=600,bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        # heading
        heading = Label(self.topFrame,text='  ADD BOOK  ',font='arial 22 bold',fg='#003f8a',bg='white')
        heading.place(x=250,y=60)

        ######################### Entries and Labels ########################

        # name
        self.lbl_name = Label(self.bottomFrame,text='Name :',font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name = Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,'Please enter a book name')
        self.ent_name.place(x=150,y=45)

        # author
        self.lbl_author = Label(self.bottomFrame,text='Author :',font='arial 15 bold',fg='white',bg='#fcc324')
        self.lbl_author.place(x=40,y=80)
        self.ent_author = Entry(self.bottomFrame, width=30,bd=4)
        self.ent_author.insert(0,'Please enter a author name')
        self.ent_author.place(x=150,y=85)

        # page
        self.lbl_page = Label(self.bottomFrame, text='page :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_page.place(x=40, y=120)
        self.ent_page = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_page.insert(0, 'Please enter page size')
        self.ent_page.place(x=150, y=125)

        # language
        self.lbl_language = Label(self.bottomFrame, text='Language :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_language.place(x=40, y=160)
        self.ent_language = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_language.insert(0, 'Please enter a Language')
        self.ent_language.place(x=150, y=165)

        # Button
        button = Button(self.bottomFrame,text='Add book',command=self.addBook)
        button.place(x=270,y=200)

    def addBook(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        page = self.ent_page.get()
        language = self.ent_language.get()

        if (name and author and page and language != ""):
            try:
                query = "INSERT INTO 'books' (book_name,book_author,book_page,book_language) VALUES(?,?,?,?)"
                cur.execute(query,(name,author,page,language))
                con.commit()
                messagebox.showinfo("Success","Successfully added to the database",icon='info')

            except:
                messagebox.showerror("Error","Cant add to the database",icon='warning')
        else:
            messagebox.showerror("Error","Fields cant be empty", icon='warning')