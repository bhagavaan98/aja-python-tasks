from model_file import Model


# with Model("root","Lucky@143","mysql") as v1:
#     v1.creating_model('p1',"(name varchar(30) , age int)")
#     v1.insert_model("insert into p1  values ('kanth',20),('Raju',23) ")

class person(Model):

    def name_validation(self,table_name):
        return table_name.isalpha()

    def creating_model(self,table_name,fields):
        
        # execution_querry = 'create table {} {}'.format(table_name,fields)
        # self.cur.execute(execution_querry)
        # print("Table is crated from person......")
        print(self)
        if self.name_validation(table_name) :
            Model.db_connection(self)
            Model.creating_model(self,table_name,fields)
            Model.db_commit(self)
            Model.db_close(self)
        else :
            print("Table name is not valid")


    
    def update_model(self,querry):
        Model.db_connection(self)
        Model.update_model(self,querry)
        Model.db_commit(self)
        Model.db_close(self)
    
    def insert_model(self,querry):
        Model.db_connection(self)
        Model.insert_model(self,querry)
        Model.db_commit(self)
        Model.db_close(self)
    def drop_model(self,querry):
        Model.db_connection(self)
        Model.drop_model(self,querry)
        Model.db_commit(self)
        Model.db_close(self)


#with person("root","Lucky@143","mysql") as v2:
    #v2.creating_model('v2',"(name varchar(30) , age int)")
    #v2.insert_model("insert into v2 values ('kanth',20),('Raju',23) ")

v2 = person("root","Lucky@143","mysql")
#v2.creating_model('v',"(name varchar(30) , age int)")
v2.insert_model("insert into v values ('kanth',20),('Raju',23) ")
v2.creating_model('v3',"(name varchar(30) , age int)")
