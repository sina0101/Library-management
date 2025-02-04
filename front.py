import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import back

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x350')
        self.root.title('Library Management')
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Top Frame
        self.frametop = Frame(self.root)
        self.frametop.pack()

        # Entry Frame
        self.Entryframe = Frame(self.frametop)
        self.Entryframe.pack(side=LEFT, padx=30)

        # Button Frame
        self.Buttonframe = Frame(self.frametop, width=80, height=0)
        self.Buttonframe.pack(side=RIGHT)

        # Buttons
        self.btn_show_all = ttk.Button(self.Buttonframe, text='Show All', command=self.show_all_pressed)
        self.btn_show_all.pack(pady=10, padx=10)

        self.btn_new = ttk.Button(self.Buttonframe, text='New', command=self.insert_pressed)
        self.btn_new.pack(pady=10, padx=10)

        self.btn_edit = ttk.Button(self.Buttonframe, text='Edit', command=self.def_edit)
        self.btn_edit.pack(pady=10, padx=10)

        self.btn_delete = ttk.Button(self.Buttonframe, text='Delete', command=self.def_delete)
        self.btn_delete.pack(pady=10, padx=10)

        self.btn_exit = ttk.Button(self.Buttonframe, text='Exit', command=self.btn_exit_pressed)
        self.btn_exit.pack(pady=10, padx=10)

        # Entry Fields
        self.lb_book_title = Label(self.Entryframe, text='Book title:')
        self.lb_book_title.grid(row=0, column=0, pady=9)

        self.ent_book_title = ttk.Entry(self.Entryframe)
        self.ent_book_title.grid(row=0, column=1, pady=9)

        self.lb_author = Label(self.Entryframe, text='Author:')
        self.lb_author.grid(row=1, column=0, pady=9)

        self.ent_author = ttk.Entry(self.Entryframe)
        self.ent_author.grid(row=1, column=1, pady=9)

        self.lb_publish_year = Label(self.Entryframe, text='Publish year:')
        self.lb_publish_year.grid(row=2, column=0, pady=9)

        self.ent_publish_year = ttk.Entry(self.Entryframe)
        self.ent_publish_year.grid(row=2, column=1, pady=9)

        self.lb_subject = Label(self.Entryframe, text='Subject:')
        self.lb_subject.grid(row=3, column=0, pady=9)

        self.ent_subject = ttk.Entry(self.Entryframe)
        self.ent_subject.grid(row=3, column=1, pady=9)

        # Search Frame
        self.searchframe = Frame(self.root)
        self.searchframe.pack(side=BOTTOM)

        self.p = StringVar()
        self.radio_title = ttk.Radiobutton(self.searchframe, text='Title', variable=self.p, value='title')
        self.radio_title.pack(side='left', anchor=W, padx=6)

        self.radio_author = ttk.Radiobutton(self.searchframe, text='Author', variable=self.p, value='author')
        self.radio_author.pack(side='left', anchor=W, padx=6)

        self.radio_year = ttk.Radiobutton(self.searchframe, text='Year', variable=self.p, value='year')
        self.radio_year.pack(side='left', anchor=W, padx=6)

        self.radio_subject = ttk.Radiobutton(self.searchframe, text='Subject', variable=self.p, value='subject')
        self.radio_subject.pack(side='left', anchor=W, padx=6)

        self.ent_search_book = ttk.Entry(self.searchframe, width=30)
        self.ent_search_book.pack(side='right')

        self.btn_search = ttk.Button(self.searchframe, text='Search', command=self.def_search_pressed)
        self.btn_search.pack(side='right', padx=10, pady=10)

    def show_all_pressed(self):
        top_show_all = Toplevel(self.root)
        top_show_all.title('***help: ( id , title , author , year , subject )***')
        top_show_all.geometry('500x400')

        rows = back.show_all()
        list_box1 = Listbox(top_show_all, height=400, width=400)
        list_box1.pack()

        if len(rows) == 0:
            messagebox.showerror('No Data!')
        else:
            for row in rows:
                list_box1.insert(END, row)

    def insert_pressed(self):
        title = self.ent_book_title.get()
        author = self.ent_author.get()
        year = self.ent_publish_year.get()
        subject = self.ent_subject.get()

        self.ent_book_title.delete(0, END)
        self.ent_author.delete(0, END)
        self.ent_publish_year.delete(0, END)
        self.ent_subject.delete(0, END)

        back.insert(title, author, year, subject)

    def def_edit(self):
        edit_win = Toplevel(self.root)
        edit_win.geometry('500x500')

        lab_id = Label(edit_win, text='ID')
        lab_id.pack()

        ent_id = ttk.Entry(edit_win)
        ent_id.pack()

        lab_title = Label(edit_win, text='Please select!')
        lab_title.pack()

        p = StringVar()
        radio_title = ttk.Radiobutton(edit_win, text='Title', variable=p, value='title')
        radio_title.pack(padx=(225, 0), anchor=W)

        radio_author = ttk.Radiobutton(edit_win, text='Author', variable=p, value='author')
        radio_author.pack(padx=(225, 0), anchor=W)

        radio_year = ttk.Radiobutton(edit_win, text='Year', variable=p, value='year')
        radio_year.pack(padx=(225, 0), anchor=W)

        radio_subject = ttk.Radiobutton(edit_win, text='Subject', variable=p, value='subject')
        radio_subject.pack(padx=(225, 0), anchor=W)

        lab_change_to = Label(edit_win, text='Change to')
        lab_change_to.pack()

        ent_new_value = ttk.Entry(edit_win)
        ent_new_value.pack()

        def btn_sub_pressed():
            id = ent_id.get()
            sell = p.get()
            new_value = ent_new_value.get()
            back.edit(id, sell, new_value)
            edit_win.destroy()

        btn_submit_edit = ttk.Button(edit_win, text='Submit', command=btn_sub_pressed)
        btn_submit_edit.pack(pady=20)

    def def_delete(self):
        delete_win = Toplevel(self.root)
        delete_win.geometry('500x500')

        lab_id = Label(delete_win, text='ID for delete:')
        lab_id.pack(padx=30, pady=30)

        ent_id_for_delete = ttk.Entry(delete_win)
        ent_id_for_delete.pack(padx=30, pady=30)

        def btn_sub_for_delete_entered():
            id_for_delete = ent_id_for_delete.get()
            back.delete_with_id(id_for_delete)
            delete_win.destroy()

        btn_sub_for_delete = ttk.Button(delete_win, text='Delete', command=btn_sub_for_delete_entered)
        btn_sub_for_delete.pack()

    def def_search_pressed(self):
        search_value = self.ent_search_book.get()
        rows_search_res = back.def_search(self.p.get(), search_value)
        self.ent_search_book.delete(0, END)

        top_show_res_search = Toplevel(self.root)
        top_show_res_search.title('***help: ( id , title , author , year , subject )***')
        top_show_res_search.geometry('500x400')

        text_box_search = Listbox(top_show_res_search, height=400, width=400)
        text_box_search.pack()

        for row in rows_search_res:
            text_box_search.insert(END, row)

    def btn_exit_pressed(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = LibraryApp(root)
    root.mainloop()
