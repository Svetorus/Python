# ������-1:
# �������� ������, ��������� ���������� dir_1 - dir_9 � �����,
# �� ������� ������� ������ ������.
# � ������ ������, ��������� ��� �����.

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


# ������-2:
# �������� ������, ������������ ����� ������� ����������.

import os

list = os.listdir()
for i in list:
    print(i)

# ������-3:
# �������� ������, ��������� ����� �����, �� �������� ������� ������ ������.

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
        print(dir_path + ' - ����� ���������� ���')


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - ������� ����������')
    except:
        print(dir_path + ' - ����� ���������� ���')

# dir_path = 'C:\\Users\\
change_dir(dir_path)