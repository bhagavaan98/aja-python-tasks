'''
1. Write a class(DB) program to create a table, insert values, update values, delete values of the table.

All database operations code write in a file(db_operations.py) and call these operations in another file( app.py).

In app.py create instance of the DB class and call all the methods by passing some data
'''

import pymysql
class Db:
    def __init__(self, user, password, database,table):
        self.user = user
        self.password = password
        self.database = database
        self.table = table

    def db_connct(self):
        self.con = pymysql.connect(user = self.user, password = self.password, database = self.database)
        self.cur = self.con.cursor()
        print('cursor opened')

    def db_close(self):
        self.cur.close()
        self.con.close()
        print("connection closed")
    def create_table(self):
        try:
            self.cur.execute(f"create table {self.table}(name varchar(20), age int, salary int)")
            print('table created')
        except Exception as er:
            print(er)
    def insert(self,fields,values):
        try:
            self.cur.execute(f"insert into {self.table}{fields} values{values}")
            print("data inserted")
        except Exception as er:
            print(er)
    def update(self,query):
        try:
            self.cur.execute(f"{query}")
            print("data updated")
        except Exception as er:
            print(er)
    def delete(self,query):
        try:
            self.cur.execute(f"{query}")
            print("data deleted")
        except Exception as er:
            print(er)
    def commit(self):
        self.con.commit()
        print("all transactions saved in database")

# using with:-

import pymysql
class DB:
    def __init__(self, username, password, database, table):
        self.username=username
        self.password=password
        self.table=table
        self.db=database
    def db_conn(self):
        self.con = pymysql.connect(user=self.username, 
                                       password=self.password, 
                                       database=self.db)
        self.cur = self.con.cursor()
    def db_close(self):
        self.cur.close()
        self.con.close()
        
    def create_table(self):
        try:
            query = f"create table {self.table}(id int, name varchar(50))"
            DB.cur.execute(query)
            print("Table Created successfully")
        except  Exception as err:
            print("DB error is",err)

    def insert_data(self, x,y):  
        query = f"insert into {self.table} values({x}, '{y}')"
        try:
            self.cur.execute(query)
            print("inserted successsfully")
            
        except Exception as err:
            print("DB error is",err)
    
        
    def update_data(self, num, value):
        query = f"update {self.table} set name='{value}' where id='{num}'"
        self.cur.execute(query)
        print("updated successsfully")
        
    def delete_data(self, num):
        query = f"delete from {self.table} where id='{num}'"
        self.cur.execute(query)
        print("deleted successsfully")
        
    def db_commit(self):
        self.con.commit()
        
    def __enter__(self):
        self.db_conn()
        return self
    
    def __exit__(self, *args, **kwars):
        self.db_commit()
        self.db_close()
        
with DB("root","root","aja","fruits") as db_ob:
    db_ob.insert_data(2,"banana")
    db_ob.update_data(2,'pineapple')
    
print("DONE")




