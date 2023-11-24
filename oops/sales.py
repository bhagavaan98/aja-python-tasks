class Customer:
    def __init__(self, name, address):
        self.name=name
        self.address=address

    def create(self):
        if not self.name.isalnum():
            print("issue with customer name")
        else:
            print(f"insert into customer values('{self.name}','{self.address}')")
            return True