from os import *
print(name)
parent_path = getcwd()
print(parent_path)
#mkdir('hell')
chdir(parent_path+'/hell')
print(getcwd())
future_path = './love/burn/you/us/i'
#makedirs(future_path)
chdir(future_path)
print(getcwd())
relative_path = 'hell/love/burn/you/us/i'

absolute_path = path.join(parent_path, relative_path )
relative_path2 = path.join(parent_path, 'hell/love/burn/you/i')
print(path)
print(relative_path2)
print(listdir(parent_path))
remove()
rmdir()
