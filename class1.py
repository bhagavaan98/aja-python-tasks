class Hello:
    time = 'nice'
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def rohit(obj):
        print('this is very:',obj.time)

    def crazy(self):
        print(self.name)
        print(self.age)
Hello.rohit= classmethod(Hello.rohit)
h = Hello('crazy', 25)
h.crazy()
