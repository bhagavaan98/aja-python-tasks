import pymysql
con = pymysql.connect(user="root",password="Lucky@143",database="mysql",port=3306)
cur = con.cursor()


class DB:
    
    def __init__(self,user,password,database):
        self.user = user
        self.password = password
        self.database = database
    
    def db_connection(self):
         
         self.con = pymysql.connect(user=self.user,password=self.password,database=self.database)
         self.cur = self.con.cursor()

    def __enter__(self):
         
        self.db_connection()
        return
    
    def __exit__(self,*args,**kwargs):
         self.cur.close()
         self.con.close()
         

    def creating_table(self,table_name,**kwra):
        
        
            fields = ""
            for i,j in kwra.items():
                fields = fields +i + " " + j + ","
            fields = fields[:len(fields)-1]
            querry = "create table {} ({})".format(table_name,fields)
         
            self.cur.execute(querry)
        
           
       
       

    def insert_into_table(self,table_name,*args):
        
        field = ""
        for i in args:
            field = field + str(i) + ","
        
        field = field[:len(field)-1]
        insert_querry = "insert into {} values {}".format(table_name,field)
        print(insert_querry)
        
        self.cur.execute(insert_querry)
       
    

    def deleting_table(self,table_name):
         querry = "drop table {}".format(table_name)
         self.cur.execute(querry)
         
    
    def updating_table(self,table_name,col_name,value):
        uodated_querry = "update {} set {} =".format(table_name,col_name)
        
        
        self.cur.execute(uodated_querry+value)
        