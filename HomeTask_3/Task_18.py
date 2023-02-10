# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

n = int(input('Введите количество элементов в массиве, натуральное число N: '))
list_1 = [randint(1, n) for i in range(n)]
print(list_1)
input_set = set(list_1)
num = int(input('Введите число X: '))
dif = 0
if num > max(input_set):
    print(max(input_set))
elif num < min(input_set):
    print(min(input_set))
else:
    while True:
        if num - dif in input_set and num + dif in input_set and num - dif != num + dif:
            print(num - dif, num + dif)
            break
        elif num - dif in input_set:
            print(num - dif)
            break 
        elif num + dif in input_set:
            print(num + dif)
            break
        else:
            dif += 1
