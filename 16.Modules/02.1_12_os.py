
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

    # 6
    # in unix
    '''
    print('#6')
    import os
    path2 = 'F:\music' + os.path.basename(__file__)
    print('creating link from {} to {}'.format(path2, __file__))
    os.symlink(__file__, path2)
    file_status2 = os.lstat(path2)
    print("file mode:", file_status2.st_mode())
    print("Points to : ", os.readlink(path2))
    os.unlink(path2)
    '''
    # 7
    import os
    print('#7')
    with open('test1.txt', 'w') as file1:
        file1.write('Python program to create a symbolic link and read it to decide the original file pointed by the link.')
    print('dirs: ', os.listdir())
    with open('test1.txt', 'r') as file1:
        print('file content:', file1.read())
    os.rename('test1.txt' , 'test1.txt' )
    with open( 'test1.txt' , 'r' ) as file1:
        print('renamed file content: ', file1.read())
    # 8
    print('#8')
    print('process id is:', os.getpid())
    print('parent process id is:', os.getppid())
    #print('user id is::', os.getuid())     # in Unix
    #os.setuid(1330)   # in unix
    #print('user id is:', os.getuid())

    # 9
    print('#9')
    import os
    print("current dir:", os.getcwd())
    print('change to parent directory: ')
    os.chdir(os.pardir)
    print('parent directory is:', os.getcwd())
    os.chdir('./16.Modules/Examples')
    print(os.getcwd())

    # 10
    print('#10')
    import os
    print('environment variables are:')
    print(os.environ)
    print('access environment variables:')
    print('HOMEPATH environment variable:', os.environ['HOMEPATH'])
    print('ALLUSERSPROFILES env variable:', os.environ['ALLUSERSPROFILE'])
    print('get environment vriables:')
    print('PYTHONPATH environment variable:', os.getenv('PYTHONPATH'))
    print('JAVA environment variable: ', os.getenv('JAVA'))

    # 11
    print('#11')
    import os
    path3 = r'F:\E-learning\EDX_Courses\EDX-Microsoft Intermediate C++'
    for root, dirs, files in os.walk(path3):
        print(root, '-->')
        for _dir in dirs:
            print('  ', _dir, '-->')
        for file in files:
            print('    ', file)

    # 12
    print('#12')
    import os
    
