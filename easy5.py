# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

path = "directory"

def create_directories(count):
    for i in range(1, count+1):
        path = f"dir_{i}"
        if not os.path.exists(path):
            os.mkdir(path)

def remove_directories(count):
    for i in range(1, count+1):
        path = f"dir_{i}"
        if os.path.exists(path):
            os.rmdir(path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

list = os.listdir()
for i in list:
    print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import os
import sys

def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)


first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file,backup_file)


def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        0
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')

# dir_path = 'C:\\Users\\
change_dir(dir_path)