﻿# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
     number = number*(10**ndigits)+0.41
     number = number//1
     return number/(10**ndigits)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

    ticket_number = repr(ticket_number)
    left_part = ticket_number[:3]
    right_part = ticket_number[-3:]

    def part_sum(str_part):
        counter = 0
        for n in str_part:
            counter += int(n)
        return counter

    if part_sum(left_part) == part_sum(right_part):
        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(123241))
print(lucky_ticket(436751))

