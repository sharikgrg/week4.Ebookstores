from functions import *
from connecting_SQLdb import *

# testing the retrieve_all_books function
retrieve_all_books()

print('////////////////////////////// separation\\\\\\\\\\\\\\\\\\\\\\\\')

# retriving books by author name
retrieve_book("'Thermodynamics'")

creating_data("'Macbeth'", "'Shakespare'", "'1990-02-21'")