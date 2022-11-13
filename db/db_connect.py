
import pyodbc


server = 'DESKTOP-M56JFP4'
bddata = 'DataSet'
#for test

user = 'alers'
password = ''
connecting_str ='DRIVER={SQL Server};SERVER='+server+'; DATABASE='+bddata+';UID='+user+';PWD='+password


def send_query(query):
    conn = pyodbc.connect(connecting_str)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    return result


query = "select address, count(*) c from sport s group by address order by c desc limit 10"
send_query(query)
