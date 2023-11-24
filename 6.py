'''Take the size of your hard disk in GB 

     	Show that in MB, KB, TB, PB '''
GB = float(input("Enter the size in GB : "))
print(f"The of {GB} in MB is {GB*1024}")
print(f"The of {GB} in KB is {GB*1048576}")
print(f"The of {GB} in MB is {GB*0.001}")
print(f"The of {GB} in MB is {GB/1048576}")