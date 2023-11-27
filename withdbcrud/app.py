"""
1. Write a class(DB) program to create a table, insert values, update values, delete values of the table.
All database operations code write in a file(db_operations.py) and call these operations in another file( app.py).
In 
"""

from db_operations import Db

# ob1 = Db('root','root','ajadb','employeedata')
# ob1.db_connct()
# # # ob1.create_table()
# # ob1.insert('(name,age,salary)',"('vijay',1064,78000)")
# # ob1.update("update employee3 set salary = 150000 where name = 'vijay'")
# # ob1.delete("delete from employee3 where name = 'shravan'")
# # ob1.commit()
# ob1.db_close()


with Db("root","root","aja","fruits") as db_ob:
    db_ob.insert('(name,age,salary)',"('vijay',1064,78000)")
    db_ob.update("update employee3 set salary = 150000 where name = 'vijay'")
    
print("DONE")