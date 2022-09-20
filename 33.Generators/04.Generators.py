import sys 
def fibonacci(limit):
    a , b =0,1
    while a < limit:
        yield a
        a , b = b, a+b

fib = fibonacci(30)
for term in fib :
    print(term)