numbers = list(range(2,15))
first , second ,*middle,second_last,last = numbers

print(middle)
my_tuple = (1,2,3,4,5)
my_list =[6,7,8,9]

new_list = [*my_tuple ,*my_list]
print(new_list)

dict_a = {'a':1, 'b':2, 'c':3}
dict_b = {'d':4,'e':5,'f':4}
my_dic = {**dict_a,**dict_b}

