import pymysql

class Model:
    def __init__(self,username,password,databse):
        self.username = username 
        self.password = password 
        self.database = databse 
    
    def db_connection(self):
        self.cun = pymysql.connect(user=self.username,password=self.password,database=self.database)
        self.cur = self.cun.cursor()
    
    def db_commit(self):
        self.cun.commit()
    def db_close(self):
        self.cur.close()
        self.cun.close()
    
    def __enter__(self):
        self.db_connection()
        print(self)
        return self
    def __exit__(self,*args,**kwrgs):
        self.db_commit()
        self.db_close()

    def creating_model(self,table_name,fields):
        execution_querry = 'create table {} {}'.format(table_name,fields)
        self.cur.execute(execution_querry)
        print("Table is crated.........")
    
    def update_model(self,querry):
        self.cur.execute(querry)
        print("Table is updated....")
    
    def insert_model(self,querry):
        self.cur.execute(querry)
        print("Table is insert....")
    def drop_model(self,querry):
        self.cur.execute(querry)
        print("Table is dropped....")