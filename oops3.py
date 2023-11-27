"""
3. Write a “Model” parent class and implement a create,update,delete method.
Write child class “Person” for Model and override methods create,update,delete methods. Call the parent(Model) class 
create 0method in the child(person) class create method and add small validation. create 

"""
import pymysql
class Person:
    def __init__(self, user, password, database,table):
        self.user = user
        self.password = password
        self.database = database
        self.table = table

    def db_connect(self):
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


class Model(Person):
    def validate_name(self,values):
        return values[0].isalnum()
    def validate_age(self,values):
        if 18 <= values[1] <= 35:
            return True
        return False
    def validate_salary(self,values):
        return values[2]>0
    def insert(self,fields,values):
        print(values[0])
        try:
            if self.validate_name(values) and self.validate_age(values) and self.validate_salary(values) :
                print("came")
                return super().insert(fields,values)
            else:
                print("name is not proper or age should be 18 to 35")
        except Exception as err:
            print(err)
             

obj = Model('root','root','ajadb','employee_data')
obj.db_connect()
obj.create_table()
obj.insert('(name,age,salary)',('vinay',32,190000))
obj.update("update employee3 set salary = 150000 where name = 'vinay'")
obj.delete("delete from employee3 where name = 'vinay'")
obj.commit()
obj.db_close()
obj.insert('(name,age,salary)',('vinay',32,190000))


