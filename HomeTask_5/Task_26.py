# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3**5)
# A = 2; B = 3 -> 8

a = int(input('Введите первое число A: '))
b = int(input('Введите второе число B: '))
def res(a, b):
    if b == 1:
        return a
    if b != 1:
        return (a * res(a, b - 1))  
print(res(a, b))
