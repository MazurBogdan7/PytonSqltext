import pyodbc

server = 'localhost\sqlexpress'
bddata = 'DataSet'
# for test
user = 'DESKTOP-M56JFP4\alers'
password = ''
conn = pyodbc.connect('DRIVER={ODBC driver for SQL Server};SERVER='+server+'; DATABASE='+bddata+';UID='+user+';PWD='+password)