"""
4. Create a child class for Person and extend two extra attributes. 
In person class of 3 if you have name,age attributes. In the child class now add two extra attributes (email and phone number) 
Do all Crud operations.
"""
import pymysql
class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        
    def dbconnct(self):
        self.con = pymysql.connect(user = 'root',password = 'root', port = 3306, database= 'ajadb')
        self.curr = self.con.cursor()
        print("connection opened")

    def dbclose(self):
        self.con.commit()
        self.con.close()
        print("connection closed")

    def create(self,table):
        self.table = table
        try:
            query = f'create table {self.table}(name varchar(20), age int, city varchar(15))'
            self.curr.execute(query)
            print("table created")
        except Exception as err:
            print(err)

    def insert(self):
        try:
            # query = f"insert into {self.table} values('{self.name}',{self.age},'{self.city}')"
            query = f"insert into {self.table}(name,age,city) values('{self.name}',{self.age},'{self.city}')"
            self.curr.execute(query)
            print("data inserted")
        except Exception as err:
            print(err)
class Child(Person):
    def __init__(self, name, age, city, email, phone):
        self.email = email
        self.phone = phone
        super().__init__(name, age, city)

    def create(self,table):
        self.table = table
        try:
            query = f"create table {self.table}(name varchar(20), age int, city varchar(15), email varchar(30), phone varchar(10))"
            self.curr.execute(query)
            print("table created")
        except Exception as err:
            print(err)

    def insert(self):
        try:
            # query = f"insert into {self.table} values('{self.name}',{self.age},'{self.city}')"
            query = f"insert into {self.table}(name,age,city,email,phone) values('{self.name}',{self.age},'{self.city}','{self.email}',{self.phone})"
            self.curr.execute(query)
            print("data inserted")
        except Exception as err:
            print(err)


ob = Child('eshwer',25, 'Hyderabad', 'eshwer@gmal.com',7842645592)
ob.dbconnct()
ob.create('passenger5')
ob.insert()
ob.dbclose()