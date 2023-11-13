with open("data.txt", "w") as f:
    for i in range(1024*1024*1024):
        file = open('data.txt', "a")
        file.write("Duplicate data \n")
        file.flush()
print("Done")  
