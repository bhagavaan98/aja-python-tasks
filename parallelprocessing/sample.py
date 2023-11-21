import multiprocessing, os
def fun1():
    print("fun1 processing: ", os.getpid())
def fun2():
    print("fun2 processing: ",os.getpid())

if __name__ == "__main__":
    print("base program: ", os.getpid())
    pr1 = multiprocessing.Process(target=fun1, name="pr1")
    pr2 = multiprocessing.Process(target=fun2, name="pr2")
    prs = [pr1, pr2]
    for pr in prs:
        pr.start()
    for pr in prs:
        pr.join() 
    print("main done")