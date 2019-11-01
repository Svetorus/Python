# �������-1:
# ���������� �������� ���� ������, ��������� ��������� ���:
# � ����� ���� ������(5�, 7� � �.�.), � ������� ������ �������.
# � ������� ������� ���� ��� ��������(���� � ����).
# ����� � ����� ��������� �������. ���� ������� ����� ����������� 
# � �������������� ���-�� ������� ���� ������������ �������. 
# �.�. ������� ������ ����� ����������� ���������� � 5� � 6�,
# �� ������ ���������� �� ����� ����������� ����� ������.

# ��������� � ����������� ������� ��������� ������ ������ ��������� ������:
# 1. �������� ������ ������ ���� ������� �����
# 2. �������� ������ ���� �������� � ��������� ������
#  (������ ������ ������������ � ������� "������� �.�.")
# 3. �������� ������ ���� ��������� ���������� ������� 
#  (������ --> ����� --> ������� --> ��������)
# 4. ������ ��� ��������� ���������� �������
# 5. �������� ������ ���� ��������, ����������� � ��������� ������

class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
 
    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname
 
    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())
 
 
# if __name__ == '__main__':  # ������������.
#     people1 = People('����', '��������', '������')
#     print(people1.get_full_name())
#     print(people1.get_short_name())
 
 
class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class
 
 
# if __name__ == '__main__':  # ������������.
#     st_1 = Student('�����', '���������', '�������', '���� ���������', '�������� �������', '7�')
#     st_2 = Student('������', '���������', '�������', '����� ��������', '������ �������', '7�')
#     st_3 = Student('����', '��������', '������', '���� �������', '���� ������', '7�')
#     print(Student.all_classes(st_1))
 
 
class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
 
 
class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}
 
 
 
if __name__ == '__main__':  # ������������.
    teachers = [Teacher('����', '��������', '������', '����������'),
                Teacher('����', '��������', '������', '����������'),
                Teacher('�����', '���������', '�������', '������'),
                Teacher('�������', '����������', '��������', '�������'),
                Teacher('������', '����������', '�������', '��������')]
    classes = [Class_rooms('11 �', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('11 �', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 �', [teachers[3], teachers[1], teachers[0]])]
    parents = [People('�����', '���������', '�������'),
               People('��������', '����������', '��������'),
               People('�����', '���������', '�������'),
               People('�����', '���������', '��������'),
               People('������', '���������', '�������'),
               People('����', '���������', '��������')]
    students = [Student('�����', 'C��������', '�������', parents[0], parents[1], classes[0]),
                Student('�����', '��������', '��������', parents[2], parents[3], classes[1]),
                Student('���������', '���������', '�������', parents[4], parents[5], classes[2])]
    print('������ ������� � �����: ')
    for f in classes:
        print(f.class_room)
 
    for f in classes:
        print('�������, ����������� � {} ������:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("������� � ������ {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())
 
    # for f in students:
    #     print('������ ��������� ������� {}'.format(f.school_class))
    #     for teacher in classes[0].teachersdict.values():
    #         print(teacher.get_full_name())