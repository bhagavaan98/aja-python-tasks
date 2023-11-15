from Database import DB


with DB("root","Lucky@143","mysql") as v1:
    v1.creating_table("student",name="varchar(30)",id="int")









# v1.insert_into_table("student",("anil",30),("Ramya",40))
# v1.deleting_table("Lk")

# v1.updating_table("student","name","raju")