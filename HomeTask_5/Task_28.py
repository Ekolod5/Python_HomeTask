# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Пример:
# 2 2
# 4


a = int(input('Введите первое число a: '))
b = int(input('Введите второе число b: '))


def sum_1(a, b):
    if b > a:
        a, b = b, a
    elif b == 0:
        return a
    return 1 + sum_1(a, b - 1)


print(sum_1(a, b))
