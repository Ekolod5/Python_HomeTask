# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Пример: 
# 6 -> 1 4 1
# 24 -> 4 16 4 
# 60 -> 10 40 10

# x, x, 4x = 6x
s = int(input('Сколько журавликов всего сделано: '))
if s % 6 != 0:
    print(f'Число S = {s} не соответствует условиям задачи')
else:
    x = s // 6
    print(f'{s} -> {x} {4 * x} {x}')
