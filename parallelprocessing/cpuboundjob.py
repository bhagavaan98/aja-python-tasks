import time
import threading
import multiprocessing
import os
def fun1():
    print("fun1 processing: ", os.getpid())

    sum(range(40000000))
    print("fun1 done")

def fun2():
    print("fun2 processing: ",os.getpid())
    sum(range(40000000))
    print("fun2 done")
if __name__ == "__main__":
    t1 = time.time()
    print("base program: ", os.getpid())
    pr1 = multiprocessing.Process(target=fun1, name="pr1")
    pr2 = multiprocessing.Process(target=fun2, name="pr2")
    prs = [pr1, pr2]
    for pr in prs:
        pr.start()
    for pr in prs:
        pr.join() 
    print(time.time()-t1)
    print("main done")

# t1 = time.time()
#sequential
# fun1()
# fun2()

#threading
# th1 = threading.Thread(target=fun1, name="thread1")
# th2 = threading.Thread(target=fun2, name="thread2")
# thrs = [th1, th2]
# for thr in thrs:
#     thr.start()
# for thr in thrs:
#     thr.join() 
#Multi processing
