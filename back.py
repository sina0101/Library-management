import sqlite3


global cur
db=sqlite3.connect('database.db')
cur=db.cursor()





def create():
    
    cur.execute('''
          CREATE TABLE IF NOT EXISTS book_bank(
                
            id INTEGER PRIMARY KEY,
            title VARCHAR(30),
            author VARCHAR(30),
            year INTEGER,
            subject VARCHAR(20)
          )      
                
                ''')

create()

def insert(title,author,year,subject):
    
    
   
    
    cur.execute('''
INSERT INTO book_bank(title,author,year,subject) VALUES(?,?,?,?)


''',(title,author,year,subject))
    db.commit()


def edit(id,sell,new_value):
    if sell=='year':
    
    
        cur.execute('''
        UPDATE book_bank SET year =?   WHERE id=? 


    ''',(new_value,id))
        

    if sell=='author':
    
    
        cur.execute('''
        UPDATE book_bank SET author =?   WHERE id=? 


    ''',(new_value,id))


    if sell=='subject':
        cur.execute('''
        UPDATE book_bank SET subject =?   WHERE id=? 


    ''',(new_value,id))


    if sell=='title':

        cur.execute('''

        UPDATE book_bank SET title=? WHERE id=?

''',(new_value,id))
        
    db.commit()


def delete_with_id(id_for_delete):
    
    cur.execute('''
    DELETE FROM book_bank WHERE id=?

''',(id_for_delete,))
    db.commit()
    
    '''def show_all():
    cur.execute('SELECT * from book_bank')
    rows = cur.fetchall()
    return rows'''

def def_search(v,search_value):
    
    if v=='title':
        res=cur.execute('''

        SELECT * FROM book_bank WHERE title=? 


    ''',(search_value,))
        

    if v=='author':
        res=cur.execute('''

        SELECT * FROM book_bank WHERE author=? 


    ''',(search_value,))
    

    if v=='year':
        res=cur.execute('''

        SELECT * FROM book_bank WHERE year=? 


    ''',(search_value,))
        
    if v=='subject':
        res=cur.execute('''

        SELECT * FROM book_bank WHERE subject=? 


    ''',(search_value,))
        



    res=cur.fetchall()
    return res
    


def show_all():
    cur.execute('SELECT * from book_bank')
    rows = cur.fetchall()
    return rows

    

