import os
from pur import Supplier
from my_pur import MySupplier 
"""
name = "sup@#"
s=MySupplier(name,"Hyderabad")

if s.validate():
    print(s.create())
else:
    print("issue in name")
print(s.validate_create())
"""
name = "sup@#"
s=MySupplier(name,"Hyderabad")
s.create()



"""
from sales import Customer
name = "cust1@#"
c=Customer(name,"Hyderabad")
print(c.create())
# validate the customer name make sure that it does not have special symbols
# if it has we need to send validation message.
"""
