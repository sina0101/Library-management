import tkinter as tk
from tkinter import ttk, messagebox
import back

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry("600x400")
        self.db = back.BookBank()

        # ویجت‌های صفحه
        self.create_widgets()

    def create_widgets(self):
        # لیست نمایش داده‌ها
        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Author", "Year", "Subject"), show="headings")
        for col in ("ID", "Title", "Author", "Year", "Subject"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # دکمه‌ها
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Show All", command=self.show_all).pack(side="left", padx=5)
        tk.Button(frame_buttons, text="New", command=self.add_book).pack(side="left", padx=5)
        tk.Button(frame_buttons, text="Edit", command=self.edit_book).pack(side="left", padx=5)
        tk.Button(frame_buttons, text="Delete", command=self.delete_book).pack(side="left", padx=5)

        # جستجو
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(frame_buttons, textvariable=self.search_var)
        self.search_entry.pack(side="left", padx=5)
        tk.Button(frame_buttons, text="Search", command=self.search_book).pack(side="left", padx=5)

        self.show_all()

    def show_all(self):
        """نمایش تمام کتاب‌ها در جدول."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in self.db.show_all():
            self.tree.insert("", "end", values=book)

    def add_book(self):
        """فرم افزودن کتاب جدید."""
        self.open_form("Add Book", self.db.insert)

    def edit_book(self):
        """فرم ویرایش اطلاعات یک کتاب."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to edit.")
            return

        book_id = self.tree.item(selected_item)["values"][0]
        self.open_form("Edit Book", lambda t, a, y, s: self.db.edit(book_id, "title", t) or
                                               self.db.edit(book_id, "author", a) or
                                               self.db.edit(book_id, "year", y) or
                                               self.db.edit(book_id, "subject", s))

    def delete_book(self):
        """حذف کتاب انتخاب شده."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to delete.")
            return

        book_id = self.tree.item(selected_item)["values"][0]
        self.db.delete(book_id)
        self.show_all()

    def search_book(self):
        """جستجو در دیتابیس."""
        query = self.search_var.get()
        if not query:
            self.show_all()
            return

        results = self.db.search("title", query)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in results:
            self.tree.insert("", "end", values=book)

    def open_form(self, title, callback):
        """فرم برای اضافه یا ویرایش کتاب."""
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("300x200")

        tk.Label(form, text="Title:").pack()
        entry_title = tk.Entry(form)
        entry_title.pack()

        tk.Label(form, text="Author:").pack()
        entry_author = tk.Entry(form)
        entry_author.pack()

        tk.Label(form, text="Year:").pack()
        entry_year = tk.Entry(form)
        entry_year.pack()

        tk.Label(form, text="Subject:").pack()
        entry_subject = tk.Entry(form)
        entry_subject.pack()

        def submit():
            callback(entry_title.get(), entry_author.get(), entry_year.get(), entry_subject.get())
            form.destroy()
            self.show_all()

        tk.Button(form, text="Submit", command=submit).pack(pady=10)


root = tk.Tk()
app = LibraryApp(root)
root.mainloop()
