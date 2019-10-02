from connecting_SQLdb import *



def retrieve_all_books():
    table = (cursor.execute("SELECT * FROM books")).fetchall()
    for data in table:
        print (f' {data[0]}) Title: {data[1]} - Author: {data[2]} - Date: {data[3]}')

def retrieve_book(name):
    table = (cursor.execute(f"SELECT * FROM books WHERE Title = {name}")).fetchone()
    print(table)

def creating_data(title, author, date):
    (cursor.execute(f"INSERT INTO books (Title, Author, Dates) VALUES ({title}, {author}, {date})"))
    conn_nwdb.commit()
