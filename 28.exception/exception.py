# errors
#1.Name error -> invalid var or obj name
a = 13
#b= c #name error

#2.FileNotFoundError 
#f = open("file1.txt")

#3.ValueError -> can't find value in obj
a=[1,3,4]
#a.remove(5) 

#4.IndexError
#print(a[6])

#5.KeyError
my_dic = {"name":"Mike"}
#my_dic["age"]
'''
x = -4
if x<0:
    raise Exception("x should be positive")
# raise AssertionError
assert (x>=0), "x is not positive"
'''
#ZeroDivisionError
try:
    a = 5 / 0
except:
    print("an error occured!!")

try:
    a = 5 / 0
    print("Hi")
except Exception as ex:
    print(ex)

try:
    a = 5 / 0 
except ZeroDivisionError as ex:
    print(ex,"error")

try:
    d = 0
    a = 5/d
    b = a + "10"
except ZeroDivisionError as e:
    print(e,"error")
except TypeError as e:
    print(e,"error")
else:
    print("every thing is fine!!")
finally:
    print("cleaning up...")