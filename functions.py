from connecting_SQLdb import *

def retrieve_all_books(query):
    return cursor.execute("SELECT * FROM books")