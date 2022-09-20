
if __name__ == '__main__':
    print('#1')
    import os

    print('os name', os.name)
    # print('os user', os.uname())  # in unix
    print('logged in username', os.getlogin())
    print('current working directory: ', os.getcwd())
    print('current directory ,directories list: ', os.listdir('.'))
    print(os.listdir(r'E:\Users'))

    # 2
    print('#2')
    import os
    path1 = 'F:\\'
    print('Folders:')
    for name in os.listdir(path1):
        if os.path.isdir(os.path.join(path1, name)):
            print(name)
    print('Files')
    for name in os.listdir(path1):
        if os.path.isfile(os.path.join(path1, name)):
            print(name)
    print('All files and directories: ', os.listdir(path1))


    # 3
    print('#3')
    import os
    path2 = 'E:\\'
    for obj in os.scandir(path2):
        if obj.is_dir():
            obj_type = 'directory'
        elif obj.is_file():
            obj_type = 'file'
        elif obj.is_link():
            obj_type = 'symbolik link'
        else:
            obj_type = 'others'
        print(obj.name, 'is', obj_type)

    # 4
    print('#4')
    import os
    file_location = 'C:\\jetbrains-crack.jar'
    print('existance:', os.access(file_location, os.F_OK))
    print('readable:', os.access(file_location, os.R_OK))
    print('writable:', os.access(file_location, os.W_OK))
    print('executable:', os.access(file_location, os.X_OK))

    # 5
    print('#5')
    import os
    file_location = 'C:\\jetbrains-crack.jar'
    print('file location:', file_location)
    file_status = os.stat(file_location)
    print('file size:', file_status.st_size)
    print('file mode:', bin(file_status.st_mode))
    print('file owner id:', file_status.st_uid)
    print('file device:', file_status.st_dev)
    import time
    print('file created in:', time.ctime(file_status.st_ctime))
    print('file modified in:', time.ctime(file_status.st_mtime))
    print('file accessed in:', time.ctime(file_status.st_atime))