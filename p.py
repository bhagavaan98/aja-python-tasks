class Cart:
    def __init__(self):
        self.items={}
    def add_product(self,item_name,quantity):
        self.items[item_name]=quantity
    def get_items(self):
        print(self.items)
obj=Cart()
obj.add_product('banana',10)
obj.get_items()
obj.add_product('apple',20)
obj.get_items()