import pymysql
con = pymysql.connect(user="root",password="Lucky@143",database="mysql",port=3306)
cur = con.cursor()


class DB:
    con = pymysql.connect(user="root",password="Lucky@143",database="mysql",port=3306)
    cur = con.cursor()
    def __init__(self):
        pass
    def creating_table(self,table_name,**kwra):
        
        
            fields = ""
            for i,j in kwra.items():
                fields = fields + i + " " + j + ","
            fields = fields[:len(fields)-1]
            querry = "create table {} ({})".format(table_name,fields)
        
            cur.execute(querry)
            
            DB.con.close()

       
       

    def insert_into_table(self,table_name,*args):
        DB.con
        field = ""
        for i in args:
            field = field + str(i) + ","
        
        field = field[:len(field)-1]
        insert_querry = "insert into {} values {}".format(table_name,field)
        print(insert_querry)
        
        cur.execute(insert_querry)
        DB.con.commit()
        DB.con.close()
    

    def deleting_table(self,table_name):
         querry = "drop table {}".format(table_name)
         cur.execute(querry)
         DB.con.close()
    
    def updating_table(self,table_name,col_name,value):
        uodated_querry = "update {} set {} =".format(table_name,col_name)
        print(uodated_querry)
        print(type(value))
        cur.execute(uodated_querry+value)
        DB.con.close()
        DB.con.commit()
         