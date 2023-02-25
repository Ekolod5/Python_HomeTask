# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны 
# быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой 
# ровно два аргумента, как, например, у операции умножения.
# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1   2   3   4   5   6   
# 2   4   6   8   10  12  
# 3   6   9   12  15  18  
# 4   8   12  16  20  24  
# 5   10  15  20  25  30  
# 6   12  18  24  30  36 


# matrix = [
#     [1, 2, 3, 4, 5, 6],
#     [2, 21, 31, 41, 5, 6],
#     [3, 22, 32, 42, 5, 6],
#     [4, 23, 33, 43, 5, 6],
#     [5, 24, 34, 44, 5, 6],
#     [6, 25, 35, 45, 5, 6]
# ]
# matr = []
# for i in range(1, 7):
#     temp = []
#     for j in range(1, 7):
#         temp.append(i*j)
#     matr.append(temp)
# for i in matr:
#     print(''.join(f'{n:<4}' for n in i))  


def print_operation_table(operation, num_rows = 6, num_columns = 6):
    table = []
    for i in range(1, num_rows + 1):
        table_1 = []
        for j in range(1, num_columns + 1):
            table_1.append(operation(i, j))
        table.append(table_1)
    for i in table:
        print(''.join(f'{n:<4}' for n in i)) 


print_operation_table(lambda x, y: x * y)
