# ������-1:
# �������� ��������� ���������� �������,
# ����������� �������� � ������� ������� ����������.
# ������� ������ ����� ���� ������ ��������, � ������� ����� ������:
# 1. ������� � �����
# 2. ����������� ���������� ������� �����
# 3. ������� �����
# 4. ������� �����
# ��� ������ ������� 1, 3, 4 ��������� ����������� �������� �����
# � ������� ��������� ��������: "������� �������/�������/�������",
# "���������� �������/�������/�������"
 
# ��� ������� ������ ������ ����������� ��������� �� ������� �����,
# ����������� � ���� ��������������� �������,
# � ��������������� � ������ ���� �� easy.py

import os
#import easy

quitz ='a'
while quitz != '0':
    print('������� ����� - ������� 1')
    print('����������� ��� � ����� - ������� 2')
    print('������� ����� - ������� 3')
    print('������� ����� - ������� 4')
    print('��� ������ - ������� 0')
    quitz = input('�������: ' )
    print(quitz)
    if quitz == '1':
        dir_name = input ('�������� ���� �����: ')
        easy.change_dir(dir_name)
    elif quitz == '2':
        dir_name = os.getcwd()
        easy.list_dir(dir_name)
    elif quitz == '3':
        dir_name = input('�������� ���� �����: ')
        easy.delete_dir(dir_name)
    elif quitz == '4':
        dir_name = input('�������� ���� �����: ')
        easy.make_dir(dir_name)
    elif quitz == '0':
        pass
    else:
        print('������ ������ ���� ���')