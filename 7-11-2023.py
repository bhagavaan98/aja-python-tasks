def fun(name,age,aadhar=None,phone=None,**kwargs):
    print("name:",name)
    print("age:",age)
    if "email" in kwargs:
        print("email is an extra field")
    elif aadhar is not None:
        print("aadhar is extra field",aadhar)
    elif phone is not None:
        print("phone:",phone)
try:
    fun("ramesh",25,phone="45613576621",email="bhag@gmail.com")
    print()
    fun(phone="1235795664",email="ravi@gmail.com")
    print()
except:
    print("age and name are mandatory")
