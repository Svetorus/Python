# # def f(a,b,*qweqweqe, c):
# #     print(a,b,qweqweqe,c )
# #
# # f(3,4,5,6,7,8,9,0, c=54)
#
#
# # def g(*args, **kwargs):
# #     print(args, kwargs)
# #
# # g(1,2,3,4, name="Andrey", surname="Pak", age="26")
#
#
#
# # def f():
# #     pass
#
#
#
# import datetime
#
# week = {
#     0: "пн",
#     1: "вт",
#     2: "ср",
#     3: "чт",
#     4: "пт",
#     5: "сб",
#     6: "вс",
# }
#
# d = datetime.date(2019, 9, 1)
#
# for i in range(100):
#     num = f"{d.day}{d.month}{d.year}"
#     s = sum(map(int, num))
#     while s >= 12:
#         s = sum(map(int, str(s)))
#
#     if s in [8, 9, 11] and week[d.weekday()] in ['вс', 'пт']:
#         print(d, week[d.weekday()], s)
#     d += datetime.timedelta(days=1)
#
# import sys
#
# class A:
#     __slots__ = ["name", "id", "surname"]
#     pass
#
#
#
#
# a = A()
#
# a.name = "Andrey"
# a.surname = "Pak"
# a.id = 1234
# # a.qwe = 2143
#
# # print(a.name, a.surname, a.id)
# # print(a)
#
#
# d = dict()
#
# print(sys.getsizeof(a))

a = ["russia", "usa", "france"]
b = ['r', 'u', 'f']

d = dict(zip(b,a))

print(d["r"])

print(d['u'])
