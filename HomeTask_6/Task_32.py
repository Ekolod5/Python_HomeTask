# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).


from Module_1 import create_list, indexes_array


num_list = create_list(int(input('Введите размер массива: ')))
left_range = int(input('Введите минимум диапазона: '))
right_range = int(input('Введите максимум диапазона: '))


print(*num_list)
print(*indexes_array(num_list, left_range, right_range))
