# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример: 
# 123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))
if 99 < number < 1000:
    print('Сумма цифр трехзначного числа:', number // 100 + number // 10 % 10 + number % 10)
else:
    print('Вы ввели не 3-х значное число')
