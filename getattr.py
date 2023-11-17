enc_trans = "".maketrans("abcdefgh","!@#$%^&*")
dec_trans = "".maketrans("!@#$%^&*","abcdefgh")
securedattrs = ("email",)
class Emp:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def __getattribute__(self, attr):
        print(attr, type(attr))
        return getattr(self, attr)
    def get_email(self):
        return self.email.translate(dec_trans)

        
jay = Emp("jairam","jay@gmail.com")
print(jay.email)
print(jay.name)