import time
import threading
def fun1():
    print("fun1 processing")
    time.sleep(5)
    print("fun1 done")

def fun2():
    print("fun2 processing")
    time.sleep(5)
    print("fun2 done")
# sequential execution
'''
t1 = time.time()
fun1()
fun2()
print(time.time()-t1)
'''
print("number of threads",threading.active_count())
t1 = time.time()
th1 = threading.Thread(target=fun1, name="thread1")
th2 = threading.Thread(target=fun2, name="thread2")
thrs = [th1, th2]
for thr in thrs:
    thr.start() 
# th1.start()
# th2.start()
print("number of threads",threading.active_count())
for thr in thrs:
    thr.join() 
# while th1.is_alive():
#     print("th1 is alive")
#     continue
# while th2.is_alive():
#     print("th2 is alive")
#     continue 

print(time.time()-t1)
print("number of threads",threading.active_count())
print("main done")