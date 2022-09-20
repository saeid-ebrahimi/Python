# Generators are memory efficient for large data 

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(10)  # generators did not call yet

value  =next(cd) # it call generator
print(value)

print(next(cd))