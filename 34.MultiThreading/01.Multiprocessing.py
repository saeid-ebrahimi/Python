from multiprocessing import Process
import os
import time
def square_numbers(num:int):
    for i in range(num):
        i + i
        time.sleep(1)

if __name__=="__main__":
    processes = []
    num_of_processes = os.cpu_count()
    # create processes
    for i in range(num_of_processes):
        p = Process(target=square_numbers,args=(50,))
        processes.append(p)

    # start 
    for p in processes:
        p.start()

    # join 
    for p in processes:
        p.join()

    print("End Main")  