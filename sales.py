class Customer:
    def __init__(self, name, address):
        self.name=name
        self.address=address
 
    def create(self):
        # connect to db
        # prepare insert query and insert data in to database
        print(f"insert into customer values('{self.name}','{self.address}')")
        return True