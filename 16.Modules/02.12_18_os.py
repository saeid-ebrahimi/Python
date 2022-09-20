# 12
print('#12')
import os
path=os.getcwd()
print("Test a path exists or not:")
path = path + '/main.py'
print(os.path.exists(path))
print(os.path.exists(path+'/os.py'))
print("File name of the path:")
print(os.path.basename(path))
print("Dir name of the path:")
print(os.path.dirname(path))

# 13
print('#13')
import os
path = os.getcwd()
print("Original path:")
print(path)
print("\nDir of the said path:")
print(os.path.split(path))
print("\nJoin one or more path components together:")
print(os.path.join(path,'hell'))

# 14
print('#14')
import os
fd = os.open( os.getcwd(), os.O_RDONLY )
os.fchown( fd, 100, -1)
os.fchown( fd, -1, 50)
print("Changed ownership successfully..")
os.close( fd )

# 15
print('#15')
import os
path = os.getcwd()+'/main.py'
print(path)
fd = os.open(path, os.O_RDWR)
info = os.fstat(fd)
print (f"ID of device containing file: {info.st_dev}")
print (f"Inode number: {info.st_ino}")
print (f"Protection: {info.st_mode}")
print (f"Number of hard links: {info.st_nlink}")
print (f"User ID of owner: {info.st_uid}")
print (f"Group ID of owner: {info.st_gid}")
print (f"Total size, in bytes: {info.st_size}")
print (f"Time of last access: {info.st_atime}")
print (f"Time of last modification: {info.st_mtime }")
print (f"Time of last status change: {info.st_ctime }")
os.close( fd)

# 16
print('#16')
import io
# Write a string to a buffer
output = io.StringIO()
output.write('Python , Practice, Patient')
# Retrieve the value written
print(output.getvalue())
# Discard buffer memory
output.close()

# 17
print('#17')
import os
if os.name == 'nt':
	cmd = 'dir'
else:
	cmd = 'ls -l'
os.system(cmd)

# 18
print('#18')
import os
if os.name == "nt":
   command = "dir"
else:
   command = "ls -l"
os.system(command)
