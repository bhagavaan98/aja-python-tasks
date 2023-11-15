import pymysql

class DB:
    
    connect = pymysql.connect(user="root", password="root", database="aja")
    cur = connect.cursor()
    
    def __init__(self,table):
        self.table=table
        
    def create_table(self):
        
        try:
            query = f"create table {self.table}(id int, name varchar(50))"
            DB.cur.execute(query)
            print("Table Created successfully")
        except  Exception as err:
            print("DB error is",err)
        
        finally:
            DB.connect.close()
            
            
    def insert_data(self, x,y):  
        DB.connect
        query = f"insert into {self.table} values({x}, '{y}')"
        try:
            DB.cur.execute(query)
            DB.connect.commit()
            print("inserted successsfully")
            
        except Exception as err:
            print("DB error is",err)
        
        finally:
            DB.connect.close()
        
    def update_data(self, num, value):
        DB.connect
        query = f"update {self.table} set name='{value}' where id='{num}'"
        DB.cur.execute(query)
        DB.connect.commit()
        print("updated successsfully")
        DB.connect.close()
        
    def delete_data(self, num):
        DB.connect
        query = f"delete from {self.table} where id='{num}'"
        DB.cur.execute(query)
        DB.connect.commit()
        print("deleted successsfully")
        DB.connect.close()
        
        
        
    
ob = DB("fruitsapples")
#ob.create_table()
#ob.insert_data(1,"Banana")
ob.insert_data(2,"pineapple")
#ob.update_data(1,'mango')
#ob.delete_data(1)