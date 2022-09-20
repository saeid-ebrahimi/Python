from threading import Thread, Lock
import os
import time
database_value = 0
def increase(lock):
    global database_value
    lock.acquire()
    local_copy = database_value
    # processing 
    local_copy += 1
    time.sleep(0.5)
    database_value = local_copy
    lock.release()

def increase2(lock):
    global database_value
    # context manager
    with lock:
        local_copy = database_value
        # processing
        local_copy += 1
        time.sleep(0.5)
        database_value = local_copy
if __name__=="__main__":
    print("start value",database_value)
    lock = Lock()
    thread1 = Thread(target=increase,args=(lock,))
    thread2 = Thread(target=increase,args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value",database_value)

    print("end main")

