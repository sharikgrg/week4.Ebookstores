from connecting_SQLdb import *

# def retrieve_all_books():
#     table = (cursor.execute("SELECT * FROM books")).fetchall()
#     for list in table:
#         print (list)

def retrieve_all_books():
    table = (cursor.execute("SELECT * FROM books")).fetchall()
    for list in table:
        print (list)

def retrieve_book(name):
    data = (cursor.execute(f"SELECT Author, Title, Dates FROM books WHERE Author = {name}")).fetchall()
    print(data)