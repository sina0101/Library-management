import sqlite3

class BookBank:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the book_bank table if it doesn't exist."""
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS book_bank(
                id INTEGER PRIMARY KEY,
                title VARCHAR(30),
                author VARCHAR(30),
                year INTEGER,
                subject VARCHAR(20)
            )
        ''')
        self.conn.commit()

    def insert(self, title, author, year, subject):
        """Insert a new book into the book_bank table."""
        self.cur.execute('''
            INSERT INTO book_bank(title, author, year, subject) 
            VALUES(?, ?, ?, ?)
        ''', (title, author, year, subject))
        self.conn.commit()

    def edit(self, id, field, new_value):
        """Edit a book's information based on the given field."""
        if field in ['title', 'author', 'year', 'subject']:
            self.cur.execute(f'''
                UPDATE book_bank 
                SET {field} = ? 
                WHERE id = ?
            ''', (new_value, id))
            self.conn.commit()
        else:
            raise ValueError("Invalid field specified")

    def delete_with_id(self, id_for_delete):
        """Delete a book from the book_bank table based on its ID."""
        self.cur.execute('''
            DELETE FROM book_bank 
            WHERE id = ?
        ''', (id_for_delete,))
        self.conn.commit()

    def search(self, field, search_value):
        """Search for books based on a specific field and value."""
        if field in ['title', 'author', 'year', 'subject']:
            self.cur.execute(f'''
                SELECT * 
                FROM book_bank 
                WHERE {field} = ?
            ''', (search_value,))
            return self.cur.fetchall()
        else:
            raise ValueError("Invalid field specified")

    def show_all(self):
        """Retrieve all books from the book_bank table."""
        self.cur.execute('SELECT * FROM book_bank')
        return self.cur.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db = BookBank()

    # Insert a new book
    db.insert("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")

    # Edit a book's year
    db.edit(1, 'year', 1926)

    # Search for books by author
    books_by_author = db.search('author', 'F. Scott Fitzgerald')
    print(books_by_author)

    # Show all books
    all_books = db.show_all()
    print(all_books)

    # Delete a book by ID
    db.delete_with_id(1)

    # Close the database connection
    db.close()
