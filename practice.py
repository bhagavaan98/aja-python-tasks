class Start:
    def __init__(self,age,place):
        self.age= age
        self.place= place
    def get(self):
        print('I do not understand oops')
a=Start(18,'hyderabad')
Start.get(19)
print(a.age)
print(a.place)