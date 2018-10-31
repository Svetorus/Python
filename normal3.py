# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]


print('fibonacci(1, 8): ', fibonacci(1, 8))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    if len(origin_list) > 1:
        pivot_index = len(origin_list) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(origin_list):
            if i != pivot_index:
                if val < origin_list[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        sort_to_max(smaller_items)
        sort_to_max(larger_items)
        origin_list[:] = smaller_items + [origin_list[pivot_index]] + larger_items
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_list(fucnt, param_b):
    end_list = list()
    for x in param_b:
        if fucnt(x) == True:
            end_list.append(x)
        else:
            continue
    return end_list
 
 
print((filter_list((lambda x: x > 5), param_b=[1, 100, 500, 7, 8, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


