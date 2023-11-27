from db_operations import Db

ob1 = Db()
ob1.create_table('Employee3','(name varchar(50), empid int, salary int)')
# ob1.insert('Employee3','(name,empid,salary)',"('shravan',1064,78000)")
# ob1.update("update employee3 set salary = 150000 where name = 'shravan'")
# ob1.delete("delete from employee3 where name = 'prakash'")