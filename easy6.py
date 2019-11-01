# ������-1: �������� ����� ��� ������-������������, ��������� ������������ ���� �����.
# ���������� ������, ����������� ���������: �������, ������ � �������� ������.
import math
 
 
class Triangle:
    def __init__(self, A, B, C):
        # ������� ��������� ����� ������� �������� ����������� �����
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
 
        self.A = A
        self.B = B
        self.C = C
        # �� ��������� �������� ��������� ��������� ����� ������� AB
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)
 
    # ���������� ������� ������������ �� ������� ������
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2
 
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))
 
    # ��������� �������� ������������
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA
 
    # ��������� ������ ������������
    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)
 
 
treugolnik1 = Triangle((3, 2), (6, 7), (0, 12))
 
print(treugolnik1.areaTriangle())
print(treugolnik1.heightTriangle())
print(treugolnik1.perimeterTriangle())
 
 
# ������-2: �������� ����� "����������� ��������", �������� ������������ 4-� �����.
# ������������� � ������ ������:
# ��������, �������� �� ������ ����������� ���������;
# ����������: ����� ������, ��������, �������.
 
class Trapeze:
    def __init__(self, A, B, C, D):
        # ������� ��������� ����� ������� �������� ����������� �����
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
 
        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2
 
            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))
 
        self.A = A
        self.B = B
        self.C = C
        self.D = D
 
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CD = sideLen(self.C, self.D)
        self.DA = sideLen(self.D, self.A)
        self.diagonal_AC = sideLen(self.C, self.A)
        self.diagonal_BD = sideLen(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA
 
        # ���������� �������� ��� 2 ������������ � ������ 2 ������� ���� �������������
        # ��� ����� � ��� ���� ��� ����������� ����� ������
        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) \
                    + areaTriangle(self.diagonal_BD, self.BC, self.CD)
 
    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False