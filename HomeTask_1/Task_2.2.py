# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример: 
# 123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)

num = input('Введите трехзначное число: ')
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print(res)
else:
    print('Вы ввели не 3-х значное число')
