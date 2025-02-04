import sqlite3

class BookBank:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """ایجاد جدول در دیتابیس اگر وجود نداشته باشد."""
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS book_bank (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER,
                subject TEXT
            )
        ''')
        self.conn.commit()

    def insert(self, title, author, year, subject):
        """افزودن یک کتاب جدید."""
        self.cur.execute('INSERT INTO book_bank (title, author, year, subject) VALUES (?, ?, ?, ?)',
                         (title, author, year, subject))
        self.conn.commit()

    def edit(self, book_id, field, new_value):
        """ویرایش اطلاعات یک کتاب."""
        if field in ['title', 'author', 'year', 'subject']:
            self.cur.execute(f'UPDATE book_bank SET {field} = ? WHERE id = ?', (new_value, book_id))
            self.conn.commit()
        else:
            raise ValueError("فیلد نامعتبر است!")

    def delete(self, book_id):
        """حذف کتاب با آی‌دی مشخص."""
        self.cur.execute('DELETE FROM book_bank WHERE id = ?', (book_id,))
        self.conn.commit()

    def search(self, field, search_value):
        """جستجو در دیتابیس بر اساس یک فیلد."""
        if field in ['title', 'author', 'year', 'subject']:
            self.cur.execute(f'SELECT * FROM book_bank WHERE {field} LIKE ?', ('%' + search_value + '%',))
            return self.cur.fetchall()
        else:
            raise ValueError("فیلد نامعتبر است!")

    def show_all(self):
        """دریافت تمام کتاب‌ها از دیتابیس."""
        self.cur.execute('SELECT * FROM book_bank')
        return self.cur.fetchall()

    def close(self):
        """بستن اتصال به دیتابیس."""
        self.conn.close()

# تست سریع

db = BookBank()
db.insert("1984", "George Orwell", 1949, "Dystopian")
print(db.show_all())
db.close()
