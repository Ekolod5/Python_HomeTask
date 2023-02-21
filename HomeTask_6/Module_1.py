
def arithmetic_prog(a1: int, d: int, n:int):
    sequence = [a1]
    for i in range(2, n + 1):
        sequence.append(a1 + (i - 1) * d)
    return sequence


def create_list(x: int):
    list_1 = []
    for _ in range(x):
        list_1.append(int(input('Введите число: ')))
    return list_1


def indexes_array(num_list: list, start: int, end: int):
    indexes_list = []
    for i in range(len(num_list)):
        if start <= num_list[i] <= end:
            indexes_list.append(i)
    return indexes_list
