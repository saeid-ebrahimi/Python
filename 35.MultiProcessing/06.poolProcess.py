from multiprocessing import Pool
def cube(number):
    return number*number*number

if __name__ == "__main__":
    pool = Pool()
    numbers = range(10)
    # map , apply, join , close
    result = pool.map(cube,numbers)
    #r = pool.apply(cube,numbers[1])   
    pool.close()
    pool.join()

    print(result)