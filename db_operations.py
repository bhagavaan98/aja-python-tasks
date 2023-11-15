'''
1. Write a class(DB) program to create a table, insert values, update values, delete values of the table.

All database operations code write in a file(db_operations.py) and call these operations in another file( app.py).

In app.py create instance of the DB class and call all the methods by passing some data
'''

import pymysql
class Db:
    con = pymysql.connect(user = 'root', password = 'root', database = 'ajadb', port = 3306)
    def create_table(self,table,fields):
        cur = Db.con.cursor()
        cur.execute(f"create table {table}{fields}")
        print('table created')
        cur.close()
        Db.con.close()
    def insert(self,table,fields,values):
        cur = Db.con.cursor()
        cur.execute(f"insert into {table}{fields} values{values}")
        Db.con.commit()
        print("data inserted")
        cur.close()
        Db.con.close()

    def update(self,query):
        cur = Db.con.cursor()
        cur.execute(f"{query}")
        Db.con.commit()
        print("data updated")
        cur.close()
        Db.con.close()

    def delete(self,query):
        cur = Db.con.cursor()
        cur.execute(f"{query}")
        Db.con.commit()
        print("data deleted")
        cur.close()
        Db.con.close()





