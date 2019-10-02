import pyodbc
server = 'localhost,1433'
database = 'Ebook_store'
username = 'SA'
password = 'Passw0rd2018'
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = conn_nwdb.cursor()