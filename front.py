import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import back

win=Tk()
win.geometry('400x350')
win.title('Library Managment')
win.resizable(False,False)

frametop = Frame(win)
frametop.config(width=200,height=20)
frametop.pack()

Entryframe = Frame(frametop)
Entryframe.pack(side=LEFT,padx=30)

Buttonframe=Frame(frametop,width=80,height=0)
Buttonframe.pack(side=RIGHT)

def show_all_pressed():
    top_show_all=Toplevel(win)
    top_show_all.title('***help: ( id , title , author , year , subject )***')
    top_show_all.geometry('500x400')
    rows=back.show_all()
    
    #text_box = Text(top_show_all, wrap=WORD)
    #text_box.pack()
    list_box1=Listbox(top_show_all,height=400,width=400)
    if  len(rows)==0:
        messagebox.showerror('No Data!')
    for row in rows:
        
        list_box1.pack()
        #list_box1.insert(END,row)
        list_box1.insert(END,row)
    top_show_all.mainloop()
    
    

btn_show_all=ttk.Button(Buttonframe,text='show all',command=show_all_pressed)
btn_show_all.pack(pady=10,padx=10)

def insert_presed():
    title=ent_book_title.get()
    author=ent_author.get()
    year=ent_publish_year.get()
    subject=ent_subject.get()

    ent_book_title.delete(0,len(title))
    ent_author.delete(0,len(author))
    ent_publish_year.delete(0,len(year))
    ent_subject.delete(0,len(subject))
    back.insert(title,author,year,subject)
    
btn_new=ttk.Button(Buttonframe,text='new',command=insert_presed)
btn_new.pack(pady=10,padx=10)

def def_edit():
    edit_win=Toplevel(win)
    edit_win.geometry('500x500')
    
    lab_id=Label(edit_win,text='id')
    lab_id.pack()

    ent_id=ttk.Entry(edit_win)
    ent_id.pack()
    
    lab_title=Label(edit_win,text='please select !')
    lab_title.pack()

    #ent_sell=ttk.Entry(edit_win)
    #ent_sell.pack()


    p=StringVar()
    radio_title=ttk.Radiobutton(edit_win,text='title',variable=p,value='title')
    radio_title.pack(padx=(225,0),anchor=W)

    radio_author=ttk.Radiobutton(edit_win,text='author',variable=p,value='author')
    radio_author.pack(padx=(225,0),anchor=W)

    radio_year=ttk.Radiobutton(edit_win,text='year',variable=p,value='year')
    radio_year.pack(padx=(225,0),anchor=W)

    radio_subject=ttk.Radiobutton(edit_win,text='subject',variable=p,value='subject')
    radio_subject.pack(padx=(225,0),anchor=W)


    lab_flash=Label(edit_win)
    lab_flash.pack()

    lab_change_to=Label(edit_win,text='change to')
    lab_change_to.pack()

    ent_new_value=ttk.Entry(edit_win)
    ent_new_value.pack()
    
    def btn_sub_pressed():
        id=ent_id.get()
        sell=p.get()
        new_value=ent_new_value.get()
        back.edit(id,sell,new_value)
        edit_win.destroy()

    btn_submit_edit=ttk.Button(edit_win,text='sub',state='normal',command=btn_sub_pressed)
    btn_submit_edit.pack(pady=20)
    
btn_edit=ttk.Button(Buttonframe,text='edit',command=def_edit)
btn_edit.pack(pady=10,padx=10)

def btn_sub_for_delete_entered():
    id_for_delete=ent_id_for_delete.get()
    ent_id_for_delete.delete(0,len(id_for_delete))
    back.delete_with_id(id_for_delete)
    delete_win.destroy()

def def_delete():
    global ent_id_for_delete , delete_win
    delete_win=Toplevel(win)
    delete_win.geometry('500x500')

    lab_id=Label(delete_win,text='id for delete it:')
    lab_id.pack(padx=30,pady=30)

    ent_id_for_delete=ttk.Entry(delete_win)
    ent_id_for_delete.pack(padx=30,pady=30)

    btn_sub_for_delete=ttk.Button(delete_win,text='enter me for delete',command=btn_sub_for_delete_entered)
    btn_sub_for_delete.pack()

    delete_win.mainloop()

btn_delete=ttk.Button(Buttonframe,text='delete',command=def_delete)
btn_delete.pack(pady=10,padx=10)

def btn_exit_pressed():
    win.destroy()

btn_exit=ttk.Button(Buttonframe,text='exit',command=btn_exit_pressed)
btn_exit.pack(pady=10,padx=10)

lb_book_tittle=Label(Entryframe,text='Book title :')
lb_book_tittle.grid(row=0,column=0,pady=9)

ent_book_title=ttk.Entry(Entryframe)
ent_book_title.grid(row=0,column=1,pady=9)

lb_author=Label(Entryframe,text='authot :')
lb_author.grid(row=1,column=0,pady=9)

ent_author=ttk.Entry(Entryframe)
ent_author.grid(row=1,column=1,pady=9)

lb_publish_year=Label(Entryframe,text='publish year :')
lb_publish_year.grid(row=2,column=0,pady=9)

ent_publish_year=ttk.Entry(Entryframe)
ent_publish_year.grid(row=2,column=1,pady=9)

lb_subject=Label(Entryframe,text='subject :')
lb_subject.grid(row=3,column=0,pady=9)

ent_subject=ttk.Entry(Entryframe)
ent_subject.grid(row=3,column=1,pady=9)

def def_search_pressed():
    list_res_search=ent_search_value=ent_serch_book.get()
    rows_search_res=back.def_search(p.get(),ent_search_value)
    ent_serch_book.delete(0,len(ent_search_value))

    top_show_res_search=Toplevel(win)
    top_show_res_search.title('***help: ( id , title , author , year , subject )***')
    top_show_res_search.geometry('500x400')
    
    text_box_search = Listbox(top_show_res_search,height=400,width=400)
    text_box_search.pack()
    for row1 in rows_search_res:
        text_box_search.insert(END,row1)
    top_show_res_search.mainloop()

frm4=Frame(win,height=20)
frm4.pack(side=BOTTOM,pady=10)

p=StringVar()
radio_title=ttk.Radiobutton(frm4,text='title',variable=p,value='title')
radio_title.pack(side='left',anchor=W,padx=6)

radio_author=ttk.Radiobutton(frm4,text='author',variable=p,value='author')
radio_author.pack(side='left',anchor=W,padx=6)

radio_year=ttk.Radiobutton(frm4,text='year',variable=p,value='year')
radio_year.pack(side='left',anchor=W,padx=6)

radio_subject=ttk.Radiobutton(frm4,text='subject',variable=p,value='subject')
radio_subject.pack(side='left',anchor=W,padx=6)

searchframe = Frame(win)
searchframe.pack(side=BOTTOM)

btn_search=ttk.Button(searchframe,text='search',command=def_search_pressed)
btn_search.pack(side='right',padx=10,pady=10)

ent_serch_book=ttk.Entry(searchframe)
ent_serch_book.config(width=30)
ent_serch_book.pack(side='right')

win.mainloop()
