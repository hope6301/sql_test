from datetime import datetime
from multiprocessing import connection
from sqlite3 import Cursor
import mysql.connector



'''
connection = mysql.connector.connect(host = 'localhost',
                                        port = '3306',
                                        user = 'root',
                                        password = 'hope0208')
cursor = connection.cursor()
sql = "select * from vemar_database.vemar_table_2;"
cursor.execute(sql)

recods = cursor.fetchall()
for r in recods:
    print(r)

cursor.close()
connection.close()
'''



def one_select_table(one_date:datetime,Campaign_Obj:str):

    connection = mysql.connector.connect(host = 'localhost',
                                        port = '3306',
                                        user = 'root',
                                        password = 'hope0208')
    cursor = connection.cursor()

    if Campaign_Obj == "all":
        sql = "select * from vemar_database.vemar_table_2 where Tdate Like \"{}\";".format(one_date)
    else:
        sql = "select * from vemar_database.vemar_table_2 where Tdate like \"{}\" and Campaign_Objective like \"{}\" group by Tdate ,Campaign_Objective ORDER BY tt ;".format(one_date,Campaign_Obj)

    cursor.execute(sql)

    tt=[]


    field_name = [des[0] for des in cursor.description]

    recods = cursor.fetchall()

    tt.append(field_name)
    for r in recods:
        tt.append(r)

    


    cursor.close()
    connection.close()

    return tt




def startend_select_table(start_date:datetime,end_date:datetime,Campaign_Obj:str):

    connection = mysql.connector.connect(host = 'localhost',
                                        port = '3306',
                                        user = 'root',
                                        password = 'hope0208')
    cursor = connection.cursor()



    sql = "select * from vemar_database.vemar_table_2 where Tdate BETWEEN \"{}\" and \"{}\";".format(start_date,end_date)



    cursor.execute(sql)
    recods = cursor.fetchall()

    cursor.close()
    connection.close()

    return recods















'''


def get_select_table(table_name:str,field_name:str,month:int):
    connection = mysql.connector.connect(host = 'localhost',
                                        port = '3306',
                                        user = 'root',
                                        password = 'hope0208')
    cursor = connection.cursor()
    #st = "SELECT * FROM vemar_database.vemar_table WHERE {} LIKE {};".format(x,1)Campaign Objective
    #st = "SELECT * FROM vemar_database.vemar_table WHERE Campaign Objective LIKE {};".format(1)

    sql = "SELECT * FROM vemar_database.vemar_table;"
    cursor.execute(sql)


    recods = cursor.fetchall()
    for r in recods:
        print(r)

    cursor.close()
    connection.close()

    df = 0
    return df

connection = mysql.connector.connect(host = 'localhost',
                                        port = '3306',
                                        user = 'root',
                                        password = 'hope0208')
cursor = connection.cursor()
#st = "SELECT * FROM vemar_database.vemar_table WHERE {} LIKE {};".format(x,1)Campaign Objective
#st = "SELECT * FROM vemar_database.vemar_table WHERE Campaign Objective LIKE {};".format(1)

sql = "select * from vemar_database.vemar_table_2;"
cursor.execute(sql)


recods = cursor.fetchall()
for r in recods:
    print(r)

cursor.close()
connection.close()


'''