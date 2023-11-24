from pur import Supplier
class MySupplier(Supplier):
    def validate(self):
        return self.name.isalnum()

    def validate_create(self):
        """
        """
        if self.validate():
            print(self.create())
        else:
            print("issue in name")

    def create(self):
        if self.validate():
           #Supplier.create(self)
           super(Supplier, self).create()
           #self.create()
        else:
            print("issue in name")

